/* ==========================================================================
   VANI KABIR STUDIO × MANTRAMM × KAVITA TAROT
   Shared Storefront Catalog & Cart Engine (Persistent across all pages)
   ========================================================================== */

const STORE_PRODUCTS = [
  {
    id: 1,
    handle: "7-chakra-radiance-bracelet",
    title: "7 Chakra Radiance Healing Energy Bracelet",
    category: "bracelets",
    categoryLabel: "Crystal Bracelet",
    intention: "chakra peace",
    price: 899,
    comparePrice: 1899,
    discount: "52% OFF",
    rating: 4.9,
    reviewsCount: 482,
    badge: "Bestseller #1",
    img: "https://images.unsplash.com/photo-1611591475870-85f8c85775c9?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1611591475870-85f8c85775c9?auto=format&fit=crop&w=700&q=80",
      "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=700&q=80",
      "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Expertly strung with natural Amethyst, Lapis Lazuli, Blue Turquoise, Green Aventurine, Tiger Eye, Carnelian, and Red Jasper beads. Consecrated to balance and harmonize all seven primary energy chakras.",
    sacredSignificance: "Aligns your core pranic centers from Muladhara (Root) to Sahasrara (Crown), clearing emotional stagnation, stress, and anxiety.",
    howToWear: "Wear on your non-dominant wrist (left wrist for receiving healing energy) on Thursday morning after bathing and chanting 'Om Namah Shivaya'.",
    benefits: [
      "Balances 7 body chakras and awakens intuitive flow",
      "Shields your personal aura against psychic drainage",
      "Durable elastic silicone cord fits all wrist sizes (16-19cm)"
    ]
  },
  {
    id: 2,
    handle: "original-5-mukhi-nepali-rudraksha-mala",
    title: "Original 5 Mukhi Nepali Rudraksha Mala (108+1)",
    category: "rudraksha",
    categoryLabel: "Nepali Rudraksha",
    intention: "peace shani",
    price: 1299,
    comparePrice: 2599,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 614,
    badge: "Varanasi Consecrated",
    img: "https://images.unsplash.com/photo-1609710228159-0fa9bd7c0827?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1609710228159-0fa9bd7c0827?auto=format&fit=crop&w=700&q=80",
      "https://images.unsplash.com/photo-1596704017254-9b121068fb31?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Directly sourced from Nepal high altitude forests and consecrated at the sanctum of Lord Shiva in Kashi. Each bead displays authentic 5 mukhi clefts and is knotted by hand with a sacred crimson silk tassel.",
    sacredSignificance: "Lord Kalagni Rudra form of Shiva. Brings mental peace, overcomes fear of mortality, and purifies karmic debts.",
    howToWear: "Best worn on Mondays during Brahma Muhurat after touching to a Shiva Lingam or washing with raw milk and Gangajal.",
    benefits: [
      "Regulates bio-electric flow, calming high blood pressure",
      "Shields travelers and seekers from accidental negative energy",
      "Comes with individual ISO 9001 certified testing report & QR"
    ]
  },
  {
    id: 3,
    handle: "7-running-horses-natural-pyrite-frame",
    title: "7 Running Horses Natural Pyrite Wealth Frame",
    category: "vastu",
    categoryLabel: "Vastu & Pyrite Frame",
    intention: "dhanlabh career",
    price: 2499,
    comparePrice: 4999,
    discount: "50% OFF",
    rating: 5.0,
    reviewsCount: 520,
    badge: "Vastu #1 Flagship",
    img: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=700&q=80",
      "https://images.unsplash.com/photo-1602173574767-37ac01994b2a?auto=format&fit=crop&w=700&q=80"
    ],
    description: "The #1 Vastu remedy for rapid commercial expansion, career promotions, and financial momentum. Inlaid with genuine natural shimmering golden pyrite minerals representing the seven solar horses of Surya Dev.",
    sacredSignificance: "The 7 Galloping Horses symbolize speed, triumph, and unstoppable progress in business and professional life according to Vastu Shastra.",
    howToWear: "Mount on the North wall (Kuber direction) or East wall (Surya direction) of your living room, main hallway, or executive cabin.",
    benefits: [
      "Activates stagnant financial flow and commercial luck",
      "Handcrafted with genuine metallic-luster golden Pyrite clusters",
      "Includes free directional Vastu placement guidelines chart"
    ]
  },
  {
    id: 4,
    handle: "24k-gold-plated-shree-yantra",
    title: "24K Gold Plated Maha Meru Shree Yantra Plate",
    category: "yantras",
    categoryLabel: "Energized Yantra",
    intention: "dhanlabh",
    price: 1499,
    comparePrice: 2999,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 340,
    badge: "Vedic Geometry",
    img: "https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1567225557594-88d73e55f2cb?auto=format&fit=crop&w=700&q=80"
    ],
    description: "The supreme mother of all sacred Vedic geometry! Precision-etched over solid heavy brass and dipped in 24K pure gold, consecrated with Sri Suktam and Lakshmi mantras.",
    sacredSignificance: "Represents the cosmic form of Tripurasundari and Mahalakshmi, dissolving poverty and Vastu imbalances.",
    howToWear: "Place on a red silk cloth facing East in your home pooja mandir, business cash locker, or front office.",
    benefits: [
      "Draws prosperous vibrations and abundance into the household",
      "Cures structural Vastu doshas without demolition",
      "Pran Pratishtha energized by certified Varanasi Acharyas"
    ]
  },
  {
    id: 5,
    handle: "raw-natural-pyrite-stone-cluster",
    title: "Raw Natural Pyrite Stone Cluster (150-200g)",
    category: "crystals",
    categoryLabel: "Raw Mineral Cluster",
    intention: "dhanlabh career",
    price: 999,
    comparePrice: 1999,
    discount: "50% OFF",
    rating: 4.8,
    reviewsCount: 298,
    badge: "Money Magnet",
    img: "https://images.unsplash.com/photo-1602173574767-37ac01994b2a?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1602173574767-37ac01994b2a?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Known since ancient times as 'The Fool's Gold' for its brilliant golden metallic crystallization. Pyrite carries strong solar masculine energy that ignites confidence and wealth manifestation.",
    sacredSignificance: "A premier wealth stone in crystal therapy that stimulates the Solar Plexus chakra.",
    howToWear: "Place on your desk, near cash registers, or inside your safe to protect your wealth from envy.",
    benefits: [
      "Shields against energy vampires and financial envy",
      "Enhances willpower, focus, and business decisions",
      "100% natural, uncut, authentic geological specimen"
    ]
  },
  {
    id: 6,
    handle: "triple-protection-bracelet",
    title: "Triple Protection Bracelet (Tiger Eye + Obsidian + Hematite)",
    category: "bracelets",
    categoryLabel: "Crystal Bracelet",
    intention: "protection",
    price: 1199,
    comparePrice: 2399,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 412,
    badge: "Evil Eye Shield",
    img: "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=700&q=80"
    ],
    description: "The ultimate energetic bodyguard! Combines Golden Tiger Eye for willpower, volcanic Black Obsidian for psychic defense, and metallic Hematite for grounded stability.",
    sacredSignificance: "Forms an impenetrable shield around your subtle aura against Buri Nazar (Evil Eye), jealousy, and psychic fatigue.",
    howToWear: "Wear on the right wrist for protection and action, or left wrist to release internal anxiety.",
    benefits: [
      "Neutralizes envious gazes and malicious thoughts",
      "Grounds scattered thinking and eliminates fear",
      "Comfortable polished 8mm natural gemstone beads"
    ]
  },
  {
    id: 7,
    handle: "raw-black-tourmaline-pendant",
    title: "Raw Black Tourmaline Negative Energy Shield Pendant",
    category: "crystals",
    categoryLabel: "Aura Protection",
    intention: "protection",
    price: 799,
    comparePrice: 1599,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 285,
    badge: "Nazar Shield",
    img: "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Natural jet-black raw Schorl Tourmaline set in a sacred silver-finish casing. Renowned for its electrostatic property that transmutes heavy negative frequencies into positive energy.",
    sacredSignificance: "The master stone for psychic boundaries and protection against environmental EMF stress.",
    howToWear: "Wear close to the heart or throat on a black thread or silver chain.",
    benefits: [
      "Absorbs heavy vibrations from toxic environments",
      "Provides grounding for sensitive souls and empaths",
      "Consecrated with Hanuman Chalisa and protection mantras"
    ]
  },
  {
    id: 8,
    handle: "green-jade-abundance-bracelet",
    title: "Natural Green Jade Abundance & Good Fortune Bracelet",
    category: "bracelets",
    categoryLabel: "Crystal Bracelet",
    intention: "dhanlabh love",
    price: 1099,
    comparePrice: 2199,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 310,
    badge: "Heart Chakra",
    img: "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Hand-selected translucent Green Jade gemstone beads representing timeless luck, financial wisdom, and Anahata (Heart Chakra) balance.",
    sacredSignificance: "Revered across Vedic and oriental traditions as the stone of harmony, prosperity, and emotional healing.",
    howToWear: "Wear on the left wrist to attract blessings of good fortune and peace.",
    benefits: [
      "Soothes the autonomic nervous system and relieves stress",
      "Encourages wise financial investments and savings",
      "Heals emotional grief and invites deep, loyal friendships"
    ]
  },
  {
    id: 9,
    handle: "original-7-mukhi-nepali-rudraksha",
    title: "Original 7 Mukhi Nepali Rudraksha with Silver Capping",
    category: "rudraksha",
    categoryLabel: "Rare Nepali Bead",
    intention: "dhanlabh shani",
    price: 2199,
    comparePrice: 4399,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 194,
    badge: "Mahalakshmi Swaroop",
    img: "https://images.unsplash.com/photo-1596704017254-9b121068fb31?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1596704017254-9b121068fb31?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Certified collector-grade Nepali 7 Mukhi Rudraksha capped in pure silver. Blessed by the Seven Saptarishis and Goddess Mahalakshmi, governed astrologically by Planet Saturn (Shani).",
    sacredSignificance: "Overcomes Sade Sati and Saturn-related obstacles while opening sudden financial avenues.",
    howToWear: "Wear around the neck or right arm on a Friday or Saturday morning.",
    benefits: [
      "Removes severe financial blockages and chronic liabilities",
      "Alleviates Shani Dosh, Rahu affliction, and mental despair",
      "Includes government-approved laboratory certificate"
    ]
  },
  {
    id: 10,
    handle: "natural-orgone-sri-yantra-pyramid",
    title: "Natural Orgone Sri Yantra Copper Coil Pyramid",
    category: "pyramids",
    categoryLabel: "Energy Pyramid",
    intention: "peace dhanlabh",
    price: 1350,
    comparePrice: 2700,
    discount: "50% OFF",
    rating: 4.8,
    reviewsCount: 226,
    badge: "Orgone Transmuter",
    img: "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Handcrafted orgonite matrix featuring copper spiral coils, natural clear quartz crystal points, and a gold-plated Sri Yantra apex to continuously purify ambient pranic flow.",
    sacredSignificance: "Transmutes stagnant dead orgone (DOR) into positive living orgone (POR), clearing room fatigue.",
    howToWear: "Place on work desks near Wi-Fi routers, monitors, or next to bedside tables.",
    benefits: [
      "Harmonizes electromagnetic smog from digital screens",
      "Enhances deep sleep, vivid dreaming, and lucid meditation",
      "Creates an auspicious sacred aura in any room"
    ]
  },
  {
    id: 11,
    handle: "brazilian-amethyst-calming-tower",
    title: "Raw Deep Purple Brazilian Amethyst Calming Tower",
    category: "crystals",
    categoryLabel: "Healing Quartz",
    intention: "peace",
    price: 1150,
    comparePrice: 2300,
    discount: "50% OFF",
    rating: 5.0,
    reviewsCount: 378,
    badge: "Third Eye Chakra",
    img: "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Genuine high-grade deep violet Brazilian Amethyst crystal obelisk tower. Directs positive energy upwards while absorbing mental anxiety and overthinking.",
    sacredSignificance: "Activates Ajna (Third Eye) and Sahasrara (Crown) chakras for intuitive awakening and quiet contemplation.",
    howToWear: "Keep on nightstands, meditation mats, or bookshelves.",
    benefits: [
      "Extinguishes racing thoughts, insomnia, and restlessness",
      "Fosters high spiritual discernment and emotional equilibrium",
      "Self-standing polished point with raw crystal accents"
    ]
  },
  {
    id: 12,
    handle: "original-vrindavan-tulsi-kanthi-mala",
    title: "Original Vrindavan Holy Tulsi Wood Kanthi Mala",
    category: "rudraksha",
    categoryLabel: "Sacred Japa Mala",
    intention: "peace love",
    price: 599,
    comparePrice: 1199,
    discount: "50% OFF",
    rating: 4.9,
    reviewsCount: 532,
    badge: "Vrindavan Dham",
    img: "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=700&q=80",
    images: [
      "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=700&q=80"
    ],
    description: "Carved from sacred Shyama Tulsi wood in the holy pilgrimage shrine of Vrindavan Dham. Emits a natural gentle basil fragrance that centers the wandering mind during japa meditation.",
    sacredSignificance: "Beloved by Lord Krishna and Vishnu. Purifies the subtle throat and respiratory system.",
    howToWear: "Wear around the neck close to the throat chakra. Remove during meat consumption or alcohol.",
    benefits: [
      "Brings peace of heart, devotion, and divine serenity",
      "Purifies the speech and throat chakra energy",
      "Traditional two-round or three-round sacred knotting"
    ]
  }
];

