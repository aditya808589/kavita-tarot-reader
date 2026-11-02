import urllib.request, json, time, base64
from pathlib import Path

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID
ROOT = Path(__file__).resolve().parent.parent

# 1. Text uploads
text_uploads = [
    ('assets/parity-commerce.js', ROOT / 'kavita-dawn/assets/parity-commerce.js'),
    ('assets/parity-catalog.js', ROOT / 'kavita-dawn/assets/parity-catalog.js'),
    ('assets/parity-cart-render.js', ROOT / 'kavita-dawn/assets/parity-cart-render.js'),
    ('assets/parity-page.js', ROOT / 'kavita-dawn/assets/parity-page.js'),
    ('assets/parity-ui.js', ROOT / 'kavita-dawn/assets/parity-ui.js'),
    ('assets/parity-storefront-refinements.css', ROOT / 'kavita-dawn/assets/parity-storefront-refinements.css'),
    ('assets/parity-category-grid.css', ROOT / 'kavita-dawn/assets/parity-category-grid.css'),
    ('assets/parity-vanikabir.css', ROOT / 'kavita-dawn/assets/parity-vanikabir.css'),
    ('layout/parity.liquid', ROOT / 'kavita-dawn/layout/parity.liquid'),
    ('sections/parity-index.liquid', ROOT / 'kavita-dawn/sections/parity-index.liquid'),
    ('sections/parity-collections.liquid', ROOT / 'kavita-dawn/sections/parity-collections.liquid'),
    ('sections/parity-consultations.liquid', ROOT / 'kavita-dawn/sections/parity-consultations.liquid'),
    ('sections/parity-product.liquid', ROOT / 'kavita-dawn/sections/parity-product.liquid'),
    ('sections/parity-about.liquid', ROOT / 'kavita-dawn/sections/parity-about.liquid'),
    ('sections/parity-contact.liquid', ROOT / 'kavita-dawn/sections/parity-contact.liquid'),
    ('sections/parity-faq.liquid', ROOT / 'kavita-dawn/sections/parity-faq.liquid'),
    ('sections/parity-cart.liquid', ROOT / 'kavita-dawn/sections/parity-cart.liquid'),
]

# Add templates
for t in (ROOT / 'kavita-dawn/templates').glob('*.json'):
    text_uploads.append((f'templates/{t.name}', t))

print(f"Deploying {len(text_uploads)} core template/script files to live theme {THEME_ID}...")

for key, local_file in text_uploads:
    if not local_file.exists():
        continue
    with open(local_file, 'r', encoding='utf-8') as f:
        content = f.read()

    payload = json.dumps({
        'asset': {
            'key': key,
            'value': content
        }
    }).encode('utf-8')

    req = urllib.request.Request(
        f'https://{STORE}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
        data=payload,
        headers={
            'X-Shopify-Access-Token': TOKEN,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f'Uploaded: {key}', flush=True)
    except urllib.error.HTTPError as e:
        print(f'ERROR {key}: {e.code} {e.read().decode()}', flush=True)
    time.sleep(0.2)

print("\nDeploying binary product & banner images to theme assets...")
import glob
product_imgs = glob.glob(str(ROOT / 'assets/product-*.*')) + glob.glob(str(ROOT / 'assets/banner-*.*'))
for img_p in sorted(product_imgs):
    p = Path(img_p)
    key = f'assets/{p.name}'
    with open(p, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    payload = json.dumps({
        'asset': {
            'key': key,
            'attachment': b64
        }
    }).encode('utf-8')
    req = urllib.request.Request(
        f'https://{STORE}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
        data=payload,
        headers={
            'X-Shopify-Access-Token': TOKEN,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f'Uploaded asset: {key}', flush=True)
    except urllib.error.HTTPError as e:
        print(f'ERROR {key}: {e.code} {e.read().decode()}', flush=True)
    time.sleep(0.2)

print("\nLive deployment successfully completed!")
