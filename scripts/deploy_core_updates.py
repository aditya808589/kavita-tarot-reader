import urllib.request, json, time, base64
from pathlib import Path

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID
ROOT = Path(__file__).resolve().parent.parent

text_uploads = [
    ('assets/parity-commerce.js', ROOT / 'kavita-dawn/assets/parity-commerce.js'),
    ('assets/parity-catalog.js', ROOT / 'kavita-dawn/assets/parity-catalog.js'),
    ('assets/parity-cart-render.js', ROOT / 'kavita-dawn/assets/parity-cart-render.js'),
    ('assets/parity-page.js', ROOT / 'kavita-dawn/assets/parity-page.js'),
    ('assets/parity-ui.js', ROOT / 'kavita-dawn/assets/parity-ui.js'),
    ('assets/parity-storefront-refinements.css', ROOT / 'kavita-dawn/assets/parity-storefront-refinements.css'),
    ('assets/parity-category-grid.css', ROOT / 'kavita-dawn/assets/parity-category-grid.css'),
    ('assets/parity-vanikabir.css', ROOT / 'kavita-dawn/assets/parity-vanikabir.css'),
    ('assets/parity-integration.css', ROOT / 'kavita-dawn/assets/parity-integration.css'),
    ('assets/kavita-live-repair.css', ROOT / 'kavita-dawn/assets/kavita-live-repair.css'),
    ('assets/storefront-refinements.css', ROOT / 'kavita-dawn/assets/storefront-refinements.css'),
    ('assets/storefront-cart.js', ROOT / 'assets/storefront-cart.js'),
    ('assets/sales-popup.js', ROOT / 'assets/sales-popup.js'),
    ('layout/parity.liquid', ROOT / 'kavita-dawn/layout/parity.liquid'),
    ('layout/theme.liquid', ROOT / 'kavita-dawn/layout/theme.liquid'),
    ('sections/kavita-rajvira-header.liquid', ROOT / 'kavita-dawn/sections/kavita-rajvira-header.liquid'),
    ('sections/parity-index.liquid', ROOT / 'kavita-dawn/sections/parity-index.liquid'),
    ('sections/parity-collections.liquid', ROOT / 'kavita-dawn/sections/parity-collections.liquid'),
    ('sections/parity-consultations.liquid', ROOT / 'kavita-dawn/sections/parity-consultations.liquid'),
    ('sections/parity-product.liquid', ROOT / 'kavita-dawn/sections/parity-product.liquid'),
    ('sections/parity-about.liquid', ROOT / 'kavita-dawn/sections/parity-about.liquid'),
    ('sections/parity-contact.liquid', ROOT / 'kavita-dawn/sections/parity-contact.liquid'),
    ('sections/parity-faq.liquid', ROOT / 'kavita-dawn/sections/parity-faq.liquid'),
    ('sections/parity-cart.liquid', ROOT / 'kavita-dawn/sections/parity-cart.liquid'),
    ('sections/parity-packages.liquid', ROOT / 'kavita-dawn/sections/parity-packages.liquid'),
]

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
    time.sleep(0.15)