// Cart State Management with localStorage
let cart = [];

function loadCart() {
  try {
    const saved = localStorage.getItem('kavita_cart');
    if (saved) cart = JSON.parse(saved);
  } catch (e) {
    cart = [];
  }
  updateCartUI();
}

function saveCart() {
  try {
    localStorage.setItem('kavita_cart', JSON.stringify(cart));
  } catch (e) {}
}

function playSacredChime(freq = 528) {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(0.001, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.2, ctx.currentTime + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 1.8);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 1.8);
  } catch (e) {}
}

function addToCart(name, price, img, handle) {
  playSacredChime(639);
  const existing = cart.find(i => i.name === name);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ name, price, qty: 1, img: img || '', handle: handle || '' });
  }
  saveCart();
  updateCartUI();
  openCart();
}

function changeQty(index, delta) {
  if (cart[index]) {
    cart[index].qty += delta;
    if (cart[index].qty <= 0) cart.splice(index, 1);
  }
  saveCart();
  updateCartUI();
}

function removeFromCart(index) {
  cart.splice(index, 1);
  saveCart();
  updateCartUI();
}

function updateCartUI() {
  const countEls = document.querySelectorAll('#cartCount, #cartCountHeader');
  const totalItems = cart.reduce((acc, i) => acc + i.qty, 0);
  const subtotal = cart.reduce((acc, i) => acc + (i.price * i.qty), 0);

  countEls.forEach(el => { if (el) el.innerText = totalItems; });

  const subtotalEl = document.getElementById('cartSubtotal');
  if (subtotalEl) subtotalEl.innerText = '₹' + subtotal.toLocaleString('en-IN');

  const shippingText = document.getElementById('shippingProgressText');
  const shippingFill = document.getElementById('shippingProgressFill');
  if (shippingText && shippingFill) {
    if (subtotal >= 999) {
      shippingText.innerHTML = '🎉 <b>CONGRATULATIONS!</b> You unlocked FREE Express Shipping!';
      shippingFill.style.width = '100%';
    } else {
      const remaining = 999 - subtotal;
      const pct = Math.min(100, Math.round((subtotal / 999) * 100));
      shippingText.innerHTML = `✦ Add <b>₹${remaining}</b> more for FREE Express Delivery!`;
      shippingFill.style.width = pct + '%';
    }
  }

  const itemsListEl = document.getElementById('cartItemsList');
  if (itemsListEl) {
    if (cart.length === 0) {
      itemsListEl.innerHTML = `
        <div style="text-align: center; color: var(--v-text-muted); padding: 3.5rem 1rem;">
          <div style="font-size: 3rem; margin-bottom: 1rem; color: var(--v-maroon);">📿</div>
          <p style="font-weight: 700; color: var(--v-text-dark); font-size: 1.1rem;">Your Sacred Cart is Empty</p>
          <p style="font-size: 0.88rem; margin-top: 0.5rem;">Explore authentic energized Rudraksha and crystals.</p>
          <a href="collections.html" class="btn btn-maroon" style="margin-top: 1.5rem; font-size: 0.82rem; padding: 0.6rem 1.4rem;">
            Explore Collections
          </a>
        </div>
      `;
    } else {
      itemsListEl.innerHTML = cart.map((item, index) => `
        <div class="cart-item-row">
          <img class="cart-item-img" src="${item.img}" alt="${item.name}">
          <div class="cart-item-info">
            <div class="cart-item-title">${item.name}</div>
            <div class="cart-item-price">₹${(item.price * item.qty).toLocaleString('en-IN')}</div>
            <div class="cart-qty-ctrl">
              <button class="qty-btn" onclick="changeQty(${index}, -1)">−</button>
              <span style="font-size: 0.85rem; font-weight: bold;">${item.qty}</span>
              <button class="qty-btn" onclick="changeQty(${index}, 1)">+</button>
              <button onclick="removeFromCart(${index})" style="background: none; border: none; color: #d32f2f; font-size: 0.75rem; margin-left: 0.8rem; cursor: pointer; font-weight: 600;">Remove</button>
            </div>
          </div>
        </div>
      `).join('');
    }
  }
}

