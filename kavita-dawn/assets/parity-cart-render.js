function renderCartDrawer() {
  const list = document.getElementById('cartItemsList');
  if (!list) return;

  const totalQty = cart.reduce((sum, item) => sum + (item.qty || 1), 0);
  const subtotal = cart.reduce((sum, item) => sum + ((item.price || 0) * (item.qty || 1)), 0);

  const discountData = JSON.parse(sessionStorage.getItem('kavita_discount') || 'null');
  let discountAmount = 0;
  if (discountData && discountData.percent && subtotal > 0) {
    discountAmount = Math.round(subtotal * (discountData.percent / 100));
  }
  const finalTotal = subtotal - discountAmount;

  const countHeader = document.getElementById('cartCountHeader');
  if (countHeader) countHeader.textContent = totalQty;

  const subtotalEl = document.getElementById('cartSubtotal');
  if (subtotalEl) {
    if (discountAmount > 0) {
      subtotalEl.innerHTML = `
        <div style="font-size: 0.82rem; color: #888; text-decoration: line-through;">₹${subtotal.toLocaleString('en-IN')}</div>
        <div style="font-size: 0.78rem; color: #2E7D32; font-weight: 700; margin: 2px 0;">10% Welcome Gift (-₹${discountAmount.toLocaleString('en-IN')})</div>
        <div style="font-size: 1.25rem; color: #80142B; font-weight: 800;">₹${finalTotal.toLocaleString('en-IN')}</div>
      `;
    } else {
      subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');
    }
  }

  // Shipping Progress Bar (Threshold ₹999)
  const freeThreshold = 999;
  const progressFill = document.getElementById('shippingProgressFill');
  const progressText = document.getElementById('shippingProgressText');

  if (progressFill && progressText) {
    if (subtotal >= freeThreshold) {
      progressFill.style.width = '100%';
      progressFill.style.background = 'linear-gradient(90deg, #d4af37, #f3e5ab)';
      progressText.innerHTML = '🎉 <b>UNLOCKED!</b> Free Express Shipping & Consecrated Gift Included!';
    } else {
      const remaining = freeThreshold - subtotal;
      const pct = Math.min(100, Math.round((subtotal / freeThreshold) * 100));
      progressFill.style.width = pct + '%';
      progressFill.style.background = 'linear-gradient(90deg, #80142b, #d4af37)';
      progressText.innerHTML = `✦ Add <b>₹${remaining.toLocaleString('en-IN')}</b> for FREE Express Delivery & Vedic Gift!`;
    }
  }

  // Empty State
  if (cart.length === 0) {
    list.innerHTML = `
      <div class="cart-empty-state">
        <div class="cart-empty-icon">🪷</div>
        <h4 style="font-family: var(--font-heading, serif); font-size: 1.25rem; color: #2d1820; margin-bottom: 0.4rem;">Your Sacred Cart is Empty</h4>
        <p style="font-size: 0.88rem; color: #7a6a6f; line-height: 1.6; max-width: 260px; margin: 0 auto 1.5rem;">
          Explore our consecrated tarot decks, natural healing crystals, and live audio consultations.
        </p>
        <a href="/collections/all" class="btn btn-maroon" onclick="closeCart()" style="padding: 0.75rem 1.6rem; font-size: 0.85rem; border-radius: 8px;">
          ✦ Explore Collections
        </a>
      </div>
    `;
    return;
  }

  // Distinctive Cutout Cart Layout
  list.innerHTML = cart.map((item, index) => `
    <div class="cart-item-cutout" data-index="${index}">
      <div class="cart-item-thumb-box">
        <img src="${item.img || 'assets/banner-1-mobile.jpg'}" alt="${item.title || item.name}" class="cart-item-thumb">
      </div>
      <div class="cart-item-details">
        <div class="cart-item-tag">✦ Consecrated & Energized</div>
        <h4 class="cart-item-title">${item.title || item.name}</h4>
        <div class="cart-item-price">₹${(item.price || 0).toLocaleString('en-IN')}</div>
        <div class="cart-item-bottom-row">
          <div class="cart-qty-pill">
            <button type="button" class="cart-qty-btn" onclick="changeQty(${index}, -1)" aria-label="Decrease quantity">−</button>
            <span class="cart-qty-num">${item.qty || 1}</span>
            <button type="button" class="cart-qty-btn" onclick="changeQty(${index}, 1)" aria-label="Increase quantity">+</button>
          </div>
          <button type="button" class="cart-item-remove-btn" onclick="removeFromCart(${index})" title="Remove item" aria-label="Remove item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            Remove
          </button>
        </div>
      </div>
    </div>
  `).join('');

  // "These Are Bought Together" Complementary Add-ons in Cart Drawer
  function resolveCartAssetImg(imgPath, handle) {
    if (typeof window !== 'undefined' && window.KAVITA_LIVE_PRODUCTS && handle && window.KAVITA_LIVE_PRODUCTS[handle]) {
      const lp = window.KAVITA_LIVE_PRODUCTS[handle];
      if (lp.featured_image) return lp.featured_image;
      if (lp.images && lp.images.length > 0) return lp.images[0];
    }
    if (typeof STORE_PRODUCTS !== 'undefined' && handle) {
      const sp = STORE_PRODUCTS.find(p => p.handle === handle);
      if (sp && sp.img && (sp.img.startsWith('http') || sp.img.startsWith('//'))) return sp.img;
    }
    if (imgPath && (imgPath.startsWith('http://') || imgPath.startsWith('https://') || imgPath.startsWith('//'))) {
      return imgPath;
    }
    if (typeof window !== 'undefined' && window.KAVITA_ASSET_BASE && imgPath) {
      const filename = imgPath.split('/').pop();
      return window.KAVITA_ASSET_BASE + filename;
    }
    return imgPath;
  }

  const upsellCandidates = [
    { handle: 'meditation-crystal-tumbles', name: 'Meditation Crystal Tumbles (Set of 7)', price: 599, compare: 999, img: 'assets/product-meditation-tumbles.jpg' },
    { handle: 'pyrite-golden-energy-booster', name: 'Natural Golden Pyrite Wealth Cluster', price: 899, compare: 1499, img: 'assets/product-pyrite-booster.png' },
    { handle: 'pyrite-money-success-bracelet', name: 'Pyrite Money Magnet Healing Bracelet', price: 799, compare: 1299, img: 'assets/product-pyrite-money-bracelet.jpg' },
    { handle: 'seven-chakra-bracelet', name: '7 Chakra Healing & Harmony Bracelet', price: 699, compare: 1199, img: 'assets/product-seven-chakra-bracelet.png' },
    { handle: 'rose-quartz-raw', name: 'Raw Rose Quartz Unconditional Love Stone', price: 799, compare: 1199, img: 'assets/product-rose-quartz-love.png' }
  ];

  const cartHandles = cart.map(i => (i.handle || i.name || i.title || '').toLowerCase());
  const eligibleUpsells = upsellCandidates.filter(u => !cartHandles.some(ch => ch.includes(u.handle.toLowerCase()) || ch.includes(u.name.toLowerCase()))).slice(0, 2);

  if (eligibleUpsells.length > 0) {
    const upsellHTML = `
      <div class="cart-bought-together-wrap" style="margin-top: 1.25rem; background: #FFFDF9; border: 1.5px dashed #D4AF37; border-radius: 12px; padding: 0.9rem; box-shadow: 0 4px 12px rgba(128, 20, 43, 0.04);">
        <div style="font-size: 0.76rem; font-weight: 700; color: #80142B; text-transform: uppercase; letter-spacing: 0.08em; display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.65rem;">
          <span>✦ These Are Bought Together</span>
          <span style="font-size: 0.68rem; background: #FFF3D6; color: #80142B; padding: 2px 6px; border-radius: 4px; font-weight: 700;">Recommended</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 0.65rem;">
          ${eligibleUpsells.map(u => {
            const uImg = resolveCartAssetImg(u.img, u.handle);
            return `
            <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; background: #FFFFFF; border: 1px solid #EEDFCA; border-radius: 8px; padding: 0.5rem 0.65rem;">
              <img src="${uImg}" alt="${u.name}" style="width: 44px; height: 44px; object-fit: cover; border-radius: 6px; flex-shrink: 0; border: 1px solid #EFE6D8;" onerror="this.onerror=null; this.src=(window.KAVITA_ASSET_BASE ? window.KAVITA_ASSET_BASE + 'kavita-logo-gold.png' : 'assets/kavita-logo-gold.png');">
              <div style="flex: 1; min-width: 0;">
                <div style="font-size: 0.8rem; font-weight: 600; color: #2A1D1A; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${u.name}</div>
                <div style="font-size: 0.78rem; font-weight: 700; color: #80142B;">₹${u.price.toLocaleString('en-IN')} <span style="font-size: 0.7rem; color: #888; text-decoration: line-through; font-weight: 400;">₹${u.compare.toLocaleString('en-IN')}</span></div>
              </div>
              <button type="button" onclick="addToCart('${u.name}', ${u.price}, '${uImg}', '${u.handle}')" class="btn btn-maroon" style="padding: 0.35rem 0.7rem; font-size: 0.75rem; border-radius: 6px; white-space: nowrap; flex-shrink: 0; cursor: pointer; border: none;">
                + Add
              </button>
            </div>
            `;
          }).join('')}
        </div>
      </div>
    `;
    list.insertAdjacentHTML('beforeend', upsellHTML);
  }

  const hasReading = cart.some(item => {
    const t = (item.title || item.name || '').toLowerCase();
    return t.includes('reading') || t.includes('call') || t.includes('voice note') || t.includes('session') || t.includes('circle') || t.includes('cord-cutting') || t.includes('bundle');
  });

  document.querySelectorAll('.checkout-cod-label, #checkoutBtnText').forEach(btn => {
    if (hasReading) {
      btn.textContent = '✦ Proceed to Secure Prepaid Checkout';
    } else {
      btn.textContent = '✦ Proceed to Secure Checkout';
    }
  });

  const readingNotice = document.getElementById('cartReadingNotice');
  if (readingNotice) {
    readingNotice.style.display = hasReading ? 'block' : 'none';
  }
}

