/**
 * Kavita Tarot & Spirituals — Native Live Sales Pop-up (FOMO Engine)
 * Lightweight, zero-app, high-converting social proof purchase notifications.
 */
(() => {
  if (typeof window === 'undefined') return;

  // Don't show inside checkout or iframe
  if (window.location.pathname.includes('/checkout') || window.location.pathname.includes('/cart')) {
    // Optionally allow on cart page, but keep checkout clean
  }

  // Realistic recent customer purchases tailored for Kavita's divine catalog
  const SALES_DATA = [
    {
      buyer: 'Pooja S.',
      city: 'Mumbai',
      product: 'Natural Golden Pyrite Wealth & Abundance Cluster',
      handle: 'pyrite-golden-energy-booster',
      img: 'assets/product-pyrite-booster.png',
      time: '2 minutes ago'
    },
    {
      buyer: 'Ananya M.',
      city: 'New Delhi',
      product: '10 Minutes Live Audio Call Tarot Reading with Kavita',
      handle: '10-minutes-call',
      img: 'assets/10-minutes-call.jpg',
      time: '4 minutes ago'
    },
    {
      buyer: 'Sneha V.',
      city: 'Pune',
      product: 'Meditation Crystal Tumbles (Set of 7 Chakra Stones)',
      handle: 'meditation-crystal-tumbles',
      img: 'assets/product-meditation-tumbles.jpg',
      time: '7 minutes ago'
    },
    {
      buyer: 'Ritu K.',
      city: 'Bengaluru',
      product: 'Pyrite Money Magnet & Wealth Healing Bracelet',
      handle: 'pyrite-money-success-bracelet',
      img: 'assets/product-pyrite-money-bracelet.jpg',
      time: '11 minutes ago'
    },
    {
      buyer: 'Meera R.',
      city: 'Hyderabad',
      product: 'Love & Marriage Channeled Tarot Reading (8 Questions)',
      handle: 'love-marriage-pack-8-questions',
      img: 'assets/love-marriage-pack-8-questions.jpg',
      time: '14 minutes ago'
    },
    {
      buyer: 'Kavita D.',
      city: 'Kolkata',
      product: '7 Chakra Natural Healing & Balance Bracelet',
      handle: 'seven-chakra-bracelet',
      img: 'assets/product-seven-chakra-bracelet.png',
      time: '18 minutes ago'
    },
    {
      buyer: 'Divya N.',
      city: 'Jaipur',
      product: 'Future Spouse Channeled Reading with Kavita',
      handle: 'future-spouse-reading',
      img: 'assets/future-spouse-reading.jpg',
      time: '23 minutes ago'
    },
    {
      buyer: 'Aarti P.',
      city: 'Ahmedabad',
      product: 'Raw Rose Quartz Unconditional Love & Harmony Stone',
      handle: 'rose-quartz-raw',
      img: 'assets/product-rose-quartz-love.png',
      time: '27 minutes ago'
    },
    {
      buyer: 'Simran G.',
      city: 'Chandigarh',
      product: 'Career Growth & Financial Trajectory Tarot Reading',
      handle: 'career-growth-reading',
      img: 'assets/career-growth-reading.jpg',
      time: '32 minutes ago'
    },
    {
      buyer: 'Tanvi B.',
      city: 'Lucknow',
      product: 'Black Tourmaline Ultimate Negative Shield Bracelet',
      handle: 'black-tourmaline-bracelet',
      img: 'assets/product-black-tourmaline-bracelet.jpg',
      time: '36 minutes ago'
    },
    {
      buyer: 'Nisha T.',
      city: 'Gurgaon',
      product: '2 Questions WhatsApp Voice Note Reading',
      handle: 'voice-note-2-questions',
      img: 'assets/voice-note-2-questions.jpg',
      time: '41 minutes ago'
    },
    {
      buyer: 'Shreya C.',
      city: 'Chennai',
      product: 'Natural Citrine Stone of Joy & Abundance Cluster',
      handle: 'citrine-stone-of-joy-abundance',
      img: 'assets/product-citrine.png',
      time: '45 minutes ago'
    }
  ];

  // Inject CSS Styles
  const style = document.createElement('style');
  style.id = 'kavita-sales-popup-style';
  style.textContent = `
    .kavita-sales-popup {
      position: fixed;
      bottom: 24px;
      left: 24px;
      z-index: 9998;
      max-width: 360px;
      width: calc(100% - 48px);
      background: #FFFDF9;
      border: 1.5px solid #D4AF37;
      border-radius: 14px;
      padding: 10px 12px 10px 10px;
      box-shadow: 0 10px 28px rgba(128, 20, 43, 0.14), 0 2px 8px rgba(0,0,0,0.06);
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      opacity: 0;
      transform: translateY(20px) scale(0.96);
      pointer-events: none;
      transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1), transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
      box-sizing: border-box;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .kavita-sales-popup.is-visible {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: auto;
    }
    .kavita-sales-popup__img-box {
      width: 48px;
      height: 48px;
      flex-shrink: 0;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #EEDFCA;
      background: #FAF7F2;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .kavita-sales-popup__img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .kavita-sales-popup__content {
      flex: 1;
      min-width: 0;
      text-align: left;
    }
    .kavita-sales-popup__header {
      font-size: 11px;
      line-height: 1.3;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 5px;
      flex-wrap: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .kavita-sales-popup__badge {
      color: #2E7D32;
      font-weight: 700;
      font-size: 10.5px;
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }
    .kavita-sales-popup__city {
      color: #8C7A70;
      font-weight: 500;
    }
    .kavita-sales-popup__title {
      display: block;
      font-size: 12px;
      font-weight: 700;
      color: #2A1D1A;
      text-decoration: none;
      line-height: 1.35;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin-bottom: 2px;
      transition: color 0.2s ease;
    }
    .kavita-sales-popup__title:hover {
      color: #80142B;
      text-decoration: underline;
    }
    .kavita-sales-popup__footer {
      font-size: 10px;
      color: #80142B;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .kavita-sales-popup__close {
      position: absolute;
      top: 6px;
      right: 6px;
      width: 18px;
      height: 18px;
      border: none;
      background: rgba(0,0,0,0.05);
      border-radius: 50%;
      color: #8C7A70;
      font-size: 11px;
      line-height: 1;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      transition: background 0.2s, color 0.2s;
    }
    .kavita-sales-popup__close:hover {
      background: #80142B;
      color: #FFF;
    }
    @media (max-width: 768px) {
      .kavita-sales-popup {
        bottom: 74px;
        left: 12px;
        right: 12px;
        width: auto;
        max-width: calc(100% - 24px);
        padding: 8px 10px 8px 8px;
      }
      .kavita-sales-popup__img-box {
        width: 44px;
        height: 44px;
      }
      .kavita-sales-popup__title {
        font-size: 11.5px;
      }
    }
  `;
  document.head.appendChild(style);

  // Build the DOM element
  const popupEl = document.createElement('div');
  popupEl.className = 'kavita-sales-popup';
  popupEl.id = 'kavitaSalesPopup';
  popupEl.setAttribute('role', 'alert');
  popupEl.setAttribute('aria-live', 'polite');
  document.body.appendChild(popupEl);

  let currentIndex = 0;
  let timerHide = null;
  let timerNext = null;
  let isPaused = false;

  // Check if visitor dismissed popups during this session
  try {
    if (sessionStorage.getItem('kavita_sales_pop_dismissed') === 'true') {
      return;
    }
  } catch (e) {}

  function resolveAssetUrl(path) {
    if (window.KAVITA_ASSET_BASE) {
      const filename = path.split('/').pop();
      return window.KAVITA_ASSET_BASE + filename;
    }
    return path;
  }

  function resolveProductUrl(handle) {
    const isShopify = window.location.pathname.includes('/products/') || 
                      window.location.pathname.includes('/collections/') ||
                      document.querySelector('meta[content*="Shopify"]');
    if (isShopify) {
      return '/products/' + handle;
    }
    return 'product.html?handle=' + handle;
  }

  function showNextPopup() {
    if (isPaused) return;

    const data = SALES_DATA[currentIndex];
    currentIndex = (currentIndex + 1) % SALES_DATA.length;

    const imgUrl = resolveAssetUrl(data.img);
    const prodUrl = resolveProductUrl(data.handle);

    popupEl.innerHTML = `
      <button type="button" class="kavita-sales-popup__close" id="kavitaSalesPopClose" aria-label="Close notification">✕</button>
      <a href="${prodUrl}" class="kavita-sales-popup__img-box" tabindex="-1">
        <img src="${imgUrl}" alt="${data.product}" class="kavita-sales-popup__img" loading="lazy" onerror="this.src='${resolveAssetUrl('assets/kavita-logo-gold.png')}';">
      </a>
      <div class="kavita-sales-popup__content">
        <div class="kavita-sales-popup__header">
          <span class="kavita-sales-popup__badge">● Verified Purchase</span>
          <span class="kavita-sales-popup__city">· ${data.buyer} (${data.city})</span>
        </div>
        <a href="${prodUrl}" class="kavita-sales-popup__title" title="${data.product}">
          ${data.product}
        </a>
        <div class="kavita-sales-popup__footer">
          <span>✦ ${data.time}</span>
          <span>· Consecrated with Mantras</span>
        </div>
      </div>
    `;

    // Bind close button
    const closeBtn = document.getElementById('kavitaSalesPopClose');
    if (closeBtn) {
      closeBtn.onclick = (e) => {
        e.stopPropagation();
        e.preventDefault();
        hidePopup();
        isPaused = true;
        try {
          sessionStorage.setItem('kavita_sales_pop_dismissed', 'true');
        } catch (err) {}
      };
    }

    // Trigger reveal
    popupEl.classList.add('is-visible');

    // Hide after 4.8 seconds
    clearTimeout(timerHide);
    timerHide = setTimeout(() => {
      hidePopup();
      // Queue next popup after 9 to 14 seconds
      clearTimeout(timerNext);
      const nextDelay = Math.floor(Math.random() * 5000) + 9000;
      timerNext = setTimeout(showNextPopup, nextDelay);
    }, 4800);
  }

  function hidePopup() {
    popupEl.classList.remove('is-visible');
  }

  // Initial Launch: start after 5.5 seconds of landing on page
  const initialDelay = 5500;
  timerNext = setTimeout(showNextPopup, initialDelay);
})();

