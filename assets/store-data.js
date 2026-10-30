/* ==========================================================================
   KAVITA TAROT READER — OFFICIAL STORE CATALOG & CART ENGINE
   Synchronized directly with https://www.kavitatarotreader.com/
   Verified Services, Genuine Crystal Items & Sacred Decks ONLY
   ========================================================================== */

const STORE_PRODUCTS = [
  /* ------------------------------------------------------------------------
     1. CORE TAROT CONSULTATIONS & READINGS
  ------------------------------------------------------------------------ */
  {
    id: 1,
    handle: "live-audio-call-tarot-reading",
    title: "Live Audio Call Tarot Reading with Kavita",
    category: "readings",
    categoryLabel: "Live Consultation",
    intention: "clarity love career guidance",
    price: 999,
    comparePrice: 1555,
    discount: "Standard & Premium",
    rating: 5.0,
    reviewsCount: 380,
    badge: "Core Service",
    img: "assets/product-live-audio.jpg",
    images: [
      "assets/product-live-audio.jpg",
      "assets/product-situational.jpg",
      "assets/deck-gold-tarot.jpg"
    ],
    description: "A deeply personal live one-on-one audio consultation delivered straight to your WhatsApp. Select duration (10, 20, or 30 mins) and choose Standard (within 3–5 days) or Premium Same-Day delivery. Kavita connects with you live to answer your specific questions on love, career, finances, and life crossroads.",
    sacredSignificance: "Channeled intuitive tarot reading connecting directly to your energetic field for grounded, empowered clarity.",
    howToWear: "Delivered live via WhatsApp audio call at your scheduled time slot. Calendar confirmation provided immediately upon booking.",
    durations: [
      { duration: "10 Minutes", standardPrice: 999, premiumPrice: 1555 },
      { duration: "20 Minutes", standardPrice: 2299, premiumPrice: 3099 },
      { duration: "30 Minutes", standardPrice: 3369, premiumPrice: 4444 }
    ],
    benefits: [
      "Direct 1-on-1 private live audio call with Kavita",
      "Guidance on your specific questions (Love, Career, Decisions)",
      "Energy reading + card interpretation + practical guidance",
      "Choice of Standard or Premium Same-Day booking"
    ]
  },
  {
    id: 2,
    handle: "whatsapp-voice-note-tarot-reading",
    title: "Personalised WhatsApp Voice Note Tarot Reading (2 Questions)",
    category: "readings",
    categoryLabel: "Voice Note Reading",
    intention: "clarity decisions swift guidance",
    price: 451,
    comparePrice: 999,
    discount: "55% OFF",
    rating: 5.0,
    reviewsCount: 520,
    badge: "Swift Guidance",
    img: "assets/product-voice-note.jpg",
    images: [
      "assets/product-voice-note.jpg",
      "assets/deck-moon-oracle.jpg"
    ],
    description: "Need swift, compassionate clarity without scheduling a live call? Submit your 2 core questions. Kavita tunes into your energy, pulls your cards, and delivers a detailed, personalized 5–10 minute voice recording directly to your WhatsApp.",
    sacredSignificance: "Permanent audio recording that you can listen back to whenever you need reassurance and direction.",
    howToWear: "Audio note delivered directly to your WhatsApp number. Standard or urgent same-day turnaround available.",
    benefits: [
      "In-depth 5–10 minute audio recording straight to WhatsApp",
      "Ask your 2 most urgent life questions",
      "Keep and re-listen to your reading whenever needed",
      "Zero call scheduling required — listen at your own convenience"
    ]
  },
  {
    id: 3,
    handle: "situational-tarot-packages",
    title: "Situational Tarot Deep Dive Package",
    category: "readings",
    categoryLabel: "Specialized Reading",
    intention: "love career finances",
    price: 1999,
    comparePrice: 3499,
    discount: "43% OFF",
    rating: 4.9,
    reviewsCount: 215,
    badge: "Specialized Deep-Dive",
    img: "assets/product-situational.jpg",
    images: [
      "assets/product-situational.jpg",
      "assets/deck-gold-tarot.jpg"
    ],
    description: "Curated for complex situations: toxic relationship crossroads, business/career shifts, family dynamics, or financial decisions. Comprehensive spread uncovering root causes, hidden influences, and recommended steps forward.",
    sacredSignificance: "Holistic situational analysis aligning karmic patterns, personal desires, and optimal timing.",
    howToWear: "Conducted via detailed audio consultation with full photographic summary of all cards drawn.",
    benefits: [
      "Tailored spread designed around your unique life dilemma",
      "Identifies hidden energetic blocks and external influences",
      "Includes concrete action steps and spiritual remedies"
    ]
  },

  /* ------------------------------------------------------------------------
     2. HEALING & ENERGY SESSIONS
  ------------------------------------------------------------------------ */
  {
    id: 4,
    handle: "distance-cord-cutting-healing",
    title: "Distance Cord-Cutting Healing Session",
    category: "healings",
    categoryLabel: "Energy Healing",
    intention: "protection healing emotional release",
    price: 2499,
    comparePrice: 3999,
    discount: "38% OFF",
    rating: 5.0,
    reviewsCount: 194,
    badge: "Emotional Freedom",
    img: "assets/product-cord-cutting.jpg",
    images: [
      "assets/product-cord-cutting.jpg",
      "assets/crystal-selenite-wand.jpg"
    ],
    description: "A powerful distance energy healing session designed to energetically detach negative emotional ties, past relationship residue, toxic patterns, and psychic drains, freeing your vital energy and restoring peace.",
    sacredSignificance: "Severs ethereal cords connecting you to past lovers, toxic workplaces, or draining friendships while preserving genuine unconditional love.",
    howToWear: "Conducted remotely by Kavita while you relax. Includes pre-session intention alignment and post-healing voice note update.",
    benefits: [
      "Releases lingering emotional baggage and obsessive thoughts",
      "Clears heavy aura blockages and restores vitality",
      "Includes aura shielding ritual to protect your newly cleared field"
    ]
  },
  {
    id: 5,
    handle: "vortex-of-blessings-session",
    title: "Vortex of Blessings — Coded Energy Circle",
    category: "healings",
    categoryLabel: "Energy Circle",
    intention: "dhanlabh peace positivity abundance",
    price: 3100,
    comparePrice: 4500,
    discount: "31% OFF",
    rating: 5.0,
    reviewsCount: 167,
    badge: "High Vibrational",
    img: "assets/product-vortex-blessings.jpg",
    images: [
      "assets/product-vortex-blessings.jpg",
      "assets/crystal-amethyst.jpg"
    ],
    description: "A specialized, coded energy circle session channeled to open stagnant pathways, inviting high-frequency blessings, auspiciousness, peace, and abundance into your life and home.",
    sacredSignificance: "Harnesses sacred celestial alignments and focused vibrational intention to uplift your personal frequency.",
    howToWear: "Remote session accompanied by consecrated sacred symbol and personalized reflection guidance.",
    benefits: [
      "Uplifts personal and household vibrational frequency",
      "Attracts synchronous opportunities and supportive people",
      "Calms chaotic life circumstances and chronic anxiety"
    ]
  },
  {
    id: 6,
    handle: "lamafera-ancient-energy-healing",
    title: "Lamafera Ancient Tibetan Energy Healing",
    category: "healings",
    categoryLabel: "Sacred Healing",
    intention: "protection healing spiritual alignment",
    price: 3500,
    comparePrice: 5500,
    discount: "36% OFF",
    rating: 5.0,
    reviewsCount: 142,
    badge: "Ancient Modality",
    img: "assets/product-lamafera.jpg",
    images: [
      "assets/product-lamafera.jpg",
      "assets/crystal-chakra-bracelet.jpg"
    ],
    description: "An ancient Tibetan energy-healing modality practiced for centuries by Buddhist monks. Clears deep-seated karmic blockages, negative vibrations, fear patterns, and heavy spiritual fatigue with sacred symbols.",
    sacredSignificance: "One of the fastest and most potent spiritual healing systems, channeling high-frequency Universal life force directly into your chakras.",
    howToWear: "Remote master healing session. Requires client to be in a quiet space during the ritual time.",
    benefits: [
      "Eradicates deep rooted subconscious stress and phobias",
      "Neutralizes heavy negative environmental vibrations",
      "Restores natural energetic alignment and spiritual clarity"
    ]
  },

  /* ------------------------------------------------------------------------
     3. CURATED HEALING CRYSTALS (FROM KAVITA'S OFFICIAL SHOP)
  ------------------------------------------------------------------------ */
  {
    id: 7,
    handle: "natural-golden-pyrite-wealth-cluster",
    title: "Natural Golden Pyrite Wealth & Abundance Cluster",
    category: "crystals",
    categoryLabel: "Healing Crystal",
    intention: "dhanlabh career abundance",
    price: 1499,
    comparePrice: 2899,
    discount: "48% OFF",
    rating: 4.9,
    reviewsCount: 310,
    badge: "Wealth Magnet",
    img: "assets/crystal-pyrite.jpg",
    images: [
      "assets/crystal-pyrite.jpg",
      "assets/crystal-amethyst.jpg"
    ],
    description: "Genuine high-grade golden metallic Pyrite cluster, personally selected and spiritually cleansed. Known as 'Fool's Gold' but celebrated as a master stone of prosperity, career success, and solar energy.",
    sacredSignificance: "Resonates with the Solar Plexus Chakra (Manipura), amplifying willpower, financial confidence, and overcoming scarcity mindset.",
    howToWear: "Place on your work desk, home study, or North/East zone of your office to channel steady wealth opportunities.",
    benefits: [
      "100% natural, ethically sourced golden mineral cluster",
      "Shields workplace from toxic professional envy and energy vampires",
      "Spiritually cleansed and energized by Kavita before dispatch"
    ]
  },
  {
    id: 8,
    handle: "raw-amethyst-calming-intuition-cluster",
    title: "Natural Raw Amethyst Calming & Third-Eye Cluster",
    category: "crystals",
    categoryLabel: "Healing Crystal",
    intention: "peace intuition clarity",
    price: 1299,
    comparePrice: 2499,
    discount: "48% OFF",
    rating: 4.9,
    reviewsCount: 248,
    badge: "Intuition & Calm",
    img: "assets/crystal-amethyst.jpg",
    images: [
      "assets/crystal-amethyst.jpg",
      "assets/crystal-pyrite.jpg"
    ],
    description: "Deep purple natural Uruguayan Amethyst specimen. Known as the stone of peace, emotional grounding, and psychic awakening. Excellent companion for tarot reading desks and meditation altars.",
    sacredSignificance: "Opens the Third Eye (Ajna) and Crown (Sahasrara) chakras, calming overactive minds and easing insomnia.",
    howToWear: "Place beside your bedside table, meditation corner, or tarot table for serene mental tranquility.",
    benefits: [
      "Deepens intuition and improves dream recall",
      "Relieves daily mental stress and chronic overthinking",
      "Beautiful raw violet crystalline structure"
    ]
  },
  {
    id: 9,
    handle: "7-chakra-radiance-bracelet",
    title: "7 Chakra Radiance Healing Energy Bracelet",
    category: "crystals",
    categoryLabel: "Crystal Bracelet",
    intention: "chakra peace protection",
    price: 899,
    comparePrice: 1899,
    discount: "52% OFF",
    rating: 4.9,
    reviewsCount: 482,
    badge: "Bestseller #1",
    img: "assets/crystal-chakra-bracelet.jpg",
    images: [
      "assets/crystal-chakra-bracelet.jpg",
      "assets/crystal-amethyst.jpg"
    ],
    description: "Strung with natural Amethyst, Lapis Lazuli, Blue Turquoise, Green Aventurine, Tiger Eye, Carnelian, and Red Jasper beads. Consecrated to balance and harmonize all seven primary energy chakras.",
    sacredSignificance: "Aligns your core pranic centers from Muladhara to Sahasrara, clearing emotional stagnation.",
    howToWear: "Wear on your non-dominant (left) wrist for receiving healing energy throughout your day.",
    benefits: [
      "Balances 7 body chakras and awakens intuitive flow",
      "Shields your personal aura against psychic drainage",
      "Durable elastic silicone cord fits all wrist sizes (16-19cm)"
    ]
  },
  {
    id: 10,
    handle: "moroccan-selenite-cleansing-wand",
    title: "Raw Moroccan Selenite Crystal Energy Cleansing Wand",
    category: "crystals",
    categoryLabel: "Healing Crystal",
    intention: "cleansing protection",
    price: 699,
    comparePrice: 1299,
    discount: "46% OFF",
    rating: 5.0,
    reviewsCount: 175,
    badge: "Aura Cleanser",
    img: "assets/crystal-selenite-wand.jpg",
    images: [
      "assets/crystal-selenite-wand.jpg",
      "assets/crystal-pyrite.jpg"
    ],
    description: "Luminous white fibrous Selenite wand from Morocco. Selenite is self-cleansing and cleanses other stones, tarot cards, and personal auras simply by being near them.",
    sacredSignificance: "Connected to Moon energy and Archangel Michael. Clears stagnant psychic debris.",
    howToWear: "Wave gently across your body from head to toe to sweep away stagnant energy, or rest your tarot deck on top of it.",
    benefits: [
      "Instant energetic eraser for tarot cards and crystals",
      "Purifies bedroom and living room atmospheric energy",
      "Never requires physical cleansing itself"
    ]
  },

  /* ------------------------------------------------------------------------
     4. SACRED TAROT & ORACLE CARDS
  ------------------------------------------------------------------------ */
  {
    id: 11,
    handle: "sacred-gold-foil-major-arcana-deck",
    title: "Sacred Gold-Foil Tarot Deck (Major & Minor Arcana)",
    category: "tarot",
    categoryLabel: "Tarot Deck",
    intention: "guidance divination",
    price: 1899,
    comparePrice: 3200,
    discount: "40% OFF",
    rating: 5.0,
    reviewsCount: 228,
    badge: "Luxury Deck",
    img: "assets/deck-gold-tarot.jpg",
    images: [
      "assets/deck-gold-tarot.jpg",
      "assets/product-situational.jpg"
    ],
    description: "Premium 78-card tarot deck crafted with shimmering gold-foil detailing on velvety matte black cardstock. Designed for deep intuitive resonance, crisp shuffling, and lifelong spiritual companionship.",
    sacredSignificance: "Based on classic esoteric symbolism with elevated contemporary celestial aesthetics.",
    howToWear: "Store in a silk pouch or wooden altar box. Cleanse with sage or selenite before your first reading.",
    benefits: [
      "Complete 78-card set (22 Major Arcana + 56 Minor Arcana)",
      "High-durability 350gsm linen-finish cardstock with gilded edges",
      "Accompanied by a guidebook explaining upright and reversed card meanings"
    ]
  },
  {
    id: 12,
    handle: "celestial-moon-intuition-oracle-cards",
    title: "Celestial Moon & Intuition Oracle Cards (44 Cards)",
    category: "tarot",
    categoryLabel: "Oracle Deck",
    intention: "intuition daily guidance",
    price: 1499,
    comparePrice: 2600,
    discount: "42% OFF",
    rating: 4.9,
    reviewsCount: 164,
    badge: "Intuitive Guidance",
    img: "assets/deck-moon-oracle.jpg",
    images: [
      "assets/deck-moon-oracle.jpg",
      "assets/product-voice-note.jpg"
    ],
    description: "A gentle, uplifting 44-card oracle deck focusing on lunar cycles, soul archetypes, and heart-centered affirmations. Ideal for daily one-card pulls, morning intentions, and evening reflection.",
    sacredSignificance: "Attunes your daily rhythm with natural moon phases and inner emotional wisdom.",
    howToWear: "Pull one card every morning after waking to set your day's grounding intention.",
    benefits: [
      "44 beautifully illustrated cards with soul affirmations",
      "Easy for beginners and experienced seekers alike",
      "Includes comprehensive companion guidebook"
    ]
  }
];

