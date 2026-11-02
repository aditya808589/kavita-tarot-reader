import urllib.request, json, time, base64, os
from pathlib import Path

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID
ROOT = Path(__file__).resolve().parent.parent

# Load products from assets/store-data.js
with open(ROOT / 'assets/store-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.find('];', start)
store_products = json.loads(text[start:end+1])

packages = store_products[30:] # items 31 to 38
print(f"Creating/updating {len(packages)} signature reading packages in Shopify Admin...")

# Fetch existing products in Shopify
req = urllib.request.Request(
    f'https://{STORE}/admin/api/2024-01/products.json?limit=250',
    headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}
)
existing_handles = {}
with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode())
    for p in data.get('products', []):
        existing_handles[p['handle']] = p['id']

for pkg in packages:
    handle = pkg['handle']
    title = pkg['title']
    price = pkg['price']
    compare_price = pkg['comparePrice']
    desc = pkg['description'].replace('\n', '<br>')
    benefits_html = ''.join(f'<li>{b}</li>' for b in pkg.get('benefits', []))
    body_html = f"<p>{desc}</p><h4>Sacred Highlights:</h4><ul>{benefits_html}</ul><p><strong>Vedic Cleansing & Energization:</strong> Each reading session is consecrated and aligned with pure intuitive channeling by Kavita.</p>"
    
    # Read image
    img_path = ROOT / pkg['img']
    img_b64 = None
    if img_path.exists():
        with open(img_path, 'rb') as img_f:
            img_b64 = base64.b64encode(img_f.read()).decode('utf-8')

    product_payload = {
        'product': {
            'title': title,
            'body_html': body_html,
            'vendor': 'Kavita — Tarot & Spirituals',
            'product_type': 'Tarot Readings & Consultations',
            'handle': handle,
            'status': 'active',
            'tags': 'tarot, readings, package, signature, voice-note',
            'variants': [{
                'price': f"{price:.2f}",
                'compare_at_price': f"{compare_price:.2f}" if compare_price else None,
                'requires_shipping': False,
                'inventory_management': None,
                'fulfillment_service': 'manual'
            }]
        }
    }
    if img_b64:
        product_payload['product']['images'] = [{
            'attachment': img_b64,
            'filename': f"{handle}.jpg"
        }]

    if handle in existing_handles:
        p_id = existing_handles[handle]
        print(f"Product '{handle}' already exists (ID: {p_id}), updating...")
        product_payload['product']['id'] = p_id
        put_req = urllib.request.Request(
            f'https://{STORE}/admin/api/2024-01/products/{p_id}.json',
            data=json.dumps(product_payload).encode('utf-8'),
            headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'},
            method='PUT'
        )
        try:
            with urllib.request.urlopen(put_req, timeout=15) as resp:
                print(f"✓ Updated product: {title}")
        except Exception as e:
            print(f"Error updating {handle}: {e}")
    else:
        print(f"Creating new product: {title} ({handle})...")
        post_req = urllib.request.Request(
            f'https://{STORE}/admin/api/2024-01/products.json',
            data=json.dumps(product_payload).encode('utf-8'),
            headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'},
            method='POST'
        )
        try:
            with urllib.request.urlopen(post_req, timeout=15) as resp:
                res_data = json.loads(resp.read().decode())
                new_id = res_data.get('product', {}).get('id')
                print(f"✓ Created product ID {new_id}: {title}")
        except Exception as e:
            print(f"Error creating {handle}: {e}")
    time.sleep(0.5)

print("\nAll 8 signature reading packages synchronized with Shopify Admin!")

