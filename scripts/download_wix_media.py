import csv, os, urllib.request, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, 'wix-store-export.csv')
DEST_DIR = os.path.join(ROOT, 'assets', 'wix-products')
os.makedirs(DEST_DIR, exist_ok=True)

dummy_names = ["I'm a product", "Brush Set", "Matte Lipstick", "Face Gloss"]

with open(CSV_PATH, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

media_to_download = set()
current_is_real = False

for r in rows:
    fieldType = r['fieldType']
    if fieldType == 'PRODUCT':
        name = r['name'].strip()
        current_is_real = not any(name.startswith(d) for d in dummy_names)
    elif fieldType == 'MEDIA' and current_is_real:
        m = r['media'].strip()
        if m:
            media_to_download.add(m)

print(f"Total media files to download: {len(media_to_download)}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

downloaded = 0
failed = 0

for idx, m in enumerate(sorted(media_to_download), 1):
    dest_path = os.path.join(DEST_DIR, m)
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        downloaded += 1
        continue

    url = f"https://static.wixstatic.com/media/{m}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp, open(dest_path, 'wb') as out_f:
            out_f.write(resp.read())
        downloaded += 1
        print(f"[{idx}/{len(media_to_download)}] Downloaded: {m} ({os.path.getsize(dest_path):,} bytes)")
        time.sleep(0.1)
    except Exception as e:
        print(f"[{idx}/{len(media_to_download)}] Failed {m}: {e}")
        failed += 1

print(f"\nCompleted! Downloaded: {downloaded}, Failed: {failed}")

