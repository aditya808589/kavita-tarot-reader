/* Shared interactions for the static storefront; no Shopify API credentials. */
(() => {
  const status=document.createElement('div'); status.id='storeStatus'; status.role='status'; status.hidden=true;
  status.style.cssText='position:fixed;bottom:100px;left:16px;right:16px;max-width:440px;margin:auto;padding:16px;background:#321923;color:white;border-radius:8px;z-index:1000;font-size:13px'; document.body.append(status);
  document.getElementById('openCartBtn')?.addEventListener('click',openCart);
  const nav=document.querySelector('.kavita-hdr__nav-bar');
  if(nav) {
    nav.id='store-navigation';const toggle=document.createElement('button');toggle.className='store-menu-toggle';toggle.type='button';toggle.textContent='☰';toggle.setAttribute('aria-label','Open menu');toggle.setAttribute('aria-controls',nav.id);toggle.setAttribute('aria-expanded','false');
    toggle.addEventListener('click',()=>{const open=nav.classList.toggle('menu-is-open');toggle.setAttribute('aria-expanded',open);toggle.setAttribute('aria-label',open?'Close menu':'Open menu');toggle.textContent=open?'×':'☰';});document.querySelector('.kavita-hdr__actions')?.prepend(toggle);
  }
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
  document.querySelectorAll('.mobile-nav-item').forEach(a=>{if(a.textContent.includes('Wishlist'))a.href='collections.html?wishlist=1';});
  window.addEventListener('DOMContentLoaded',()=>{
    syncWishlist();
    if(typeof renderCollection==='function') {
      const params=new URLSearchParams(location.search),query=params.get('search')?.trim().toLowerCase();
      const baseApply=window.applyFilters;
      window.applyFilters=()=>{baseApply();if(query)activeProducts=activeProducts.filter(p=>(p.title+' '+p.categoryLabel+' '+p.intention).toLowerCase().includes(query));if(params.has('wishlist'))activeProducts=activeProducts.filter(p=>readWishlist().includes(p.id));if(params.get('cat')==='oracle')activeProducts=activeProducts.filter(p=>p.title.toLowerCase().includes('oracle'));applySorting();syncWishlist();};
      window.applyFilters();
    }
  });
  document.addEventListener('keydown' ,event=>{if(event.key==='Escape'){document.querySelectorAll('.modal-overlay.active').forEach(el=>el.classList.remove('active'));closeCart();}});
})();
