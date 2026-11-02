(() => {
 const dialog=document.getElementById('welcomeDialog');if(!dialog)return;
 const get=k=>{try{return sessionStorage.getItem(k);}catch{return null;}},set=(k,v)=>{try{sessionStorage.setItem(k,v);}catch{}};
 let opener;const close=()=>{dialog.close();opener?.focus({preventScroll:true});};
 dialog.querySelector('.welcome-close').onclick=close;
 dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)close();}});
 if(!get('kavita_welcome_seen'))setTimeout(()=>{if(document.querySelector('.modal-overlay.active,#cartDrawer.active'))return;opener=document.activeElement;dialog.showModal();set('kavita_welcome_seen','1');dialog.querySelector('.welcome-close').focus();},2000);
 dialog.querySelector('.welcome-claim').onclick=async function(){this.disabled=true;const status=dialog.querySelector('.welcome-status');try{const r=await fetch('/cart/update.js',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({discount:'WELCOME10'})});if(!r.ok)throw Error();const cart=await r.json();const code=cart.discount_codes?.find(d=>d.code.toUpperCase()==='WELCOME10');if(code?.applicable){set('kavita_welcome_claimed','1');status.textContent='WELCOME10 applied. Your discount will appear at checkout.';this.textContent='DISCOUNT CLAIMED';}else{status.textContent='Code: WELCOME10. Eligibility is checked at checkout.';this.textContent='CODE SAVED';set('kavita_welcome_claimed','1');}if(typeof refreshCart==='function')refreshCart().catch(()=>{});}catch{status.textContent='Please enter WELCOME10 at checkout.';}finally{this.disabled=false;}};
})();
