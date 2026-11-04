/* Shared interactions for the static storefront; no Shopify API credentials. */
(() => {
  const status=document.createElement('div'); status.id='storeStatus'; status.role='status'; status.hidden=true;
  status.style.cssText='position:fixed;bottom:100px;left:16px;right:16px;max-width:440px;margin:auto;padding:16px;background:#321923;color:white;border-radius:8px;z-index:1000;font-size:13px'; document.body.append(status);
  document.getElementById('openCartBtn')?.addEventListener('click',openCart);
  const actions=document.querySelector('.kavita-hdr__actions');
  if(actions&&!actions.querySelector('.kavita-hdr__icon-btn--reading')){
    const reading=document.createElement('a');reading.href='/?view=consultations';reading.className='kavita-hdr__icon-btn kavita-hdr__icon-btn--reading';reading.setAttribute('aria-label','Book a reading');reading.title='Book a reading';
    reading.innerHTML='<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="5" width="16" height="16" rx="3"/><path d="M8 3v4m8-4v4M4 10h16m-8 3 .8 2.2L15 16l-2.2.8L12 19l-.8-2.2L9 16l2.2-.8Z"/></svg>';
    const wishlist=actions.querySelector('[aria-label="Wishlist"]');actions.insertBefore(reading,wishlist||actions.firstChild);
  }
  const nav=document.querySelector('.kavita-hdr__nav-bar');
  if(nav) nav.id='store-navigation';
  window.closeQuickView=()=>document.getElementById('quickViewModal')?.classList.remove('active');
  window.closeSearchModal=()=>document.getElementById('searchModal')?.classList.remove('active');
  window.openSearchModal=()=>{
    const wrap=document.querySelector('.kavita-hdr__search-wrap');
    if(wrap) { wrap.classList.toggle('search-is-open'); wrap.querySelector('input')?.focus(); }
  };
  document.querySelectorAll('.kavita-hdr__icon-btn--search-mobile').forEach(button=>{button.removeAttribute('onclick');button.addEventListener('click',e=>{e.preventDefault();openSearchModal();});});
  // Pages which omitted a mobile search action receive the same control.
  if(!document.querySelector('.kavita-hdr__icon-btn--search-mobile')) {
    const button=document.createElement('button');button.type='button';button.className='kavita-hdr__icon-btn kavita-hdr__icon-btn--search-mobile';button.textContent='⌕';button.setAttribute('aria-label','Search store');button.addEventListener('click',openSearchModal);document.querySelector('.kavita-hdr__actions')?.prepend(button);
  }
  document.querySelectorAll('.faq-question').forEach((old,index)=>{
    const button=document.createElement('button'); button.type='button';button.className=old.className;button.innerHTML=old.innerHTML;
    const item=old.closest('.faq-item'),answer=item.querySelector('.faq-answer');answer.id='faq-answer-'+index;
    button.setAttribute('aria-controls',answer.id);button.setAttribute('aria-expanded',item.classList.contains('active'));
    button.addEventListener('click',()=>{const expanded=item.classList.toggle('active');button.setAttribute('aria-expanded',expanded);});old.replaceWith(button);
  });
  // Only intentions scroll; offerings and products remain grids.
  document.querySelectorAll('.luxury-intentions-grid').forEach((track,index)=>{
    track.id=track.id||'intention-slider-'+index;
    track.tabIndex=0;track.setAttribute('aria-label','Shop by intention');
    const controls=document.createElement('div');controls.className='slider-controls';
    const prev=document.createElement('button'),next=document.createElement('button'),label=document.createElement('span');
    prev.textContent='←';next.textContent='→';prev.type=next.type='button';
    prev.setAttribute('aria-label','Previous intentions');next.setAttribute('aria-label','Next intentions');
    prev.setAttribute('aria-controls',track.id);next.setAttribute('aria-controls',track.id);
    label.textContent='Explore at your own pace';controls.append(prev,label,next);track.after(controls);
    const update=()=>{prev.disabled=track.scrollLeft<2;next.disabled=track.scrollLeft+track.clientWidth>=track.scrollWidth-2;controls.hidden=track.scrollWidth<=track.clientWidth+2;};
    const move=direction=>track.scrollBy({left:direction*(track.firstElementChild.getBoundingClientRect().width+parseFloat(getComputedStyle(track).columnGap)),behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
    prev.addEventListener('click',()=>move(-1));next.addEventListener('click',()=>move(1));
    track.addEventListener('keydown',event=>{if(event.target===track&&['ArrowLeft','ArrowRight'].includes(event.key)){event.preventDefault();move(event.key==='ArrowRight'?1:-1);}});
    track.addEventListener('scroll',update,{passive:true});new ResizeObserver(update).observe(track);update();
  });
  // Persist actual product IDs, not a counter detached from products.
  const readWishlist=()=>{try{return JSON.parse(localStorage.getItem('kavita_wishlist_ids')||'[]');}catch{return [];}};
  const syncWishlist=()=>{
    const ids=readWishlist();document.querySelectorAll('.product-wishlist-heart').forEach(button=>{const id=Number(button.getAttribute('onclick')?.match(/,\s*(\d+)/)?.[1]);const active=ids.includes(id);button.classList.toggle('is-active',active);button.textContent=active?'♥':'♡';button.setAttribute('aria-pressed',active);});
    document.querySelectorAll('#mobileWishlistCount, [aria-label="Wishlist"] .kavita-hdr__badge').forEach(el=>el.textContent=ids.length);
  };
  window.toggleWishlist=(button,id)=>{let ids=readWishlist();ids=ids.includes(id)?ids.filter(value=>value!==id):[...ids,id];localStorage.setItem('kavita_wishlist_ids',JSON.stringify(ids));syncWishlist();};
  document.querySelectorAll('.mobile-nav-item').forEach(a=>{if(a.textContent.includes('Wishlist'))a.href='/collections/all?wishlist=1';});
  window.addEventListener('DOMContentLoaded',()=>{
    syncWishlist();
    // Welcome offer is initialized by welcome.js.
    if(typeof renderCollection==='function') {
      const params=new URLSearchParams(location.search),query=params.get('search')?.trim().toLowerCase();
      const baseApply=window.applyFilters;
      window.applyFilters=()=>{baseApply();if(query)activeProducts=activeProducts.filter(p=>(p.title+' '+p.categoryLabel+' '+p.intention).toLowerCase().includes(query));if(params.has('wishlist'))activeProducts=activeProducts.filter(p=>readWishlist().includes(p.id));if(params.get('cat')==='oracle')activeProducts=activeProducts.filter(p=>p.title.toLowerCase().includes('oracle'));applySorting();syncWishlist();};
      window.applyFilters();
    }
  });
  document.addEventListener('keydown' ,event=>{if(event.key==='Escape'){document.querySelectorAll('.modal-overlay.active').forEach(el=>el.classList.remove('active'));closeCart();document.getElementById('welcomeDialog')?.close();}});

  // Live Predictive Search Dropdown Engine
  function initPredictiveSearch() {
    const searchWrap = document.querySelector('.kavita-hdr__search-wrap');
    if (!searchWrap) return;
    const searchInput = searchWrap.querySelector('.kavita-hdr__search-input') || searchWrap.querySelector('input[type="search"]') || searchWrap.querySelector('input');
    if (!searchInput) return;

    let dropdown = document.getElementById('kavitaSearchDropdown');
    if (!dropdown) {
      dropdown = document.createElement('div');
      dropdown.id = 'kavitaSearchDropdown';
      dropdown.className = 'kavita-search-dropdown';
      dropdown.setAttribute('role', 'listbox');
      dropdown.setAttribute('aria-label', 'Search suggestions');
      searchWrap.appendChild(dropdown);
    }

    const isShopify = typeof window.Shopify !== 'undefined' || location.pathname.startsWith('/collections') || location.pathname.startsWith('/products');

    const quickLinks = [
      { label: '✦ Live Audio Tarot', query: 'Live Audio' },
      { label: '✦ WhatsApp Voice Note', query: 'Voice Note' },
      { label: '✦ Golden Pyrite Cluster', query: 'Pyrite' },
      { label: '✦ 7 Chakra Bracelet', query: 'Chakra' },
      { label: '✦ Cord-Cutting Healing', query: 'Cord-Cutting' },
      { label: '✦ Gold Tarot Deck', query: 'Tarot Deck' }
    ];

    function getProductUrl(p) {
      if (isShopify) {
        const root = (window.Shopify?.routes?.root || '/');
        return root + 'products/' + (p.handle || p.id);
      }
      return '/products/?id=' + p.id;
    }

    function getSearchUrl(q) {
      if (isShopify) {
        return (window.Shopify?.routes?.root || '/') + 'collections/all?search=' + encodeURIComponent(q);
      }
      return '/collections/all?search=' + encodeURIComponent(q);
    }

    function escapeHtml(s) {
      if (!s) return '';
      return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    function highlightMatch(text, q) {
      const i = text.toLowerCase().indexOf(q.toLowerCase());
      if (i === -1) return escapeHtml(text);
      const before = escapeHtml(text.substring(0, i));
      const match = escapeHtml(text.substring(i, i + q.length));
      const after = escapeHtml(text.substring(i + q.length));
      return before + '<mark style="background: rgba(212, 175, 55, 0.35); color: #80142B; padding: 0 2px; border-radius: 2px; font-weight: 800;">' + match + '</mark>' + after;
    }

    function renderItem(p, q) {
      const titleEsc = escapeHtml(p.title);
      const titleHtml = q ? highlightMatch(p.title, q) : titleEsc;
      const priceFormatted = '₹' + Number(p.price).toLocaleString('en-IN');
      const compareFormatted = p.comparePrice && p.comparePrice > p.price ? '₹' + Number(p.comparePrice).toLocaleString('en-IN') : '';

      return '<a href="' + getProductUrl(p) + '" class="kavita-search-dropdown__item">' +
        '<img src="' + p.img + '" alt="' + titleEsc + '" class="kavita-search-dropdown__thumb" onerror="this.style.opacity=0.5;">' +
        '<div class="kavita-search-dropdown__info">' +
          '<div class="kavita-search-dropdown__title">' + titleHtml + '</div>' +
          '<div class="kavita-search-dropdown__meta">' +
            (p.categoryLabel ? '<span class="kavita-search-dropdown__badge">' + escapeHtml(p.categoryLabel) + '</span>' : '') +
            '<span class="kavita-search-dropdown__price">' + priceFormatted + '</span>' +
            (compareFormatted ? '<span class="kavita-search-dropdown__compare-price">' + compareFormatted + '</span>' : '') +
          '</div>' +
        '</div>' +
        '<span style="color: #C59B27; font-size: 0.95rem; font-weight: bold; margin-left: auto;">↗</span>' +
      '</a>';
    }

    function render(query) {
      query = (query || '').trim();
      const catalog = window.STORE_PRODUCTS || [];

      if (!query) {
        let html = '<div class="kavita-search-dropdown__header"><span>Popular Offerings</span><span style="font-size:0.68rem;color:#8A6414;">✦ Quick Select</span></div>';
        html += '<div style="padding: 10px 14px; display: flex; flex-wrap: wrap; gap: 4px;">';
        quickLinks.forEach(item => {
          html += '<a href="' + getSearchUrl(item.query) + '" class="kavita-search-dropdown__quick-tag">' + item.label + '</a>';
        });
        html += '</div>';

        const featured = catalog.slice(0, 3);
        if (featured.length > 0) {
          html += '<div class="kavita-search-dropdown__header"><span>Curated for You</span></div>';
          featured.forEach(p => {
            html += renderItem(p, '');
          });
        }
        dropdown.innerHTML = html;
        dropdown.classList.add('active');
        return;
      }

      const qLower = query.toLowerCase();
      const matches = catalog.filter(p => {
        return (
          (p.title && p.title.toLowerCase().includes(qLower)) ||
          (p.category && p.category.toLowerCase().includes(qLower)) ||
          (p.categoryLabel && p.categoryLabel.toLowerCase().includes(qLower)) ||
          (p.intention && p.intention.toLowerCase().includes(qLower)) ||
          (p.description && p.description.toLowerCase().includes(qLower))
        );
      }).slice(0, 5);

      if (matches.length === 0) {
        dropdown.innerHTML = '<div class="kavita-search-dropdown__empty">' +
          '<p style="font-weight: 700; color: #1C1917; margin-bottom: 6px;">No sacred offerings found for "' + escapeHtml(query) + '"</p>' +
          '<p style="font-size: 0.8rem; color: #7D756D; margin-bottom: 12px;">Try searching for "Pyrite", "Audio", or "Chakra"</p>' +
          '<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 4px;">' +
            quickLinks.slice(0, 4).map(item => '<a href="' + getSearchUrl(item.query) + '" class="kavita-search-dropdown__quick-tag">' + item.label + '</a>').join('') +
          '</div>' +
        '</div>';
        dropdown.classList.add('active');
        return;
      }

      let html = '<div class="kavita-search-dropdown__header"><span>Products (' + matches.length + ')</span><span style="font-size:0.68rem;color:#7D756D;">Press Enter to search all</span></div>';
      matches.forEach(p => {
        html += renderItem(p, query);
      });
      html += '<a class="kavita-search-dropdown__footer" href="' + getSearchUrl(query) + '">View all results for &quot;' + escapeHtml(query) + '&quot; ➔</a>';

      dropdown.innerHTML = html;
      dropdown.classList.add('active');
    }

    let timer;
    searchInput.addEventListener('input', e => {
      clearTimeout(timer);
      timer = setTimeout(() => render(e.target.value), 100);
    });

    searchInput.addEventListener('focus', e => {
      render(e.target.value);
    });

    document.addEventListener('click', e => {
      if (!searchWrap.contains(e.target)) {
        dropdown.classList.remove('active');
      }
    });

    searchInput.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        dropdown.classList.remove('active');
      }
    });
  }

  
  // Mobile Slide-Out Drawer Engine
  function initMobileDrawer() {
    let drawer = document.getElementById('mobileMenuDrawer');
    if (!drawer) {
      drawer = document.createElement('div');
      drawer.id = 'mobileMenuDrawer';
      drawer.className = 'kavita-mobile-drawer';
      drawer.setAttribute('aria-hidden', 'true');

      const isShopify = typeof window.Shopify !== 'undefined' || location.pathname.startsWith('/collections') || location.pathname.startsWith('/products');
      const root = isShopify ? (window.Shopify?.routes?.root || '/') : '';
      const allColUrl = isShopify ? root + 'collections/all' : '/collections/all';
      const readingsUrl = isShopify ? root + '?view=consultations' : '/?view=consultations';
      const aboutUrl = isShopify ? root + '?view=about' : '/?view=about';
      const contactUrl = isShopify ? root + 'pages/contact' : '/pages/contact';
      const faqUrl = isShopify ? root + '?view=faq' : '/?view=faq';
      const homeUrl = isShopify ? root : '/';

      drawer.innerHTML = `
        <div class="kavita-mobile-drawer__overlay" onclick="closeMobileMenu()"></div>
        <div class="kavita-mobile-drawer__panel">
          <div class="kavita-mobile-drawer__header">
            <div class="kavita-mobile-drawer__brand">
              <span style="font-family: 'Cinzel', serif; font-weight: 800; font-size: 1.05rem; color: #1C1917; letter-spacing: 0.08em;">✦ KAVITA TAROT</span>
            </div>
            <button type="button" class="kavita-mobile-drawer__close" onclick="closeMobileMenu()" aria-label="Close menu">✕</button>
          </div>
          <div class="kavita-mobile-drawer__body">
            <ul class="kavita-mobile-drawer__nav">
              <li><a href="${homeUrl}" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">🏠</span> Home</a></li>
              <li><a href="${allColUrl}" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">🎴</span> All Offerings</a></li>
              <li><a href="${allColUrl}?cat=tarot" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">✨</span> Tarot Decks</a></li>
              <li><a href="${allColUrl}?cat=oracle" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">🌙</span> Oracle Cards</a></li>
              <li><a href="${allColUrl}?cat=crystals" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">💎</span> Crystals & Sacred Stones</a></li>
              <li><a href="${readingsUrl}" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">🔮</span> 1-on-1 Consultations</a></li>
              <li><a href="${aboutUrl}" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">🕊️</span> Meet Kavita</a></li>
              <li><a href="${contactUrl}" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">✉️</span> Contact & Booking</a></li>
              <li><a href="${faqUrl}" class="kavita-mobile-drawer__link" onclick="closeMobileMenu()"><span class="k-drawer-icon">❓</span> Frequently Asked Questions</a></li>
            </ul>
            <div class="kavita-mobile-drawer__footer">
              <a href="https://wa.me/919990788358?text=Hi+Kavita%2C+I+would+like+to+book+a+tarot+reading." target="_blank" class="kavita-mobile-drawer__wa-btn">
                💬 WhatsApp Direct Booking: +91 93103 87104
              </a>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(drawer);
    }

    window.openMobileMenu = function() {
      const d = document.getElementById('mobileMenuDrawer');
      if (d) {
        d.classList.add('active');
        d.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }
    };

    window.closeMobileMenu = function() {
      const d = document.getElementById('mobileMenuDrawer');
      if (d) {
        d.classList.remove('active');
        d.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      }
    };

    /* removed toggle */ [].forEach(btn => {
      btn.onclick = (e) => {
        e.preventDefault();
        openMobileMenu();
      };
    });
  }

  // ==========================================
  // SACRED SANCTUARY NEWSLETTER POP-UP (10% OFF)
  // Non-permanent: Shows once on visit, permanently silenced on dismiss/subscribe
  // ==========================================
  window.openNewsletterPopup = function() {
    let overlay = document.getElementById('kavitaNewsletterOverlay') || document.getElementById('kavitaWelcomeOverlay');
    if (!overlay) return;
    overlay.style.display = 'flex';
    requestAnimationFrame(() => {
      overlay.classList.add('active');
    });
  };
  window.openWelcomePopup = window.openNewsletterPopup;

  window.closeNewsletterPopup = function() {
    let overlay = document.getElementById('kavitaNewsletterOverlay') || document.getElementById('kavitaWelcomeOverlay');
    if (overlay) {
      overlay.classList.remove('active');
      setTimeout(() => {
        if (overlay && !overlay.classList.contains('active')) {
          overlay.style.display = 'none';
        }
      }, 350);
    }
    // Permanently remember that the user dismissed the newsletter
    try {
      localStorage.setItem('kavita_newsletter_dismissed', 'true');
    } catch (e) {}
  };
  window.closeWelcomePopup = window.closeNewsletterPopup;

  window.handleNewsletterSubmit = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    const emailInput = document.getElementById('kavitaNewsletterEmail');
    const email = emailInput ? emailInput.value.trim() : '';
    if (!email || !email.includes('@')) {
      alert('Please enter a valid email address.');
      return false;
    }

    const discountData = { code: 'WELCOME10', percent: 10, email: email, subscribedAt: Date.now() };
    try {
      localStorage.setItem('kavita_discount', JSON.stringify(discountData));
      sessionStorage.setItem('kavita_discount', JSON.stringify(discountData));
      localStorage.setItem('kavita_newsletter_subscribed', 'true');
      localStorage.setItem('kavita_newsletter_dismissed', 'true');

      let subscribers = [];
      try {
        subscribers = JSON.parse(localStorage.getItem('kavita_subscribers') || '[]');
      } catch (err) {}
      if (!subscribers.includes(email)) {
        subscribers.push(email);
        localStorage.setItem('kavita_subscribers', JSON.stringify(subscribers));
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText('WELCOME10');
      }
    } catch (e) {}

    // Show success confirmation
    const form = document.getElementById('kavitaNewsletterForm');
    const success = document.getElementById('kavitaNewsletterSuccess');
    if (form) form.style.display = 'none';
    if (success) success.style.display = 'block';

    if (typeof renderCartDrawer === 'function') {
      renderCartDrawer();
    }

    setTimeout(() => {
      window.closeNewsletterPopup();
    }, 2500);

    return false;
  };

  function initNewsletterPopup() {
    const overlay = document.getElementById('kavitaNewsletterOverlay') || document.getElementById('kavitaWelcomeOverlay');
    if (!overlay) return;

    const closeBtn = document.getElementById('kavitaNewsletterCloseBtn') || document.getElementById('kavitaWelcomeCloseBtn');
    if (closeBtn && !closeBtn._bound) {
      closeBtn._bound = true;
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        window.closeNewsletterPopup();
      });
    }

    if (overlay && !overlay._bound) {
      overlay._bound = true;
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
          window.closeNewsletterPopup();
        }
      });
    }

    // Auto-launch once on visit if not dismissed or already subscribed
    const urlParams = new URLSearchParams(window.location.search);
    const forceShow = urlParams.get('popup') === '1' || urlParams.get('newsletter') === '1';
    let isDismissed = false;
    try {
      isDismissed = localStorage.getItem('kavita_newsletter_dismissed') === 'true' ||
                    localStorage.getItem('kavita_newsletter_subscribed') === 'true';
    } catch (e) {}

    if (forceShow || !isDismissed) {
      setTimeout(() => {
        window.openNewsletterPopup();
      }, 1800);
    }
  }

  // Bind initializers on both immediate and DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initMobileDrawer();
      initPredictiveSearch();
      initNewsletterPopup();
    });
  } else {
    initMobileDrawer();
    initPredictiveSearch();
    initNewsletterPopup();
  }

  // Backup check in case elements rendered asynchronously
  setTimeout(initNewsletterPopup, 800);

  // 2027 Spotlight Slider & Direct Checkout Handlers
  let currentSpotlightSlide = 0;
  window.slideSpotlight = function(direction) {
    const totalSlides = 2;
    currentSpotlightSlide = (currentSpotlightSlide + direction + totalSlides) % totalSlides;
    window.updateSpotlightUI();
  };
  window.setSpotlightSlide = function(index) {
    currentSpotlightSlide = index;
    window.updateSpotlightUI();
  };
  window.updateSpotlightUI = function() {
    const track = document.getElementById('spotlightTrack');
    if (track) {
      track.style.transform = `translateX(-${currentSpotlightSlide * 100}%)`;
    }
    const dots = document.querySelectorAll('.spotlight-dot');
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSpotlightSlide);
    });
  };
  window.directCheckout2027 = async function() {
    const vid = 48598240166049;
    try {
      if (typeof parityRequest === 'function') {
        await parityRequest('cart/add.js', { items: [{ id: vid, quantity: 1 }] });
        window.location.href = '/checkout';
        return;
      }
      if (typeof fetch === 'function') {
        await fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ items: [{ id: vid, quantity: 1 }] })
        });
        window.location.href = '/checkout';
        return;
      }
    } catch (e) {}
    if (typeof addToCart === 'function') {
      addToCart('2027 Year-Ahead Reading – Complete Year, Month-by-Month (Diwali Special)', 3333, 'assets/product-2027-year-ahead-cover.jpg', '2027-year-ahead-reading-diwali-special');
    }
    window.location.href = '/checkout';
  };
})();
