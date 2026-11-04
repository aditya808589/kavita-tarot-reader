import json, urllib.request, base64, time
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shopify_config import TOKEN, STORE

ROOT = Path(__file__).resolve().parent.parent

PRODUCTS_DATA = [
    {
        "title": "Love & Relationships Healing Oil (With Energized Crystals)",
        "handle": "love-relationships-healing-oil-with-energized-crystals",
        "price": "777.00",
        "compare_at_price": "1299.00",
        "img_path": ROOT / "assets/product-healing-oil-love-relationships.jpg",
        "product_type": "Healing Oil",
        "tags": "Healing Oil, Rose Quartz, Love, Relationships, Consecrated, Roll-on, Self-Love",
        "body_html": """
<p><strong>Open your heart chakra to deep unconditional love, emotional harmony, and soulmate magnetism with the Love & Relationships Healing Oil.</strong></p>
<p>Formulated with sacred pure essential oils and infused with genuine, Vedic-energized Rose Quartz crystal chips right inside the roll-on bottle. Apply on pulse points (wrists, behind ears, neck, and heart space) to awaken romantic attraction, soothe relationship misunderstandings, and deepen self-love.</p>
<h4>✦ Key Focus Areas:</h4>
<ul>
  <li>❤️ Unconditional Love & Emotional Healing</li>
  <li>🌸 Self-Love, Self-Worth & Inner Peace</li>
  <li>🕊️ Harmonious Heart-to-Heart Communication</li>
  <li>✨ Soul Connection & Relationship Restoration</li>
</ul>
<p><strong>Package:</strong> 10ml Roll-on glass bottle with gold cap & display box.</p>
<p><strong>How to Use:</strong> Roll gently onto wrists, neck, or collarbone before sleep, meditation, or dates while setting your loving intention.</p>
"""
    },
    {
        "title": "Money Attraction Healing Oil (With Energized Crystals)",
        "handle": "money-attraction-healing-oil-with-energized-crystals",
        "price": "777.00",
        "compare_at_price": "1299.00",
        "img_path": ROOT / "assets/product-healing-oil-money-attraction.jpg",
        "product_type": "Healing Oil",
        "tags": "Healing Oil, Money Attraction, Pyrite, Citrine, Wealth, Abundance, Consecrated, Roll-on",
        "body_html": """
<p><strong>Magnetize financial windfalls, career promotions, and steady business prosperity with the Money Attraction Healing Oil.</strong></p>
<p>Charged during auspicious planetary hours and enriched with authentic Pyrite and Citrine crystal chips, this sacred consecrated oil dissolves scarcity fears and aligns your personal aura with unstoppable abundance.</p>
<h4>✦ Key Focus Areas:</h4>
<ul>
  <li>💰 Wealth & Golden Abundance</li>
  <li>🚀 Business Growth & Unexpected Financial Opportunities</li>
  <li>💼 Career Confidence & Victory in Negotiations</li>
  <li>🪙 Financial Stability & Mindset Cleansing</li>
</ul>
<p><strong>Package:</strong> 10ml Roll-on glass bottle with gold cap & display box.</p>
<p><strong>How to Use:</strong> Anoint your wrists, palm centers, wallet, financial documents, or cash box before important meetings, client calls, or trading sessions.</p>
"""
    },
    {
        "title": "Study & Concentration Healing Oil (With Energized Crystals)",
        "handle": "study-concentration-healing-oil-with-energized-crystals",
        "price": "777.00",
        "compare_at_price": "1299.00",
        "img_path": ROOT / "assets/product-healing-oil-study-focus.jpg",
        "product_type": "Healing Oil",
        "tags": "Healing Oil, Study, Memory, Concentration, Focus, Sodalite, Consecrated, Roll-on",
        "body_html": """
<p><strong>Awaken sharp mental clarity, effortless memory recall, and deep laser focus with the Study Healing Oil.</strong></p>
<p>Specially formulated for students, competitive exam aspirants, and professionals requiring peak cognitive performance. Infused with consecrated Third Eye crystal chips (Sodalite & Quartz), this aromatherapeutic blend clears mental fatigue and locks in concentration.</p>
<h4>✦ Key Focus Areas:</h4>
<ul>
  <li>📚 Laser Focus & Deep Study Retention</li>
  <li>🧠 Exam Anxiety Relief & Mental Calm</li>
  <li>💡 Quick Memory Recall & Clear Analytical Thinking</li>
  <li>⚡ Distraction Elimination & Brain Stamina</li>
</ul>
<p><strong>Package:</strong> 10ml Roll-on glass bottle with gold cap & display box.</p>
<p><strong>How to Use:</strong> Roll on temples, back of neck, and wrists 5 minutes before studying, reading, or exams.</p>
"""
    },
    {
        "title": "Aura Booster Sacred Bath Salt (Aura Cleansing & Energy Shield)",
        "handle": "aura-booster-sacred-bath-salt",
        "price": "555.00",
        "compare_at_price": "899.00",
        "img_path": ROOT / "assets/product-bath-salt-aura-booster.jpg",
        "product_type": "Spiritual Bath Salt",
        "tags": "Bath Salt, Aura Booster, Cleansing, Protection, Stress Relief, Relaxation, Consecrated",
        "body_html": """
<p><strong>Strip away psychic smog, negative vibrations, and emotional exhaustion with the Aura Booster Sacred Bath Salt.</strong></p>
<p>Your aura absorbs dense energy from daily environments, crowded spaces, and negative interactions. This consecrated ritual salt bath revitalizes your electromagnetic field, leaving you spiritually renewed, deeply relaxed, and energetically shielded.</p>
<h4>✦ Key Benefits:</h4>
<ul>
  <li>🧿 Immediate Psychic Fatigue & Nazar Cleansing</li>
  <li>🕊️ Deep Muscle Relaxation & Stress Relief</li>
  <li>✨ Recharges Depleted Vitality & Body Aura</li>
</ul>
<p><strong>Net Weight:</strong> 200g Resealable Moisture-Lock Pouch.</p>
<p><strong>How to Use:</strong> Add 2-3 tablespoons into warm bath water or a foot soak tub. Soak for 15-20 minutes while visualizing all fatigue dissolving into the water.</p>
"""
    },
    {
        "title": "Energy Booster Sacred Bath Salt (Vitality & Fatigue Relief)",
        "handle": "energy-booster-sacred-bath-salt",
        "price": "555.00",
        "compare_at_price": "899.00",
        "img_path": ROOT / "assets/product-bath-salt-energy-booster.jpg",
        "product_type": "Spiritual Bath Salt",
        "tags": "Bath Salt, Energy Booster, Vitality, Stamina, Stress Relief, Relaxation, Consecrated",
        "body_html": """
<p><strong>Recharge your physical vitality and banish chronic tiredness with the Energy Booster Sacred Bath Salt.</strong></p>
<p>Blended with invigorating mineral salts and consecrated herbal extracts, this soak awakens sluggish chakras, boosts inner motivation, and restores the active fiery drive needed to conquer your goals.</p>
<h4>✦ Key Benefits:</h4>
<ul>
  <li>🔥 Overcomes Lethargy & Chronic Sluggishness</li>
  <li>⚡ Enhances Natural Physical Stamina & Morning Drive</li>
  <li>🌿 Cellular Mineral Rejuvenation & Nervous System Reset</li>
</ul>
<p><strong>Net Weight:</strong> 200g Resealable Moisture-Lock Pouch.</p>
<p><strong>How to Use:</strong> Dissolve 2-3 spoonfuls in a warm bath or morning foot soak to energize your entire body.</p>
"""
    },
    {
        "title": "Coffee Detox Sacred Bath Salt (Aromatherapeutic Scrub & Soak)",
        "handle": "coffee-detox-sacred-bath-salt",
        "price": "555.00",
        "compare_at_price": "899.00",
        "img_path": ROOT / "assets/product-bath-salt-coffee.jpg",
        "product_type": "Spiritual Bath Salt",
        "tags": "Bath Salt, Coffee, Detox, Exfoliating, Relaxation, Consecrated, Skin Care",
        "body_html": """
<p><strong>Indulge your senses with the Coffee Detox Sacred Bath Salt — a rich aromatherapeutic blend of real coffee grounds and unrefined mineral crystal salts.</strong></p>
<p>Rich in antioxidants and natural caffeine, this stimulating soak detoxifies stagnant fluid buildup, smooths skin texture, and awakens the senses with an irresistible warm roasted coffee aroma.</p>
<h4>✦ Key Benefits:</h4>
<ul>
  <li>☕ Lymphatic Detox & Stagnant Energy Drainage</li>
  <li>✨ Skin Smoothing & Exfoliating Rejuvenation</li>
  <li>🌟 Instant Mental Alertness & Mood Elevation</li>
</ul>
<p><strong>Net Weight:</strong> 200g Resealable Moisture-Lock Pouch.</p>
<p><strong>How to Use:</strong> Add to a warm bath or use as a gentle wet body polish in the shower before rinsing.</p>
"""
    },
    {
        "title": "Health Booster Sacred Bath Salt (Immunity & Recovery Soak)",
        "handle": "health-booster-sacred-bath-salt",
        "price": "555.00",
        "compare_at_price": "899.00",
        "img_path": ROOT / "assets/product-bath-salt-health-booster.jpg",
        "product_type": "Spiritual Bath Salt",
        "tags": "Bath Salt, Health Booster, Immunity, Recovery, Relaxation, Consecrated, Sleep",
        "body_html": """
<p><strong>Restore physical balance and support holistic wellness with the Health Booster Sacred Bath Salt.</strong></p>
<p>Formulated with restorative mineral salts and consecrated healing herbal infusions, this therapeutic soak draws out bodily inflammation, relaxes tight muscles, and creates the ideal energetic container for cellular repair and peaceful sleep.</p>
<h4>✦ Key Benefits:</h4>
<ul>
  <li>🌿 Soothes Muscular Aches & Joint Stiffness</li>
  <li>🌙 Promotes Deep Restorative REM Sleep</li>
  <li>🛡️ Immune System Support & Energetic Grounding</li>
</ul>
<p><strong>Net Weight:</strong> 200g Resealable Moisture-Lock Pouch.</p>
<p><strong>How to Use:</strong> Soak in a warm tub or foot bath for 20 minutes before bedtime.</p>
"""
    }
]

