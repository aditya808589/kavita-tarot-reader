import json, urllib.request, base64, time
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shopify_config import TOKEN, STORE

ROOT = Path(__file__).resolve().parent.parent

def shopify_api(endpoint, method='GET', payload=None):
    url = f"https://{STORE}/admin/api/2024-01/{endpoint}"
    data = json.dumps(payload).encode('utf-8') if payload else None
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "X-Shopify-Access-Token": TOKEN,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        },
        method=method
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("1. Updating Product 8857782943905 with unified variants and 3 professional photos...")
with open(ROOT / "assets/product-healing-oil-love-relationships.jpg", "rb") as f:
    img1_b64 = base64.b64encode(f.read()).decode("utf-8")
with open(ROOT / "assets/product-healing-oil-money-attraction.jpg", "rb") as f:
    img2_b64 = base64.b64encode(f.read()).decode("utf-8")
with open(ROOT / "assets/product-healing-oil-study-focus.jpg", "rb") as f:
    img3_b64 = base64.b64encode(f.read()).decode("utf-8")

oil_body = """
<p><strong>Awaken divine alignment, emotional harmony, and unstoppable prosperity with the Aromatherapy & Sacred Healing Oil.</strong></p>
<p>Formulated with pure therapeutic-grade essential oils and infused with genuine, Vedic-consecrated crystal chips settled right inside the roll-on bottle. Convenient 10ml size with luxury gold cap and presentation box.</p>
<h4>✦ Available Sacred Blends:</h4>
<ul>
  <li>💖 <strong>Love & Relationships:</strong> Infused with natural Rose Quartz crystals to awaken unconditional love, heart healing, and soulmate magnetism.</li>
  <li>💰 <strong>Money Attraction:</strong> Infused with golden Pyrite & Citrine crystals to dissolve scarcity fears and magnetize wealth, promotions & financial luck.</li>
  <li>🧠 <strong>Study & Concentration:</strong> Infused with deep-blue Sodalite & Quartz crystals to eliminate brain fog and lock in laser focus & memory retention.</li>
</ul>
<p><strong>Package:</strong> 10ml Roll-on glass bottle with gold cap & display box.</p>
<p><strong>How to Use:</strong> Roll gently onto pulse points (wrists, behind ears, neck, or collarbone) before sleep, study, work, or dates while setting your intention.</p>
"""

# Update product details and options
oil_payload = {
    "product": {
        "id": 8857782943905,
        "title": "Aromatherapy & Sacred Healing Oil (With Energized Crystals)",
        "body_html": oil_body,
        "options": [
            {
                "name": "Sacred Blend"
            }
        ],
        "variants": [
            {
                "id": 48762496319649,
                "option1": "Love & Relationships (Rose Quartz)",
                "price": "777.00",
                "compare_at_price": "1299.00",
                "sku": "oil-love-relationships",
                "requires_shipping": True
            },
            {
                "option1": "Money Attraction (Pyrite & Citrine)",
                "price": "777.00",
                "compare_at_price": "1299.00",
                "sku": "oil-money-attraction",
                "requires_shipping": True
            },
            {
                "option1": "Study & Concentration (Sodalite & Quartz)",
                "price": "777.00",
                "compare_at_price": "1299.00",
                "sku": "oil-study-concentration",
                "requires_shipping": True
            }
        ],
        "images": [
            {"attachment": img1_b64, "filename": "product-healing-oil-love-relationships.jpg"},
            {"attachment": img2_b64, "filename": "product-healing-oil-money-attraction.jpg"},
            {"attachment": img3_b64, "filename": "product-healing-oil-study-focus.jpg"}
        ]
    }
}

resp_oil = shopify_api("products/8857782943905.json", method="PUT", payload=oil_payload)
prod_updated = resp_oil.get("product", {})
print(f"Updated Oil Product: {prod_updated.get('title')}")
oil_variants = prod_updated.get("variants", [])
for v in oil_variants:
    print(f"  Variant: {v.get('title')} -> ID: {v.get('id')}")

time.sleep(1)

# Delete duplicate products 8857783107745 and 8857783271585
for del_id in [8857783107745, 8857783271585]:
    try:
        shopify_api(f"products/{del_id}.json", method="DELETE")
        print(f"Deleted duplicate product {del_id}")
    except Exception as e:
        print(f"Could not delete {del_id}: {e}")

time.sleep(1)

# Update the 4 bath salt product images on Shopify
bath_salts = [
    (8857783402657, ROOT / "assets/product-bath-salt-aura-booster.jpg", "product-bath-salt-aura-booster.jpg"),
    (8857783500961, ROOT / "assets/product-bath-salt-energy-booster.jpg", "product-bath-salt-energy-booster.jpg"),
    (8857783632033, ROOT / "assets/product-bath-salt-coffee.jpg", "product-bath-salt-coffee.jpg"),
    (8857783730337, ROOT / "assets/product-bath-salt-health-booster.jpg", "product-bath-salt-health-booster.jpg"),
]

for pid, path, fname in bath_salts:
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    payload = {
        "product": {
            "id": pid,
            "images": [
                {"attachment": b64, "filename": fname}
            ]
        }
    }
    shopify_api(f"products/{pid}.json", method="PUT", payload=payload)
    print(f"Updated professional graphic for Bath Salt {pid} -> {fname}")
    time.sleep(0.5)

print("\nAll Shopify products and graphics successfully updated!")