function openCart() {
  const overlay = document.getElementById('cartOverlay');
  const drawer = document.getElementById('cartDrawer');
  if (overlay && drawer) {
    overlay.classList.add('active');
    drawer.classList.add('active');
  }
}

function closeCart() {
  const overlay = document.getElementById('cartOverlay');
  const drawer = document.getElementById('cartDrawer');
  if (overlay && drawer) {
    overlay.classList.remove('active');
    drawer.classList.remove('active');
  }
}

function checkoutCart() {
  if (cart.length === 0) {
    alert('Your cart is empty. Please select an energized item.');
    return;
  }
  const subtotal = cart.reduce((acc, i) => acc + (i.price * i.qty), 0);
  const itemsStr = cart.map(i => `${i.name} (x${i.qty}) - ₹${i.price * i.qty}`).join('%0A');
  const waMsg = `*ORDER ENQUIRY - MANTRAMM × KAVITA*%0A%0A*Items:*%0A${itemsStr}%0A%0A*Total Amount:* ₹${subtotal}%0A%0APlease confirm availability & Cash on Delivery options!`;
  window.open(`https://wa.me/919876543210?text=${waMsg}`, '_blank');
}

// Global alias
window.STORE_PRODUCTS = STORE_PRODUCTS;
window.PRODUCTS_DB = STORE_PRODUCTS;

