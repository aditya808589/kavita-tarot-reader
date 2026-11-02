import urllib.request, json, base64
from pathlib import Path

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID
PRODUCT_ID = 8844156043425
IMG_PATH = Path('assets/product-meditation-tumbles.jpg')

with open(IMG_PATH, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

payload = json.dumps({
    "image": {
        "attachment": b64,
        "alt": "Meditation Crystal Tumbles"
    }
}).encode('utf-8')

req = urllib.request.Request(
    f"https://{STORE}/admin/api/2024-01/products/{PRODUCT_ID}/images.json",
    data=payload,
    headers={
        "X-Shopify-Access-Token": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode())
        img = data.get("image", {})
        print(f"SUCCESS: Attached image {img.get('id')} to Shopify product {PRODUCT_ID}!")
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.read().decode()}")
except Exception as e:
    print(f"Error: {e}")

