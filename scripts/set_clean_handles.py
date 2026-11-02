import urllib.request, json, time, base64
from pathlib import Path
import csv

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID
ROOT = Path(__file__).resolve().parent.parent

headers = {
    'X-Shopify-Access-Token': TOKEN,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

def shopify_req(endpoint, data=None, method='GET'):
    url = f'https://{STORE}/admin/api/2024-01/{endpoint}'
    payload = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 204:
                return {}
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        print(f"HTTP {e.code} on {method} {endpoint}: {err_msg}")
        return None
    except Exception as e:
        print(f"Error on {method} {endpoint}: {e}")
        return None

# 1. Delete 4 duplicates if they exist
dup_ids = [8843690836129, 8843690901665, 8843690934433, 8843690967201]
for did in dup_ids:
    print(f"Deleting duplicate product {did}...")
    shopify_req(f'products/{did}.json', method='DELETE')
    time.sleep(0.3)

# 2. Load store-data.js
with open(ROOT / 'assets/store-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'const STORE_PRODUCTS = (\[.*?\]);\n\n/\*', text, re.DOTALL)
store_products = json.loads(match.group(1))

# Load wix-store-export.csv to map wix handles
dummy_names = ["I'm a product", "Brush Set", "Matte Lipstick", "Face Gloss"]
with open(ROOT / 'wix-store-export.csv', 'r', encoding='utf-8') as f:
    wix_rows = list(csv.DictReader(f))

wix_real = [r for r in wix_rows if r['fieldType'] == 'PRODUCT' and not any(r['name'].strip().startswith(d) for d in dummy_names)]

# Fetch all products on Shopify
res = shopify_req('products.json?limit=250')
sh_prods = res.get('products', []) if res else []
print(f"Found {len(sh_prods)} products on Shopify.")

prods_by_handle = {p['handle'].lower(): p for p in sh_prods}

# Map each of our 42 store_products to a wix handle
# Let's inspect scripts/build_full_store_catalog.py catalog_defs
from importlib.machinery import SourceFileLoader
cat_module = SourceFileLoader("cat", str(ROOT / 'scripts/build_full_store_catalog.py')).load_module()
catalog_defs = cat_module.catalog_defs

wix_to_clean = {c['handle_key'].lower(): c for c in catalog_defs}

success = 0
for wix_h, c_def in wix_to_clean.items():
    clean_handle = c_def['handle']
    title = c_def['title']
    sh_prod = prods_by_handle.get(wix_h) or prods_by_handle.get(clean_handle)
    if not sh_prod:
        print(f"Could not find Shopify product for wix handle: {wix_h} ({title})")
        continue

    pid = sh_prod['id']
    vid = sh_prod['variants'][0]['id']
    
    # find matching in store_products
    sp = next((p for p in store_products if p['handle'] == clean_handle), None)
    price = str(sp['price']) if sp else str(sh_prod['variants'][0]['price'])
    compare = str(sp['comparePrice']) if sp and sp.get('comparePrice') and sp['comparePrice'] > sp['price'] else None

    print(f"Updating [{pid}]: {wix_h} -> {clean_handle} | {title} (₹{price})")
    update_data = {
        'product': {
            'id': pid,
            'handle': clean_handle,
            'title': title,
            'status': 'active',
            'product_type': c_def['categoryLabel'],
            'variants': [{
                'id': vid,
                'price': price,
                'compare_at_price': compare
            }]
        }
    }
    shopify_req(f'products/{pid}.json', data=update_data, method='PUT')
    success += 1
    time.sleep(0.3)

    # If no images, upload the high-res one
    if len(sh_prod.get('images', [])) == 0 and sp:
        img_p = ROOT / sp['img']
        if img_p.exists():
            with open(img_p, 'rb') as im_f:
                b64 = base64.b64encode(im_f.read()).decode('utf-8')
            img_data = {
                'image': {
                    'attachment': b64,
                    'filename': img_p.name
                }
            }
            shopify_req(f'products/{pid}/images.json', data=img_data, method='POST')
            print(f"  Uploaded photo {img_p.name}")
            time.sleep(0.3)

print(f"\nCompleted! Updated {success} products to clean handles.")

