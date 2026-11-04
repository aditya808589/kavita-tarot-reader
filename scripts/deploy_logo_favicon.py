import urllib.request, json, time, base64
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shopify_config import TOKEN, STORE, THEME_ID

ROOT = Path(__file__).resolve().parent.parent

imgs = [
    ('assets/kavita-logo-gold.png', ROOT / 'assets/kavita-logo-gold.png'),
    ('assets/kavita-favicon.png', ROOT / 'assets/kavita-favicon.png'),
    ('assets/kavita-favicon-32x32.png', ROOT / 'assets/kavita-favicon-32x32.png'),
    ('assets/apple-touch-icon.png', ROOT / 'assets/apple-touch-icon.png'),
    ('assets/favicon.ico', ROOT / 'assets/favicon.ico'),
]

layouts = [
    ('layout/parity.liquid', ROOT / 'kavita-dawn/layout/parity.liquid'),
    ('layout/theme.liquid', ROOT / 'kavita-dawn/layout/theme.liquid'),
    ('layout/password.liquid', ROOT / 'kavita-dawn/layout/password.liquid'),
]

print(f"Deploying transparent logo and favicons to live theme {THEME_ID}...")

for key, local_file in layouts:
    with open(local_file, 'r', encoding='utf-8') as f:
        content = f.read()
    payload = json.dumps({'asset': {'key': key, 'value': content}}).encode('utf-8')
    req = urllib.request.Request(
        f'https://{STORE}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
        data=payload,
        headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
        method='PUT'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f'Uploaded: {key}', flush=True)
    except urllib.error.HTTPError as e:
        print(f'ERROR {key}: {e.code} {e.read().decode()}', flush=True)
    time.sleep(0.2)

for asset_key, local_path in imgs:
    with open(local_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    payload = json.dumps({'asset': {'key': asset_key, 'attachment': b64}}).encode('utf-8')
    req = urllib.request.Request(
        f'https://{STORE}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
        data=payload,
        headers={'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
        method='PUT'
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            print(f'Uploaded: {asset_key}', flush=True)
    except urllib.error.HTTPError as e:
        print(f'ERROR {asset_key}: {e.code} {e.read().decode()}', flush=True)
    time.sleep(0.2)

print("Deployment complete!")