created_results = []

for item in PRODUCTS_DATA:
    with open(item["img_path"], "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "product": {
            "title": item["title"],
            "handle": item["handle"],
            "body_html": item["body_html"],
            "vendor": "Kavita Tarot Reader",
            "product_type": item["product_type"],
            "status": "active",
            "tags": item["tags"],
            "variants": [
                {
                    "price": item["price"],
                    "compare_at_price": item["compare_at_price"],
                    "sku": item["handle"],
                    "inventory_management": None,
                    "requires_shipping": True
                }
            ],
            "images": [
                {
                    "attachment": img_b64,
                    "filename": item["img_path"].name
                }
            ]
        }
    }

    url = f"https://{STORE}/admin/api/2024-01/products.json"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "X-Shopify-Access-Token": TOKEN,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            prod = data.get("product", {})
            pid = prod.get("id")
            vid = prod.get("variants", [{}])[0].get("id")
            handle = prod.get("handle")
            created_results.append({
                "title": item["title"],
                "handle": handle,
                "productId": pid,
                "variantId": vid,
                "price": float(item["price"]),
                "comparePrice": float(item["compare_at_price"])
            })
            print(f"SUCCESS: Created {item['title']} -> ID: {pid}, Variant: {vid}, Handle: {handle}", flush=True)
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"ERROR creating {item['title']}: {e.code} - {err}", flush=True)
    time.sleep(0.5)

print("\n--- Summary of Created Products ---")
print(json.dumps(created_results, indent=2))

with open(ROOT / "scripts/created_new_products.json", "w") as out:
    json.dump(created_results, out, indent=2)

