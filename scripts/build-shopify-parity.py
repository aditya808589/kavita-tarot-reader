"""Port approved static storefront presentation; native commerce is parity-commerce.js."""
from pathlib import Path
import re,json,shutil
root=Path(__file__).resolve().parent.parent;r=root/'kavita-dawn'
pages=['index','collections','consultations','product','about','contact','faq','cart','packages']
handles=re.findall(r'["\']?handle["\']?\s*:\s*["\']([^"\']+)["\']',(root/'assets/store-data.js').read_text())
route={'index':'/','collections':'/collections/all','consultations':'/?view=consultations','product':'/products/','about':'/?view=about','contact':'/pages/contact','faq':'/?view=faq','cart':'/cart','packages':'/?view=packages'}
def links(s):
 for i,h in enumerate(handles,1):s=s.replace('product.html?id='+str(i)+('"' if False else '~'),'') if False else s
 s=re.sub(r'product\.html\?id=(\d+)',lambda m:'/products/'+handles[int(m[1])-1] if 0 <= int(m[1])-1 < len(handles) else '/products',s)
 for name,url in route.items():s=s.replace(name+'.html?',url+('&' if '?' in url else '?')).replace(name+'.html',url)
 return s.replace('/products/?id=${p.id}','/products/${p.handle}')
# Assets required by the exact static source, including existing imagery.
asset_names=set()
for name in pages:
 source=(root/(name+'.html')).read_text();asset_names.update(re.findall(r'assets/([\w.-]+)',source))
for p in (root/'assets').iterdir():
 if p.is_file() and (p.name in asset_names or p.suffix.lower() in ['.jpg','.jpeg','.png','.webp']):shutil.copyfile(p,r/'assets'/p.name)
for name in ['storefront-refinements.css','category-grid.css','vanikabir.css','ice-effect.js']:
 shutil.copyfile(root/'assets'/name,r/'assets'/('parity-'+name))
# shared catalogue is enriched with live Shopify variant IDs and prices
catalog=(root/'assets/store-data.js').read_text().split('/* Active Cart State')[0]
catalog=links(catalog)
catalog=catalog.replace('const STORE_PRODUCTS', 'var STORE_PRODUCTS')
(r/'assets/parity-catalog.js').write_text(catalog)
ui=links((root/'assets/storefront-ui.js').read_text());(r/'assets/parity-ui.js').write_text(ui)
cart=(root/'assets/storefront-cart.js').read_text();a=cart.index('function renderCartDrawer()');b=cart.index('function addToCart(',a)
(r/'assets/parity-cart-render.js').write_text(links(cart[a:b]))
layout='''<!doctype html><html lang="{{ request.locale.iso_code }}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{{ page_title | escape }} — Kavita Tarot Reader</title><link rel="canonical" href="{{ canonical_url }}">{{ content_for_header }}
<link rel="icon" type="image/x-icon" href="{{ 'favicon.ico' | asset_url }}">
<link rel="icon" type="image/png" sizes="32x32" href="{{ 'kavita-favicon-32x32.png' | asset_url }}">
<link rel="icon" type="image/png" sizes="192x192" href="{{ 'kavita-favicon.png' | asset_url }}">
<link rel="apple-touch-icon" sizes="180x180" href="{{ 'apple-touch-icon.png' | asset_url }}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{{ 'parity-vanikabir.css' | asset_url | stylesheet_tag }}
{{ 'parity-category-grid.css' | asset_url | stylesheet_tag }}
{{ 'parity-storefront-refinements.css' | asset_url | stylesheet_tag }}
<script>window.KAVITA_ASSET_BASE={{ 'kavita-logo-gold.png' | asset_url | split: 'kavita-logo-gold.png' | first | json }};window.KAVITA_HANDLE={{ product.handle | json }};</script>
<script src="{{ 'parity-catalog.js' | asset_url }}"></script>
<script>window.KAVITA_LIVE_PRODUCTS={
'''
for i,h in enumerate(handles):
 layout+="{% assign entry = nil %}{% assign entry = all_products['"+h+"'] %}"+json.dumps(h)+":{% if entry != blank and entry.handle == '"+h+"' %}{{ entry | json }}{% else %}null{% endif %}"+(',' if i<len(handles)-1 else '')+'\n'
layout+='''};</script><script src="{{ 'parity-commerce.js' | asset_url }}"></script><script src="{{ 'parity-cart-render.js' | asset_url }}"></script>
</head><body>{{ content_for_layout }}</body></html>'''
(r/'layout/parity.liquid').write_text(layout)
for name in pages:
 s=(root/(name+'.html')).read_text()
 head=s.split('</head>')[0];styles='\n'.join(re.findall(r'<style>.*?</style>',head,re.S))
 body=re.search(r'<body[^>]*>(.*)</body>',s,re.S)[1]
 body=re.sub(r'<script src="assets/(?:store-data|storefront-cart|storefront-ui)\.js"></script>','',body)
 # Real product handles determine product page, not local query IDs.
 body=body.replace("STORE_PRODUCTS.find(p => p.id === idParam) || STORE_PRODUCTS[0]", "STORE_PRODUCTS.find(p => p.handle === window.KAVITA_HANDLE) || STORE_PRODUCTS.find(p => p.id === idParam) || STORE_PRODUCTS[0]")
 if name=='product':
  modal=re.search(r'  <div class="modal-overlay" id="bookingModal".*?(?=  <!-- =+\n       16\.)',(root/'index.html').read_text(),re.S)[0]
  body+=modal
 body=links(body)
 body=re.sub(r'(["\'])assets/([\w.-]+)',lambda m:m[1]+"{{ '"+m[2]+"' | asset_url }}",body)
 # Inline dynamic image URLs from catalogue are normalized by commerce adapter.
 styles+="\n{{ 'parity-storefront-refinements.css' | asset_url | stylesheet_tag }}\n{{ 'parity-category-grid.css' | asset_url | stylesheet_tag }}\n{{ 'parity-integration.css' | asset_url | stylesheet_tag }}\n"
 body+='\n<script src="{{ \'parity-ui.js\' | asset_url }}"></script><script src="{{ \'parity-page.js\' | asset_url }}"></script>'
 (r/'sections'/('parity-'+name+'.liquid')).write_text(styles+body+'\n{% schema %}\n'+json.dumps({'name':'Preview '+name,'settings':[]})+'\n{% endschema %}')
 template={'layout':'parity','sections':{'main':{'type':'parity-'+name,'settings':{}}},'order':['main']}
 targets={'index':['index.json'],'collections':['collection.json','search.json'],'product':['product.json','product.service.json'],'cart':['cart.json'],'contact':['page.contact.json'],'about':['index.about.json','page.about.json'],'faq':['index.faq.json','page.faq.json'],'consultations':['index.consultations.json','page.book-online.json'],'packages':['index.packages.json','page.packages.json','page.signature-packages.json']}[name]
 for t in targets:(r/'templates'/t).write_text(json.dumps(template,indent=2))
print('Built eight preview-matched Shopify templates')
