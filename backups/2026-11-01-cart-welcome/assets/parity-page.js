(() => {
 let activeService=null,opener=null;
 const modal=document.getElementById('bookingModal');
 const titles=['Live Audio','WhatsApp Voice','Situational','Distance Cord','Vortex','Lamafera'];
 window.openBookingModal=(name)=>{
  activeService=STORE_PRODUCTS.find(p=>p.title===name)||STORE_PRODUCTS[titles.findIndex(t=>name.toLowerCase().includes(t.toLowerCase()))];
  if(!modal||!activeService){parityError(Error('Please select a reading first.'));return;}
  opener=document.activeElement;document.getElementById('modalServiceTitle').textContent=activeService.title;
  modal.classList.add('active');document.body.style.overflow='hidden';document.getElementById('clientName')?.focus({preventScroll:true});
 };
 window.closeBookingModal=()=>{modal?.classList.remove('active');document.body.style.overflow='';opener?.focus({preventScroll:true});};
 window.handleBookingSubmit=async event=>{
  event.preventDefault();const button=event.target.querySelector('[type=submit]');button.disabled=true;const props={};
  for(const [id,label] of [['clientName','Full name'],['clientDob','Date of birth'],['clientTime','Time of birth'],['clientPlace','Place of birth'],['clientPhone','WhatsApp'],['clientQuery','Questions']]){const field=document.getElementById(id);if(field?.value)props[label]=field.value;}
  try{await addToCart(activeService.title,activeService.price,activeService.img,activeService.handle,props);closeBookingModal();openCart();}catch{}finally{button.disabled=false;}
 };
 modal?.addEventListener('click',event=>{if(event.target===modal)closeBookingModal();});
 const submit=modal?.querySelector('[type=submit]');if(submit)submit.textContent='Continue to booking';
 document.addEventListener('keydown',event=>{if(event.key==='Escape')closeBookingModal();if(event.key==='Tab'&&modal?.classList.contains('active')){const nodes=[...modal.querySelectorAll('button,input,textarea,select,a[href]')].filter(e=>!e.disabled);const first=nodes[0],last=nodes.at(-1);if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}}});
 const ready=()=>{
  if(typeof currentProduct!=='undefined'&&currentProduct?.id<=6){const button=document.querySelector('[onclick="addCurrentProductToCart()"]');if(button){button.textContent='Book this session';button.onclick=()=>openBookingModal(currentProduct.title);}}
  document.querySelectorAll('a[href*="product.html?id="]').forEach(a=>{const id=Number(a.href.split('id=')[1]);const p=STORE_PRODUCTS.find(x=>x.id===id);if(p)a.href='/products/'+p.handle;});
  // Preserve the local card composition while displaying the live Shopify price.
  document.querySelectorAll('.product-card').forEach(card=>{const link=card.querySelector('a[href*="/products/"]');const p=STORE_PRODUCTS.find(p=>link?.getAttribute('href').split('?')[0]==='/products/'+p.handle);if(!p)return;const price=card.querySelector('.current-price');if(price)price.textContent='₹'+p.price.toLocaleString('en-IN');const compare=card.querySelector('.compare-price');if(compare){compare.textContent='₹'+p.comparePrice.toLocaleString('en-IN');compare.hidden=p.comparePrice<=p.price;}});
 };
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',ready);else ready();
 window.buyViaWhatsApp=()=>{if(typeof currentProduct!=='undefined'){if(currentProduct.id<=6)openBookingModal(currentProduct.title);else addToCart(currentProduct.title,currentProduct.price,currentProduct.img,currentProduct.handle,{},typeof currentQty==='number'?currentQty:1);}};
})();
// Use Shopify checkout for consultation intake, never the preview's placeholder phone.
window.handleConsultationSubmit=async event=>{
 event.preventDefault();const value=id=>document.getElementById(id)?.value||'';
 const name=value('selectedServiceInput');const match=STORE_PRODUCTS.slice(0,6).find(p=>name.toLowerCase().includes(p.title.split(' ').slice(0,2).join(' ').toLowerCase()))||STORE_PRODUCTS.find(p=>name.toLowerCase().includes(p.categoryLabel.toLowerCase()));
 if(!match){parityError(Error('Please choose a consultation before continuing.'));return;}
 const button=event.target.querySelector('[type=submit]');button.disabled=true;
 try{await addToCart(match.title,match.price,match.img,match.handle,{'Full name':value('clientFullName'),'WhatsApp':value('clientMobile'),'Date of birth':value('clientBirthDate'),'Time of birth':value('clientBirthTime'),'Place of birth':value('clientBirthPlace'),'Preferred time':value('clientSlot'),'Questions':value('clientQuestions')});}finally{button.disabled=false;}
};
