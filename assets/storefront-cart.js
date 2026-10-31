/**
 * KAVITA TAROT READER — LUXURY CART DRAWER ENGINE
 * Slide-out sidebar cart with premium octagonal cutout item layouts,
 * free shipping progress meter, live quantity adjustments, and WhatsApp checkout.
 */

var cart = CartEngine.getCart().map(item => ({...item, name: item.name || item.title, title: item.title || item.name}));

function saveCart() {
  CartEngine.setCart(cart);
}

function openCart() {
  const drawer = document.getElementById('cartDrawer');
  const overlay = document.getElementById('cartOverlay');
  if (drawer && overlay) {
    drawer.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    renderCartDrawer();
  } else {
    window.location.href = 'cart.html';
  }
}

function closeCart() {
  const drawer = document.getElementById('cartDrawer');
  const overlay = document.getElementById('cartOverlay');
  if (drawer) drawer.classList.remove('active');
  if (overlay) overlay.classList.remove('active');
  document.body.style.overflow = '';
}

function updateCartUI() {
  CartEngine.updateBadges();
  const totalQty = cart.reduce((sum, item) => sum + (item.qty || 1), 0);
  document.querySelectorAll('#cartCount, #mobileCartCount, #cartCountHeader, .kavita-hdr__badge--cart').forEach(el => {
    el.textContent = totalQty;
  });
  renderCartDrawer();
}

function renderCartDrawer() {
  const list = document.getElementById('cartItemsList');
  if (!list) return;

  const totalQty = cart.reduce((sum, item) => sum + (item.qty || 1), 0);
  const subtotal = cart.reduce((sum, item) => sum + ((item.price || 0) * (item.qty || 1)), 0);

  const countHeader = document.getElementById('cartCountHeader');
  if (countHeader) countHeader.textContent = totalQty;

  const subtotalEl = document.getElementById('cartSubtotal');
  if (subtotalEl) subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');

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
        <a href="collections.html" class="btn btn-maroon" onclick="closeCart()" style="padding: 0.75rem 1.6rem; font-size: 0.85rem; border-radius: 8px;">
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
}

function addToCart(name, price, img, handle) {
  let product = null;
  if (typeof STORE_PRODUCTS !== 'undefined') {
    product = STORE_PRODUCTS.find(p => p.handle === handle || p.title === name || p.img === img);
  }
  
  const title = product ? product.title : name;
  const itemPrice = product ? product.price : (Number(price) || 999);
  const itemImg = product ? product.img : (img || 'assets/banner-1-mobile.jpg');
  const itemId = product ? product.id : Date.now();

  const existing = cart.find(item => item.id === itemId || item.title === title);
  if (existing) {
    existing.qty = (existing.qty || 1) + 1;
  } else {
    cart.push({
      id: itemId,
      name: title,
      title: title,
      price: itemPrice,
      img: itemImg,
      qty: 1
    });
  }

  saveCart();
  updateCartUI();
  openCart(); // Instantly open slide-out cart sidebar!

  const status = document.getElementById('storeStatus');
  if (status) {
    status.textContent = title + ' added to your sacred cart.';
    status.hidden = false;
    clearTimeout(window.storeStatusTimer);
    window.storeStatusTimer = setTimeout(() => status.hidden = true, 3500);
  }
}

function removeFromCart(index) {
  if (cart[index]) {
    cart.splice(index, 1);
    saveCart();
    updateCartUI();
  }
}

function changeQty(index, delta) {
  if (!cart[index]) return;
  cart[index].qty = (cart[index].qty || 1) + delta;
  if (cart[index].qty <= 0) {
    cart.splice(index, 1);
  }
  saveCart();
  updateCartUI();
}

function checkoutCart() {
  alert('This is a storefront preview. Secure Shopify checkout with Cash on Delivery (COD) will be processed when connected to Shopify Admin. You can also place this order directly via WhatsApp!');
}

function whatsappCheckout() {
  if (cart.length === 0) {
    alert('Your cart is empty. Please add items before checking out.');
    return;
  }

  const subtotal = cart.reduce((sum, item) => sum + ((item.price || 0) * (item.qty || 1)), 0);
  let msg = `*NEW ORDER FROM KAVITA TAROT WEBSITE*%0A%0A`;
  cart.forEach((item, i) => {
    msg += `${i + 1}. *${item.title || item.name}* (Qty: ${item.qty || 1}) — ₹${((item.price || 0) * (item.qty || 1)).toLocaleString('en-IN')}%0A`;
  });
  msg += `%0A*Total Amount:* ₹${subtotal.toLocaleString('en-IN')}%0A`;
  msg += `*Consecration Request:* Please energize with Vedic Beeja Mantras before shipping.%0A%0APlease confirm my order & provide delivery details!`;

  window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
}

function playSacredChime() {
  /* Silent or optional tone */
}

// Bind Header & Mobile Cart triggers
document.addEventListener('DOMContentLoaded', () => {
  updateCartUI();

  // Any button with cart opener
  document.querySelectorAll('#openCartBtn, .kavita-hdr__icon-btn--cart, a[href="cart.html"], .mobile-nav-cart').forEach(btn => {
    // Only intercept if we have the drawer on this page
    if (document.getElementById('cartDrawer')) {
      btn.addEventListener('click', (e) => {
        // If clicking on header/nav cart icon, open drawer instead of redirecting
        if (!btn.classList.contains('allow-page-nav')) {
          e.preventDefault();
          openCart();
        }
      });
    }
  });

  // Close on overlay or Escape
  document.getElementById('cartOverlay')?.addEventListener('click', closeCart);
});
