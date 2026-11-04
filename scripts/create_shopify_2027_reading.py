import json, urllib.request, base64
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shopify_config import TOKEN, STORE

ROOT = Path(__file__).resolve().parent.parent

# Read images
cover_path = ROOT / 'assets/product-2027-year-ahead-cover.jpg'
details_path = ROOT / 'assets/product-2027-year-ahead-details.jpg'

with open(cover_path, 'rb') as f:
    cover_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(details_path, 'rb') as f:
    details_b64 = base64.b64encode(f.read()).decode('utf-8')

title = "2027 Year-Ahead Reading – Complete Year, Month-by-Month (Diwali Special)"
handle = "2027-year-ahead-reading-diwali-special"

body_html = """
<p><strong>What will 2027 bring for you? ✨</strong></p>
<p>This Diwali, get your complete year mapped out in one deep, personal tarot reading. I go month by month through all 12 months of 2027 so you know what's coming in love, money and career, and when to act.</p>
<h4>✦ What you get:</h4>
<ul>
  <li>🗓️ <strong>Month-by-month guidance</strong> for all 12 months of 2027</li>
  <li>❤️ <strong>Love and relationships</strong> outlook & milestones</li>
  <li>💰 <strong>Money and finances</strong> timeline</li>
  <li>💼 <strong>Career and growth</strong> opportunities</li>
  <li>🪔 <strong>Your personal Lakshmi remedy</strong> for prosperity in 2027</li>
  <li>✨ <strong>FREE bonus:</strong> your 2027 lucky colour + lucky months</li>
</ul>
<p><strong>Format:</strong> Voice note reading, delivered on WhatsApp within 10 days of booking.</p>
<p><em>After payment, share your name, date of birth and any focus area on WhatsApp: +91 93103 87104</em></p>
<p><strong>⏳ Diwali price ₹3,333 (regular ₹5,555). Only 21 slots.</strong></p>
"""

product_payload = {
    "product": {
        "title": title,
        "handle": handle,
        "body_html": body_html,
        "vendor": "Kavita Tarot Reader",
        "product_type": "Tarot Reading",
        "status": "active",
        "tags": "2027, Diwali Special, Tarot Reading, Voice Note, Year Ahead, Exclusive",
        "variants": [
            {
                "price": "3333.00",
                "compare_at_price": "5555.00",
                "requires_shipping": False,
                "inventory_management": None,
                "inventory_policy": "continue"
            }
        ],
        "images": [
            {
                "attachment": cover_b64,
                "filename": "product-2027-year-ahead-cover.jpg",
                "alt": "2027 Year-Ahead Reading – Complete Year, Month-by-Month"
            },
            {
                "attachment": details_b64,
                "filename": "product-2027-year-ahead-details.jpg",
                "alt": "What You Get in 2027 Year-Ahead Reading"
            }
        ]
    }
}

# Check if product already exists
check_req = urllib.request.Request(
    f"https://{STORE}/admin/api/2024-01/products.json?handle={handle}",
    headers={"X-Shopify-Access-Token": TOKEN}
)

existing_prod = None
try:
    with urllib.request.urlopen(check_req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        products = data.get("products", [])
        if products:
            existing_prod = products[0]
            print(f"Product already exists with ID {existing_prod['id']}")
except Exception as e:
    print(f"Check error: {e}")

if existing_prod:
    prod_id = existing_prod['id']
    variant_id = existing_prod['variants'][0]['id']
    # Update product
    update_payload = {
        "product": {
            "id": prod_id,
            "title": title,
            "body_html": body_html,
            "variants": [
                {
                    "id": variant_id,
                    "price": "3333.00",
                    "compare_at_price": "5555.00"
                }
            ]
        }
    }
    req = urllib.request.Request(
        f"https://{STORE}/admin/api/2024-01/products/{prod_id}.json",
        data=json.dumps(update_payload).encode('utf-8'),
        headers={"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        prod = res['product']
        print(f"Updated product ID: {prod['id']}, Variant ID: {prod['variants'][0]['id']}")
else:
    # Create product
    req = urllib.request.Request(
        f"https://{STORE}/admin/api/2024-01/products.json",
        data=json.dumps(product_payload).encode('utf-8'),
        headers={"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        prod = res['product']
        print(f"Created product ID: {prod['id']}, Variant ID: {prod['variants'][0]['id']}")

print(f"Product URL: https://{STORE}/products/{handle}")
print(f"Variant ID: {prod['variants'][0]['id']}")

