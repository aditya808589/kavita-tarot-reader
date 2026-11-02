import urllib.request, json, time

from pathlib import Path; import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from shopify_config import TOKEN, STORE, THEME_ID

uploads = [
    ('assets/parity-storefront-refinements.css', 'kavita-dawn/assets/parity-storefront-refinements.css'),
    ('assets/parity-integration.css', 'kavita-dawn/assets/parity-integration.css'),
    ('assets/parity-ui.js', 'kavita-dawn/assets/parity-ui.js'),
    ('sections/parity-index.liquid', 'kavita-dawn/sections/parity-index.liquid'),
    ('sections/parity-collections.liquid', 'kavita-dawn/sections/parity-collections.liquid'),
    ('sections/parity-consultations.liquid', 'kavita-dawn/sections/parity-consultations.liquid'),
    ('sections/parity-product.liquid', 'kavita-dawn/sections/parity-product.liquid'),
    ('sections/parity-about.liquid', 'kavita-dawn/sections/parity-about.liquid'),
    ('sections/parity-contact.liquid', 'kavita-dawn/sections/parity-contact.liquid'),
    ('sections/parity-faq.liquid', 'kavita-dawn/sections/parity-faq.liquid'),
    ('sections/parity-cart.liquid', 'kavita-dawn/sections/parity-cart.liquid'),
]

for key, local_file in uploads:
    with open(local_file, 'r') as f:
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
        with urllib.request.urlopen(req) as resp:
            print(f'Uploaded: {key}', flush=True)
    except urllib.error.HTTPError as e:
        print(f'ERROR {key}: {e.code} {e.read().decode()}', flush=True)
    time.sleep(0.3)

