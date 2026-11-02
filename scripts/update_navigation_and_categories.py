import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = ['about.html', 'cart.html', 'collections.html', 'consultations.html', 'contact.html', 'faq.html', 'index.html', 'product.html']

old_nav_pattern = r'<ul class="kavita-hdr__menu">.*?</ul>'
new_nav = '''<ul class="kavita-hdr__menu">
          <li class="kavita-hdr__menu-item"><a href="collections.html" class="kavita-hdr__menu-link">All Collections</a></li>
          <li class="kavita-hdr__menu-item"><a href="consultations.html" class="kavita-hdr__menu-link">Tarot Readings</a></li>
          <li class="kavita-hdr__menu-item"><a href="collections.html?cat=bracelets" class="kavita-hdr__menu-link">Healing Bracelets</a></li>
          <li class="kavita-hdr__menu-item"><a href="collections.html?cat=crystals" class="kavita-hdr__menu-link">Crystals &amp; Carvings</a></li>
          <li class="kavita-hdr__menu-item"><a href="collections.html?cat=rakhis" class="kavita-hdr__menu-link">Sacred Rakhis</a></li>
          <li class="kavita-hdr__menu-item"><a href="about.html" class="kavita-hdr__menu-link">About Kavita</a></li>
          <li class="kavita-hdr__menu-item"><a href="contact.html" class="kavita-hdr__menu-link">Contact</a></li>
        </ul>'''

for fname in HTML_FILES:
    fpath = os.path.join(ROOT, fname)
    if not os.path.exists(fpath):
        continue
    content = open(fpath, 'r', encoding='utf-8').read()
    if re.search(old_nav_pattern, content, re.DOTALL):
        updated = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated navigation bar in: {fname}")

# Now update category circles row in index.html
index_path = os.path.join(ROOT, 'index.html')
index_content = open(index_path, 'r', encoding='utf-8').read()

old_circle_row_pattern = r'<div class="categories-circle-row">.*?</div>\s*</div>\s*</section>'
new_circle_row = '''<div class="categories-circle-row">
        <!-- 1. Live Audio Calls -->
        <a href="consultations.html" class="cat-circle-card">
          <div class="cat-circle-avatar-wrap">
            <img loading="lazy" decoding="async" class="cat-circle-img" src="assets/product-call-10min.jpg" alt="Live Audio Consultations">
          </div>
          <div class="cat-circle-name">Live Audio Calls</div>
        </a>

        <!-- 2. WhatsApp Voice Notes -->
        <a href="consultations.html" class="cat-circle-card">
          <div class="cat-circle-avatar-wrap">
            <img loading="lazy" decoding="async" class="cat-circle-img" src="assets/product-voice-2q.jpg" alt="Voice Note Readings">
          </div>
          <div class="cat-circle-name">Voice Notes</div>
        </a>

        <!-- 3. Sacred Energy Circles -->
        <a href="product.html?id=8" class="cat-circle-card">
          <div class="cat-circle-avatar-wrap">
            <img loading="lazy" decoding="async" class="cat-circle-img" src="assets/product-energy-circle.jpg" alt="Personalised Energy Circles">
          </div>
          <div class="cat-circle-name">Energy Circles</div>
        </a>

        <!-- 4. Healing Gemstone Bracelets -->
        <a href="collections.html?cat=bracelets" class="cat-circle-card">
          <div class="cat-circle-avatar-wrap">
            <img loading="lazy" decoding="async" class="cat-circle-img" src="assets/product-seven-chakra-bracelet.png" alt="Healing Gemstone Bracelets">
          </div>
          <div class="cat-circle-name">Healing Bracelets</div>
        </a>

        <!-- 5. Healing Crystals & Carvings -->
        <a href="collections.html?cat=crystals" class="cat-circle-card">
          <div class="cat-circle-avatar-wrap">
            <img loading="lazy" decoding="async" class="cat-circle-img" src="assets/product-citrine.png" alt="Healing Crystals">
          </div>
          <div class="cat-circle-name">Healing Crystals</div>
        </a>

        <!-- 6. Sacred Charged Rakhis -->
        <a href="collections.html?cat=rakhis" class="cat-circle-card">
          <div class="cat-circle-avatar-wrap">
            <img loading="lazy" decoding="async" class="cat-circle-img" src="assets/product-rakhi-money-magnet-1.jpg" alt="Sacred Charged Rakhis">
          </div>
          <div class="cat-circle-name">Sacred Rakhis</div>
        </a>
      </div>
    </div>
  </section>'''

if re.search(old_circle_row_pattern, index_content, re.DOTALL):
    index_content = re.sub(old_circle_row_pattern, new_circle_row, index_content, flags=re.DOTALL)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Updated categories-circle-row in index.html")

print("All navigation and category circles updated successfully!")