// Search Modal controls
function openSearchModal() {
  playSacredChime(440);
  const modal = document.getElementById('searchModal');
  if (modal) {
    modal.classList.add('active');
    const input = document.getElementById('searchBoxInput');
    if (input) setTimeout(() => input.focus(), 150);
  }
}

function closeSearchModal() {
  const modal = document.getElementById('searchModal');
  if (modal) modal.classList.remove('active');
}

function handleSearch(query) {
  const container = document.getElementById('searchResultsList');
  if (!container) return;
  if (!query || query.trim().length === 0) {
    container.innerHTML = '';
    return;
  }
  const q = query.toLowerCase();
  const matches = STORE_PRODUCTS.filter(p => 
    p.title.toLowerCase().includes(q) || 
    (p.categoryLabel && p.categoryLabel.toLowerCase().includes(q)) ||
    (p.category && p.category.toLowerCase().includes(q)) ||
    (p.intention && p.intention.toLowerCase().includes(q))
  );
  if (matches.length === 0) {
    container.innerHTML = `<div style="color: var(--v-text-muted); font-size: 0.85rem; padding: 1rem 0;">No spiritual products matching "${query}".</div>`;
    return;
  }
  container.innerHTML = matches.map(p => `
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 0; border-bottom: 1px solid var(--v-border); gap: 1rem;">
      <a href="product.html?id=${p.id}" style="display: flex; align-items: center; gap: 0.8rem; text-decoration: none; color: inherit; flex: 1;">
        <img src="${p.img}" style="width: 44px; height: 44px; border-radius: 8px; object-fit: cover; border: 1px solid var(--v-border);">
        <div>
          <div style="font-size: 0.88rem; color: var(--v-text-dark); font-weight: 700; line-height: 1.3;">${p.title}</div>
          <div style="font-size: 0.78rem; color: var(--v-maroon); font-family: var(--font-heading); font-weight: 700; margin-top: 0.2rem;">₹${p.price.toLocaleString('en-IN')}</div>
        </div>
      </a>
      <div style="display: flex; gap: 0.4rem;">
        <a href="product.html?id=${p.id}" class="btn btn-outline" style="padding: 0.35rem 0.75rem; font-size: 0.75rem;">View</a>
        <button class="btn btn-maroon" style="padding: 0.35rem 0.85rem; font-size: 0.75rem;" onclick="addToCart('${p.title}', ${p.price}, '${p.img}', '${p.handle}'); closeSearchModal();">
          Add
        </button>
      </div>
    </div>
  `).join('');
}

