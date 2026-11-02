import os, shutil, subprocess, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, 'assets')
WIX = os.path.join(ASSETS, 'wix-products')

# Map product handles to clean asset filenames and their Wix media source
# We will inspect wix-store-export.csv to get the exact mapping
with open(os.path.join(ROOT, 'wix-store-export.csv'), mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

dummy_names = ["I'm a product", "Brush Set", "Matte Lipstick", "Face Gloss"]

media_map = {}
current_handle = None
for r in rows:
    handle = r['handle']
    fieldType = r['fieldType']
    if fieldType == 'PRODUCT':
        current_handle = handle
        media_map[current_handle] = []
    elif fieldType == 'MEDIA' and current_handle:
        m = r['media'].strip()
        if m:
            media_map[current_handle].append(m)

real_products = [r for r in rows if r['fieldType'] == 'PRODUCT' and not any(r['name'].strip().startswith(d) for d in dummy_names)]

# Define clean target names for each product
target_assets = {}

for r in real_products:
    name = r['name'].strip()
    handle = r['handle']
    name_l = name.lower()
    imgs = media_map.get(handle, [])
    src_img = imgs[0] if imgs else None

    # Determine clean filename based on name
    if 'aventurine bracelet' in name_l:
        clean_name = 'product-aventurine-bracelet.jpg'
    elif 'rose quartz small angel' in name_l:
        clean_name = 'product-rose-quartz-angel.jpg'
    elif 'kunzite bracelet' in name_l:
        clean_name = 'product-kunzite-bracelet.jpg'
    elif name == 'Rose Quartz':
        clean_name = 'product-rose-quartz.png'
    elif name == 'Seven chakra':
        clean_name = 'product-seven-chakra-bracelet.png'
    elif name == 'Tiger Eye':
        clean_name = 'product-tiger-eye.png'
    elif '10 minutes call' in name_l:
        clean_name = 'product-call-10min.jpg'
    elif '30 minutes call' in name_l:
        clean_name = 'product-call-30min.jpg'
    elif 'voice note- 1 question' in name_l:
        clean_name = 'product-voice-1q.jpg'
    elif 'voice note- 2 questions' in name_l:
        clean_name = 'product-voice-2q.jpg'
    elif 'voice note- 4 questions' in name_l:
        clean_name = 'product-voice-4q.jpg'
    elif 'voice note- 5 questions' in name_l:
        clean_name = 'product-voice-5q.jpg'
    elif 'amethyst and clear quartz mixed bracelet' in name_l:
        clean_name = 'product-amethyst-clear-quartz-bracelet.jpg'
    elif name == 'Carnelian':
        clean_name = 'product-carnelian.jpg'
    elif 'amethyst, clear quartz, and rose quartz' in name_l:
        clean_name = 'product-amethyst-clear-rose-bracelet.jpg'
    elif 'black tourmaline bracelet' in name_l:
        clean_name = 'product-black-tourmaline-bracelet.jpg'
    elif 'rune reading' in name_l:
        clean_name = 'product-rune-reading.jpg'
    elif 'pixu' in name_l:
        clean_name = 'product-pixiu-abundance-bracelet.jpg'
    elif 'pyrite money & success bracelet' in name_l:
        clean_name = 'product-pyrite-money-bracelet.jpg'
    elif name == 'Red Jasper':
        clean_name = 'product-red-jasper.jpg'
    elif 'clear quartz – the master healer' in name_l:
        clean_name = 'product-clear-quartz.jpg'
    elif 'personalised energy circle' in name_l:
        clean_name = 'product-energy-circle.jpg'
    elif name == 'Career + Crystal Bundle':
        clean_name = 'product-career-bundle.jpg'
    elif 'career reading + labradorite' in name_l:
        clean_name = 'product-career-labradorite-bundle.png'
    elif name == 'Lapis Lazuli':
        clean_name = 'product-lapis-lazuli.jpg'
    elif name == 'Amazonite':
        clean_name = 'product-amazonite.jpg'
    elif 'sulemani hakik' in name_l:
        clean_name = 'product-sulemani-hakik.png'
    elif 'citrine' in name_l:
        clean_name = 'product-citrine.png'
    elif 'rose quartz: the stone of universal love' in name_l:
        clean_name = 'product-rose-quartz-love.png'
    elif 'malachite' in name_l:
        clean_name = 'product-malachite.png'
    elif 'smoky quartz' in name_l:
        clean_name = 'product-smoky-quartz.png'
    elif 'pyrite: the golden energy booster' in name_l:
        clean_name = 'product-pyrite-booster.png'
    elif 'unakite' in name_l:
        clean_name = 'product-unakite.png'
    elif 'wulou' in name_l:
        clean_name = 'product-wulou-keychain.jpg'
    elif name == 'Rhodonite':
        clean_name = 'product-rhodonite.png'
    elif handle == 'Product_f86fd72e-a630-4474-95a6-6ee261e390c4':
        clean_name = 'product-rakhi-money-magnet-1.jpg'
    elif handle == 'Product_19de4d91-0ea1-416e-a3b2-38b72e67ef21':
        clean_name = 'product-rakhi-money-magnet-2.jpg'
    elif 'triple protection rakhi' in name_l and 'bhabhi' not in name_l:
        clean_name = 'product-rakhi-triple-protection.jpg'
    elif 'seven chakra rakhi' in name_l:
        clean_name = 'product-rakhi-seven-chakra.jpg'
    elif 'bhai bhabhi rudraksha rakhi' in name_l:
        clean_name = 'product-rakhi-bhai-bhabhi-rudraksha.jpg'
    elif 'bhai bhabhi money magnet rakhi' in name_l:
        clean_name = 'product-rakhi-bhai-bhabhi-money-magnet.jpg'
    elif 'triple protection bhai bhabhi rakhi' in name_l:
        clean_name = 'product-rakhi-bhai-bhabhi-triple-protection.jpg'
    else:
        clean_name = f'product-{handle.lower()}.jpg'

    target_assets[handle] = (clean_name, src_img)

# Now copy and convert each
for handle, (clean_name, src_img) in target_assets.items():
    dest = os.path.join(ASSETS, clean_name)
    if not src_img:
        print(f"Skipping {handle} (No src image yet, target: {clean_name})")
        continue

    src = os.path.join(WIX, src_img)
    if not os.path.exists(src):
        print(f"Source not found on disk: {src}")
        continue

    # Convert or copy
    if src_img.endswith('.avif'):
        subprocess.run(['sips', '-s', 'format', 'jpeg', src, '--out', dest], check=True)
        print(f"Converted AVIF to JPEG: {clean_name}")
    elif src_img.endswith('.jpeg'):
        subprocess.run(['sips', '-s', 'format', 'jpeg', src, '--out', dest], check=True)
        print(f"Normalized JPEG: {clean_name}")
    else:
        shutil.copyfile(src, dest)
        print(f"Copied: {clean_name} ({os.path.getsize(dest):,} bytes)")

print("\nAsset preparation finished!")

