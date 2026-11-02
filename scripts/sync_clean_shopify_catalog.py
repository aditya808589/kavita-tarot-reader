import urllib.request, json, time, base64, os
from pathlib import Path

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
        with urllib.request.urlopen(req) as resp:
            if resp.status == 204:
                return {}
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        print(f"HTTP {e.code} on {method} {endpoint}: {err_msg}")
        return None

# 1. Fetch all products
print("Fetching all existing Shopify products...")
all_prods = []
url_endpoint = 'products.json?limit=250'
res = shopify_req(url_endpoint)
if res:
    all_prods = res.get('products', [])

print(f"Total products in store: {len(all_prods)}")

# 2. Identify and delete dummy products & old mock products
dummy_titles = ["I'm a product", "Brush Set", "Matte Lipstick", "Face Gloss"]
old_mock_handles = [
    'distance-cord-cutting-healing',
    'lamafera-ancient-energy-healing',
    'celestial-moon-intuition-oracle-cards',
    'moroccan-selenite-cleansing-wand',
    'sacred-gold-foil-major-arcana-deck',
    'situational-tarot-packages',
    'natural-golden-pyrite-wealth-cluster',
    'raw-amethyst-calming-intuition-cluster',
    '7-chakra-radiance-bracelet',
    'live-audio-call-tarot-reading',
    'whatsapp-voice-note-tarot-reading',
    'vortex-of-blessings-session'
]

deleted_count = 0
for p in all_prods:
    pid = p['id']
    title = p['title'].strip()
    handle = p['handle'].strip()

    is_dummy = any(title.startswith(d) for d in dummy_titles) or handle in old_mock_handles
    if is_dummy:
        print(f"Deleting dummy/old product: [{pid}] {title} ({handle})")
        shopify_req(f'products/{pid}.json', method='DELETE')
        deleted_count += 1
        time.sleep(0.3)

print(f"Deleted {deleted_count} dummy products.")

# 3. Read store-data.js to map authentic catalog to Shopify products
with open(ROOT / 'assets/store-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# parse STORE_PRODUCTS array
match = re.search(r'const STORE_PRODUCTS = (\[.*?\]);\n\n/\*', text, re.DOTALL)
if not match:
    print("Could not match STORE_PRODUCTS in store-data.js")
    exit(1)

store_products = json.loads(match.group(1))
print(f"Loaded {len(store_products)} products from store-data.js")

# Re-fetch remaining authentic products from Shopify
res = shopify_req('products.json?limit=250')
remaining_prods = res.get('products', []) if res else []
print(f"Remaining authentic products in Shopify: {len(remaining_prods)}")

# Map by original handle (e.g. product_<uuid>)
prods_by_orig_handle = {p['handle'].lower(): p for p in remaining_prods}

# Load wix-store-export to get UUID for each item
import csv
with open(ROOT / 'wix-store-export.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    wix_rows = list(reader)

wix_real = [r for r in wix_rows if r['fieldType'] == 'PRODUCT' and not any(r['name'].strip().startswith(d) for d in dummy_titles)]
wix_handle_by_name = {r['name'].strip(): r['handle'].lower() for r in wix_real}

updated_count = 0
for p_data in store_products:
    target_handle = p_data['handle']
    title = p_data['title']
    price = str(p_data['price'])
    compare_price = str(p_data['comparePrice']) if p_data.get('comparePrice') and p_data['comparePrice'] > p_data['price'] else None
    
    # Find matching Shopify product
    # Try exact title or wix UUID
    sh_prod = None
    for p in remaining_prods:
        if p['handle'] == target_handle or p['title'] == title or p['title'].lower() in title.lower():
            sh_prod = p
            break
            
    if not sh_prod:
        # Check wix handle match
        for w_name, w_h in wix_handle_by_name.items():
            if w_name.lower() in title.lower() or title.lower() in w_name.lower():
                sh_prod = prods_by_orig_handle.get(w_h)
                if sh_prod:
                    break

    if sh_prod:
        pid = sh_prod['id']
        vid = sh_prod['variants'][0]['id']
        print(f"Updating [{pid}] -> handle: {target_handle} | {title} (₹{price})")
        update_body = {
            'product': {
                'id': pid,
                'handle': target_handle,
                'title': title,
                'status': 'active',
                'variants': [{
                    'id': vid,
                    'price': price,
                    'compare_at_price': compare_price
                }]
            }
        }
        shopify_req(f'products/{pid}.json', data=update_body, method='PUT')
        updated_count += 1
        time.sleep(0.3)

        # Upload high-res image if none or replace
        img_local = ROOT / p_data['img']
        if img_local.exists() and len(sh_prod.get('images', [])) == 0:
            with open(img_local, 'rb') as img_f:
                b64_img = base64.b64encode(img_f.read()).decode('utf-8')
            img_body = {
                'image': {
                    'attachment': b64_img,
                    'filename': img_local.name
                }
            }
            shopify_req(f'products/{pid}/images.json', data=img_body, method='POST')
            print(f"  Uploaded high-res photo: {img_local.name}")
            time.sleep(0.3)
    else:
        print(f"Creating new product in Shopify: {title} ({target_handle})...")
        create_body = {
            'product': {
                'title': title,
                'handle': target_handle,
                'body_html': f"<p>{p_data['description']}</p>",
                'status': 'active',
                'product_type': p_data['categoryLabel'],
                'variants': [{
                    'price': price,
                    'compare_at_price': compare_price
                }]
            }
        }
        new_res = shopify_req('products.json', data=create_body, method='POST')
        if new_res and 'product' in new_res:
            new_pid = new_res['product']['id']
            print(f"  Created new product ID: {new_pid}")
            img_local = ROOT / p_data['img']
            if img_local.exists():
                with open(img_local, 'rb') as img_f:
                    b64_img = base64.b64encode(img_f.read()).decode('utf-8')
                img_body = {
                    'image': {
                        'attachment': b64_img,
                        'filename': img_local.name
                    }
                }
                shopify_req(f'products/{new_pid}/images.json', data=img_body, method='POST')
                print(f"  Uploaded photo for new product: {img_local.name}")
        time.sleep(0.3)

print(f"\nShopify sync complete! Updated {updated_count} products.")