// Quick View Modal
function openQuickView(id) {
  const product = STORE_PRODUCTS.find(p => p.id === id);
  if (!product) return;
  playSacredChime(432);
  const content = `
    <div style="display: flex; gap: 1.8rem; flex-wrap: wrap;">
      <img src="${product.img}" style="width: 240px; height: 240px; object-fit: cover; border-radius: 14px; border: 1px solid var(--v-border);" alt="${product.title}">
      <div style="flex: 1; min-width: 260px;">
        <div style="color: var(--v-gold-dark); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; margin-bottom: 0.3rem;">${product.categoryLabel || product.category}</div>
        <h3 style="font-size: 1.35rem; color: var(--v-text-dark); margin-bottom: 0.5rem; line-height: 1.3;">${product.title}</h3>
        <div style="display: flex; align-items: baseline; gap: 0.8rem; margin-bottom: 1rem;">
          <span style="font-family: var(--font-heading); font-size: 1.45rem; color: var(--v-maroon); font-weight: 800;">₹${product.price.toLocaleString('en-IN')}</span>
          <span style="text-decoration: line-through; color: var(--v-text-muted); font-size: 0.94rem;">₹${product.comparePrice.toLocaleString('en-IN')}</span>
          <span style="color: var(--v-green); background: #E8F8F0; padding: 0.2rem 0.55rem; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">SAVE ${product.discount || '50%'}</span>
        </div>
        <p style="color: #5C544D; font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.2rem;">${product.description}</p>
        <ul style="list-style: none; margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--v-text-dark);">
          ${(product.benefits || []).map(b => `<li style="margin-bottom: 0.35rem;">✦ ${b}</li>`).join('')}
        </ul>
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
          <button class="btn btn-maroon" style="flex: 1; min-width: 160px; padding: 0.75rem 1.4rem;" onclick="addToCart('${product.title}', ${product.price}, '${product.img}', '${product.handle}'); closeQuickView();">
            ✦ Add to Cart
          </button>
          <a href="product.html?id=${product.id}" class="btn btn-outline" style="padding: 0.75rem 1.4rem;">
            Full Details →
          </a>
        </div>
      </div>
    </div>
  `;
  const container = document.getElementById('quickViewContent');
  if (container) container.innerHTML = content;
  const modal = document.getElementById('quickViewModal');
  if (modal) modal.classList.add('active');
}

function closeQuickView() {
  const modal = document.getElementById('quickViewModal');
  if (modal) modal.classList.remove('active');
}

// Global initialization
document.addEventListener('DOMContentLoaded', () => {
  loadCart();
  const openCartBtn = document.getElementById('openCartBtn');
  if (openCartBtn) openCartBtn.addEventListener('click', openCart);
});