print("\nDeploying banner & product image assets...")
extra_imgs = [
    ('assets/product-healing-oil-love-relationships.jpg', ROOT / 'assets/product-healing-oil-love-relationships.jpg'),
    ('assets/product-healing-oil-money-attraction.jpg', ROOT / 'assets/product-healing-oil-money-attraction.jpg'),
    ('assets/product-healing-oil-study-focus.jpg', ROOT / 'assets/product-healing-oil-study-focus.jpg'),
    ('assets/product-bath-salt-aura-booster.jpg', ROOT / 'assets/product-bath-salt-aura-booster.jpg'),
    ('assets/product-bath-salt-energy-booster.jpg', ROOT / 'assets/product-bath-salt-energy-booster.jpg'),
    ('assets/product-bath-salt-coffee.jpg', ROOT / 'assets/product-bath-salt-coffee.jpg'),
    ('assets/product-bath-salt-health-booster.jpg', ROOT / 'assets/product-bath-salt-health-booster.jpg'),
    ('assets/product-2027-year-ahead-cover.jpg', ROOT / 'assets/product-2027-year-ahead-cover.jpg'),
    ('assets/product-2027-year-ahead-details.jpg', ROOT / 'assets/product-2027-year-ahead-details.jpg'),
    ('assets/banner-desktop-crystal-align-3x1.jpg', ROOT / 'assets/banner-desktop-crystal-align-3x1.jpg'),
    ('assets/banner-mobile-crystal-align-4x5.jpg', ROOT / 'assets/banner-mobile-crystal-align-4x5.jpg'),
    ('assets/banner-desktop-crystal-velvet-3x1.jpg', ROOT / 'assets/banner-desktop-crystal-velvet-3x1.jpg'),
    ('assets/banner-mobile-crystal-velvet-4x5.jpg', ROOT / 'assets/banner-mobile-crystal-velvet-4x5.jpg'),
    ('assets/banner-desktop-crystal-power-3x1.jpg', ROOT / 'assets/banner-desktop-crystal-power-3x1.jpg'),
    ('assets/banner-mobile-crystal-power-4x5.jpg', ROOT / 'assets/banner-mobile-crystal-power-4x5.jpg'),
    ('assets/banner-zodiac-bracelets.jpg', ROOT / 'assets/banner-zodiac-bracelets.jpg'),
    ('assets/product-meditation-tumbles.jpg', ROOT / 'assets/product-meditation-tumbles.jpg'),
    ('assets/product-pyrite-booster.png', ROOT / 'assets/product-pyrite-booster.png'),
    ('assets/product-pyrite-money-bracelet.jpg', ROOT / 'assets/product-pyrite-money-bracelet.jpg'),
    ('assets/product-seven-chakra-bracelet.png', ROOT / 'assets/product-seven-chakra-bracelet.png'),
    ('assets/product-rose-quartz-love.png', ROOT / 'assets/product-rose-quartz-love.png'),
    ('assets/hero-banner-luxury-sanctuary.jpg', ROOT / 'assets/hero-banner-luxury-sanctuary.jpg'),
    ('assets/banner-desktop-readings-3x1.jpg', ROOT / 'assets/banner-desktop-readings-3x1.jpg'),
    ('assets/banner-desktop-crystals-3x1.jpg', ROOT / 'assets/banner-desktop-crystals-3x1.jpg'),
    ('assets/banner-desktop-sanctuary-3x1.jpg', ROOT / 'assets/banner-desktop-sanctuary-3x1.jpg'),
    ('assets/banner-desktop-collection-3x1.jpg', ROOT / 'assets/banner-desktop-collection-3x1.jpg'),
    ('assets/banner-desktop-guidance-3x1.jpg', ROOT / 'assets/banner-desktop-guidance-3x1.jpg'),
    ('assets/banner-mobile-readings-4x5.jpg', ROOT / 'assets/banner-mobile-readings-4x5.jpg'),
    ('assets/banner-mobile-crystals-4x5.jpg', ROOT / 'assets/banner-mobile-crystals-4x5.jpg'),
    ('assets/banner-mobile-sanctuary-4x5.jpg', ROOT / 'assets/banner-mobile-sanctuary-4x5.jpg'),
    ('assets/banner-mobile-readings.jpg', ROOT / 'assets/banner-mobile-readings.jpg'),
    ('assets/banner-1-mobile.jpg', ROOT / 'assets/banner-1-mobile.jpg'),
    ('assets/banner-2-mobile.jpg', ROOT / 'assets/banner-2-mobile.jpg'),
    ('assets/package-no-contact-5card.jpg', ROOT / 'assets/package-no-contact-5card.jpg'),
    ('assets/package-future-spouse.jpg', ROOT / 'assets/package-future-spouse.jpg'),
    ('assets/package-love-marriage-8q.jpg', ROOT / 'assets/package-love-marriage-8q.jpg'),
    ('assets/package-no-contact-4q.jpg', ROOT / 'assets/package-no-contact-4q.jpg'),
    ('assets/package-heart-consultation.jpg', ROOT / 'assets/package-heart-consultation.jpg'),
    ('assets/package-career-growth.jpg', ROOT / 'assets/package-career-growth.jpg'),
    ('assets/package-reunion-reading.jpg', ROOT / 'assets/package-reunion-reading.jpg'),
    ('assets/package-deep-insight-8q.jpg', ROOT / 'assets/package-deep-insight-8q.jpg'),
    ('assets/10-minutes-call.jpg', ROOT / 'assets/10-minutes-call.jpg'),
    ('assets/30-minutes-call.jpg', ROOT / 'assets/30-minutes-call.jpg'),
    ('assets/voice-note-1-question.jpg', ROOT / 'assets/voice-note-1-question.jpg'),
    ('assets/voice-note-2-questions.jpg', ROOT / 'assets/voice-note-2-questions.jpg'),
    ('assets/voice-note-5-questions-angel-guidance.jpg', ROOT / 'assets/voice-note-5-questions-angel-guidance.jpg'),
    ('assets/career-growth-reading.jpg', ROOT / 'assets/career-growth-reading.jpg'),
    ('assets/deep-insight-reading-8-questions.jpg', ROOT / 'assets/deep-insight-reading-8-questions.jpg'),
    ('assets/future-spouse-reading.jpg', ROOT / 'assets/future-spouse-reading.jpg'),
    ('assets/love-marriage-pack-8-questions.jpg', ROOT / 'assets/love-marriage-pack-8-questions.jpg'),
    ('assets/no-contact-situation-5-card-reading.jpg', ROOT / 'assets/no-contact-situation-5-card-reading.jpg'),
    ('assets/no-contact-situation-pack-4-questions.jpg', ROOT / 'assets/no-contact-situation-pack-4-questions.jpg'),
    ('assets/reunion-reading.jpg', ROOT / 'assets/reunion-reading.jpg')
]
for asset_key, local_path in extra_imgs:
    if local_path.exists():
        with open(local_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        payload = json.dumps({
            'asset': {
                'key': asset_key,
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
                print(f'Uploaded: {asset_key}', flush=True)
        except urllib.error.HTTPError as e:
            print(f'ERROR {asset_key}: {e.code} {e.read().decode()}', flush=True)

print("\nCore live deployment successfully completed!")

