/* Shopify-native commerce behind the approved local presentation. */
var cart=[];
const parityRoot=window.Shopify?.routes?.root||'/';
const parityAsset=p=>p?.startsWith('assets/')?window.KAVITA_ASSET_BASE+p.slice(7):p;
STORE_PRODUCTS.forEach(p=>{p.img=parityAsset(p.img);p.images=(p.images||[]).map(parityAsset);const live=window.KAVITA_LIVE_PRODUCTS?.[p.handle];if(live&&live.handle===p.handle){if(live.featured_image){p.img=live.featured_image;if(live.images&&live.images.length>0)p.images=live.images;}if(live.price>0)p.price=live.price/100;if(live.compare_at_price>0)p.comparePrice=live.compare_at_price/100;if(live.variants?.[0]?.id)p.variantId=live.variants[0].id;p.available=live.available;p.live=live;}});
const CartEngine={getCart:()=>cart,updateBadges:()=>document.querySelectorAll('#cartCount,#kavita-cart-badge,.cart-badge,#mobileCartCount,#cartCountHeader,.kavita-hdr__badge--cart').forEach(el=>el.textContent=cart.reduce((sum,p)=>sum+p.qty,0))};
async function parityRequest(endpoint,body){const response=await fetch(parityRoot+endpoint,{method:body?'POST':'GET',headers:{'Content-Type':'application/json',Accept:'application/json'},body:body?JSON.stringify(body):undefined});const data=await response.json();if(!response.ok)throw Error(data.description||'Unable to update your bag. Please try again.');return data;}
async function refreshCart(){const data=await parityRequest('cart.js');cart=data.items.map(item=>({id:item.product_id,key:item.key,variantId:item.variant_id,name:item.product_title,title:item.product_title,price:item.final_price/100,img:item.image,qty:item.quantity,properties:item.properties}));updateCartUI();if(typeof renderCartPage==='function')renderCartPage();return data;}
function updateCartUI(){CartEngine.updateBadges();if(typeof renderCartDrawer==='function')renderCartDrawer();}
function openCart(){const drawer=document.getElementById('cartDrawer'),overlay=document.getElementById('cartOverlay');if(!drawer){location.href=parityRoot+'cart';return;}drawer.classList.add('active');overlay?.classList.add('active');drawer.setAttribute('role','dialog');drawer.setAttribute('aria-modal','true');document.body.style.overflow='hidden';updateCartUI();refreshCart().catch(parityError);}
function closeCart(){document.querySelectorAll('.cart-drawer,.cart-drawer-overlay').forEach(e=>e.classList.remove('active'));if(!document.querySelector('.modal-overlay.active'))document.body.style.overflow='';}
function parityError(error){let status=document.getElementById('storeStatus');if(!status){status=document.createElement('p');status.id='storeStatus';status.role='alert';document.body.append(status);}status.textContent=error.message;status.hidden=false;}
let parityQueue=Promise.resolve();
function addToCart(name,price,img,handle,properties={},quantity=1){const item=STORE_PRODUCTS.find(p=>p.handle===handle||p.title===name||p.img===img);if(!item?.variantId){parityError(Error('This item is not available to purchase.'));return Promise.reject(Error('Product unavailable'));}const run=async()=>{await parityRequest('cart/add.js',{items:[{id:item.variantId,quantity,properties}]});window.location.href='/checkout';};parityQueue=parityQueue.catch(()=>{}).then(run);return parityQueue.catch(e=>{parityError(e);window.location.href='/checkout';});}
window.bookConsultationDirect=async function(variantId,properties={}){if(!variantId){window.location.href='/checkout';return;}try{await parityRequest('cart/add.js',{items:[{id:variantId,quantity:1,properties}]});window.location.href='/checkout';}catch(e){window.location.href='/checkout';}};
window.buyViaWhatsApp=function(){if(typeof addCurrentProductToCart==='function'){addCurrentProductToCart();}else{window.location.href='/checkout';}};
async function changeQty(index,delta){try{const item=cart[index];if(!item)return;await parityRequest('cart/change.js',{id:item.key,quantity:Math.max(0,item.qty+delta)});await refreshCart();}catch(e){parityError(e);}}
async function removeFromCart(index){if(cart[index])return changeQty(index,-cart[index].qty);}
async function saveCart(){if(!cart.length){await parityRequest('cart/clear.js',{});await refreshCart();}}
function checkoutCart(){location.href='/checkout';}
function playSacredChime(){}
document.addEventListener('DOMContentLoaded',()=>refreshCart().catch(parityError));
