import urllib.request, json, time, base64
from pathlib import Path

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID
ROOT = Path(__file__).resolve().parent.parent

packages = [
    ('no-contact-situation-5-card-reading', ROOT / 'assets/package-no-contact-5card.jpg'),
    ('future-spouse-reading', ROOT / 'assets/package-future-spouse.jpg'),
    ('love-marriage-pack-8-questions', ROOT / 'assets/package-love-marriage-8q.jpg'),
    ('no-contact-situation-pack-4-questions', ROOT / 'assets/package-no-contact-4q.jpg'),
    ('heart-consultation-private-healing', ROOT / 'assets/package-heart-consultation.jpg'),
    ('career-growth-reading', ROOT / 'assets/package-career-growth.jpg'),
    ('reunion-reading', ROOT / 'assets/package-reunion-reading.jpg'),
    ('deep-insight-reading-8-questions', ROOT / 'assets/package-deep-insight-8q.jpg')
]

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

print(f"Updating image assets on Shopify Admin for {len(packages)} packages...")

for handle, img_path in packages:
    if not img_path.exists():
        print(f"Skipping {handle}, image not yet ready: {img_path}")
        continue
    
    p_id = existing_handles.get(handle)
    if not p_id:
        print(f"Product {handle} not found in Shopify Admin")
        continue

    with open(img_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode('utf-8')

    # Post image to product
    img_payload = json.dumps({
        'image': {
            'attachment': img_b64,
            'filename': f"{handle}.jpg",
            'position': 1
        }
    }).encode('utf-8')

    post_req = urllib.request.Request(
        f'https://{STORE}/admin/api/2024-01/products/{p_id}/images.json',
        data=img_payload,
        headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        with urllib.request.urlopen(post_req, timeout=20) as resp:
            print(f"✓ Uploaded new image for {handle} (Product ID: {p_id})")
    except Exception as e:
        print(f"Error uploading image for {handle}: {e}")
    time.sleep(0.5)

print("\nShopify Admin package images update completed!")