/* Active Cart State Management (SessionStorage & Event Driven) */
const CartEngine = {
  getCart() {
    try {
      return JSON.parse(sessionStorage.getItem("kavita_cart") || "[]");
    } catch (e) {
      return [];
    }
  },
  setCart(items) {
    sessionStorage.setItem("kavita_cart", JSON.stringify(items));
    this.updateBadges();
    window.dispatchEvent(new CustomEvent("kavita:cart-updated", { detail: { items } }));
  },
  addItem(productId, durationOpt = null, isPremium = false) {
    const p = STORE_PRODUCTS.find(x => x.id === Number(productId));
    if (!p) return;

    let price = p.price;
    let title = p.title;

    if (durationOpt && p.durations) {
      const match = p.durations.find(d => d.duration === durationOpt);
      if (match) {
        price = isPremium ? match.premiumPrice : match.standardPrice;
        title += ` (${durationOpt} - ${isPremium ? 'Premium Same-Day' : 'Standard'})`;
      }
    }

    const cart = this.getCart();
    const existing = cart.find(x => x.id === p.id && x.title === title);
    if (existing) {
      existing.qty += 1;
    } else {
      cart.push({
        id: p.id,
        title: title,
        price: price,
        img: p.img,
        qty: 1
      });
    }

    this.setCart(cart);
  },
  updateBadges() {
    const cart = this.getCart();
    const count = cart.reduce((acc, item) => acc + item.qty, 0);
    const badges = document.querySelectorAll("#cartCount, #kavita-cart-badge, .cart-badge");
    badges.forEach(b => {
      b.textContent = count;
      b.style.display = count > 0 ? "inline-flex" : "none";
    });
  }
};

document.addEventListener("DOMContentLoaded", function() {
  CartEngine.updateBadges();
});
