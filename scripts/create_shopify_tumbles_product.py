import urllib.request, json

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID

product_data = {
    "product": {
        "title": "Meditation Crystal Tumbles",
        "handle": "meditation-crystal-tumbles",
        "body_html": "<p>Immerse your daily spiritual practice with our consecrated <strong>Meditation Crystal Tumbles</strong> set. Handpicked and polished to tactile perfection, this sacred collection of authentic tumbled stones features Clear Quartz, Amethyst, Rose Quartz, and Citrine—specifically selected to balance the chakras, deepen breathwork, and quiet the racing mind during meditation and prayer.</p><p>Each stone is spiritually cleansed with white sage and energized by Kavita with Vedic Beeja mantras before dispatch.</p><h4>How to Use</h4><p>Hold gently in palm during meditation, place over specific chakras while lying down, or carry in your pocket to sustain an aura of grounded calm throughout the day.</p>",
        "vendor": "Kavita Tarot Reader",
        "product_type": "Healing Crystals",
        "status": "active",
        "tags": "crystals, meditation, tumbles, peace, clarity, protection, dhanlabh",
        "variants": [
            {
                "title": "Default Title",
                "price": "999.00",
                "compare_at_price": "1888.00",
                "sku": "CRYSTAL-TUMBLE-SET",
                "inventory_management": None,
                "requires_shipping": True
            }
        ]
    }
}

req = urllib.request.Request(
    f"https://{STORE}/admin/api/2024-01/products.json",
    data=json.dumps(product_data).encode("utf-8"),
    headers={
        "X-Shopify-Access-Token": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
        p = data.get("product", {})
        print(f"SUCCESS: Created product '{p.get('title')}' (ID: {p.get('id')}, Handle: {p.get('handle')}) in Shopify Admin!")
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.read().decode()}")
except Exception as e:
    print(f"Error: {e}")

