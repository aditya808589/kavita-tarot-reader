import csv, json, re, html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, 'wix-store-export.csv')

def clean_html(text):
    if not text:
        return ''
    t = re.sub(r'<br\s*/?>', '\n', text)
    t = re.sub(r'</p>', '\n\n', t)
    t = re.sub(r'</li>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()

with open(CSV_PATH, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

dummy_names = ["I'm a product", "Brush Set", "Matte Lipstick", "Face Gloss"]
real_rows = [r for r in rows if r['fieldType'] == 'PRODUCT' and not any(r['name'].strip().startswith(d) for d in dummy_names)]

row_by_handle = {r['handle']: r for r in real_rows}

# Detailed definitions in desired order
catalog_defs = [
  # 1. READINGS & CONSULTATIONS (10 items)
  {
    "handle_key": "Product_6d804ac6-153e-4914-abce-f282a9b2f83d",
    "handle": "10-minutes-call",
    "title": "10 Minutes Live Audio Call Tarot Reading with Kavita",
    "category": "readings",
    "categoryLabel": "Live Audio Consultation",
    "intention": "clarity love career guidance dhanlabh",
    "badge": "Popular Reading",
    "rating": 5.0,
    "reviewsCount": 420,
    "img": "assets/product-call-10min.jpg",
    "images": ["assets/product-call-10min.jpg", "assets/official-reading-menu.jpg"],
    "durations": [
      { "duration": "10 Minutes (3 Questions only)", "standardPrice": 999, "urgentPrice": 1555 },
      { "duration": "20 Minutes", "standardPrice": 2299, "urgentPrice": 3099 },
      { "duration": "30 Minutes", "standardPrice": 3369, "urgentPrice": 4444 }
    ],
    "sacredSignificance": "Direct channeled intuitive guidance connecting into your immediate energetic field for focused answers.",
    "howToWear": "Conducted live 1-on-1 via WhatsApp Audio call. Select your slot upon checkout or connect via WhatsApp immediately.",
    "benefits": [
      "Direct 1-on-1 private live audio call with Kavita",
      "Focused clarity on up to 3 pressing life/love/career questions",
      "Actionable energetic advice and timeline predictions",
      "Choice of Standard or Urgent (Within 24 Hours) booking"
    ]
  },
  {
    "handle_key": "Product_d0e992ef-96de-4322-ae8d-e33d52c9e7e4",
    "handle": "30-minutes-call",
    "title": "30 Minutes Comprehensive Live Audio Call Tarot Reading",
    "category": "readings",
    "categoryLabel": "Live Audio Consultation",
    "intention": "clarity love career guidance protection dhanlabh",
    "badge": "Deep Dive Session",
    "rating": 5.0,
    "reviewsCount": 512,
    "price_override": 3369,
    "compare_price_override": 4444,
    "img": "assets/product-call-30min.jpg",
    "images": ["assets/product-call-30min.jpg", "assets/official-reading-menu.jpg"],
    "durations": [
      { "duration": "20 Minutes", "standardPrice": 2299, "urgentPrice": 3099 },
      { "duration": "30 Minutes", "standardPrice": 3369, "urgentPrice": 4444 }
    ],
    "sacredSignificance": "Full soul-level energetic reading uncovering root causes, relationship dynamics, financial trajectories, and soul missions.",
    "howToWear": "Conducted live 1-on-1 via WhatsApp Audio call. Direct private appointment confirmation provided.",
    "benefits": [
      "30 minutes of deep-dive unrestricted intuitive exploration",
      "Comprehensive spreads for love, marriage, business & personal growth",
      "Root energetic blockage detection & crystal recommendation",
      "Choice of Standard or Urgent (Within 24 Hours) delivery"
    ]
  },
  {
    "handle_key": "manual-video-call",
    "handle": "video-call-tarot-reading",
    "title": "Live Video Call Tarot Reading with Kavita",
    "category": "readings",
    "categoryLabel": "Live Video Consultation",
    "intention": "clarity love career deep-guidance healing",
    "badge": "Face-to-Face Clarity",
    "rating": 5.0,
    "reviewsCount": 388,
    "price_override": 1888,
    "compare_price_override": 2499,
    "img": "assets/product-call-30min.jpg",
    "images": ["assets/product-call-30min.jpg", "assets/official-reading-menu.jpg"],
    "durations": [
      { "duration": "10 Minutes", "standardPrice": 1888, "urgentPrice": 2199 },
      { "duration": "30 Minutes", "standardPrice": 4499, "urgentPrice": 5499 }
    ],
    "description_override": "Face to Face Deeper Clarity: A private, direct 1-on-1 live video consultation with Kavita via WhatsApp Video or Google Meet.\n\n✦ 10 Minutes: Standard Delivery ₹1,888 | Urgent (Within 24 Hrs) ₹2,199\n✦ 30 Minutes: Standard Delivery ₹4,499 | Urgent (Within 24 Hrs) ₹5,499\n\n✦ What You Experience:\n- Direct face-to-face sacred tarot card spread\n- Real-time answers to pressing love, marriage, business or career questions\n- Immediate energetic diagnosis and personalized Vedic remedies\n- Choice of Standard or Urgent (Within 24 Hours) appointment",
    "sacredSignificance": "Direct eye-to-eye intuitive transmission unlocking the deepest layers of your subconscious and energetic field.",
    "howToWear": "Conducted live face-to-face via private WhatsApp Video call or Google Meet. Link & slot scheduled upon booking.",
    "benefits": [
      "Private face-to-face 1-on-1 live session with Kavita",
      "Real-time visual card spread and channeled intuitive interpretation",
      "Detailed energetic guidance for high-stakes decisions",
      "Choice of Standard or Urgent (Within 24 Hrs) priority scheduling"
    ]
  },
  {
    "handle_key": "Product_12888300-3f3e-46a6-914c-898f69ff9b02",
    "handle": "voice-note-1-question",
    "title": "WhatsApp Voice Note Tarot Reading (1 Question)",
    "category": "readings",
    "categoryLabel": "Voice Note Reading",
    "intention": "clarity love quick guidance",
    "badge": "Quick Answer",
    "rating": 4.9,
    "reviewsCount": 284,
    "price_override": 299,
    "compare_price_override": 499,
    "description_override": "Need swift, compassionate clarity without scheduling a live call? Submit your 1 core question. Kavita tunes into your energy, pulls your cards, and delivers a detailed, personalized voice recording directly to your WhatsApp.\n\n✦ 1 Question: ₹299/-\n✦ Delivery: Answer delivered as voice note within 7-10 days.\n✦ Urgent: For urgent readings, connect directly on WhatsApp (+91 93103 87104).",
    "img": "assets/product-voice-1q.jpg",
    "images": ["assets/product-voice-1q.jpg", "assets/official-reading-menu.jpg"],
    "sacredSignificance": "Crisp, channeled audio reading delivered directly to your personal WhatsApp message inbox to listen at your leisure.",
    "howToWear": "Delivered as a high-quality WhatsApp voice note within 7-10 days. For urgent readings, connect directly on WhatsApp (+91 93103 87104).",
    "benefits": [
      "Targeted answer to 1 specific question (₹299)",
      "Answer delivered as voice note in 7-10 days",
      "Urgent same-day option available via WhatsApp",
      "Permanent audio file to re-listen anytime you need clarity"
    ]
  },
  {
    "handle_key": "Product_2e4978b1-fecf-4e00-bfdb-b71bd9657eeb",
    "handle": "voice-note-2-questions",
    "title": "WhatsApp Voice Note Tarot Reading (2 Questions)",
    "category": "readings",
    "categoryLabel": "Voice Note Reading",
    "intention": "clarity love career guidance",
    "badge": "Bestseller",
    "rating": 5.0,
    "reviewsCount": 460,
    "price_override": 399,
    "compare_price_override": 699,
    "description_override": "Need swift, compassionate clarity without scheduling a live call? Submit your 2 core questions. Kavita tunes into your energy, pulls your cards, and delivers a detailed, personalized voice recording directly to your WhatsApp.\n\n✦ 2 Questions: ₹399/-\n✦ Delivery: Answer delivered as voice note within 7-10 days.\n✦ Urgent: For urgent readings, connect directly on WhatsApp (+91 93103 87104).",
    "img": "assets/product-voice-2q.jpg",
    "images": ["assets/product-voice-2q.jpg", "assets/official-reading-menu.jpg"],
    "sacredSignificance": "In-depth double audio transmission exploring interconnected aspects of your query (e.g. current feelings + outcome, or job change + timing).",
    "howToWear": "Delivered as personal WhatsApp audio notes within 7-10 days. For urgent readings, connect on WhatsApp (+91 93103 87104).",
    "benefits": [
      "Comprehensive channeled answers to 2 important questions (₹399)",
      "Answer delivered as voice note in 7-10 days",
      "Urgent same-day option available via WhatsApp",
      "Convenient audio format you keep forever"
    ]
  },
  {
    "handle_key": "Product_8b045676-fe23-48b1-9167-1826b62f4fa1",
    "handle": "voice-note-4-questions",
    "title": "WhatsApp Voice Note Tarot Reading (4 Questions)",
    "category": "readings",
    "categoryLabel": "Voice Note Reading",
    "intention": "clarity love career guidance dhanlabh",
    "badge": "Multi-Topic",
    "rating": 5.0,
    "reviewsCount": 195,
    "img": "assets/product-voice-4q.jpg",
    "images": ["assets/product-voice-4q.jpg", "assets/official-reading-menu.jpg"],
    "sacredSignificance": "Multi-dimensional reading covering four distinct areas of life such as love, career, family, and spiritual evolution.",
    "howToWear": "Delivered via WhatsApp voice message. Send your 4 questions directly after booking.",
    "benefits": [
      "In-depth analysis of 4 distinct questions",
      "Detailed cards breakdown with specific advice",
      "Listen privately at your own pace anytime",
      "Personalized remedies and energetic outlook"
    ]
  },
  {
    "handle_key": "Product_383e5be0-88ec-4d45-95cf-1ce0be4b8dd8",
    "handle": "voice-note-5-questions-angel-guidance",
    "title": "Voice Note (5 Questions) + Angelic Guidance",
    "category": "readings",
    "categoryLabel": "Voice Note Reading",
    "intention": "clarity love career protection angel guidance",
    "badge": "Complete Reading",
    "rating": 5.0,
    "reviewsCount": 310,
    "img": "assets/product-voice-5q.jpg",
    "images": ["assets/product-voice-5q.jpg", "assets/official-reading-menu.jpg"],
    "sacredSignificance": "Extensive reading answering 5 key queries combined with a divine Angel Oracle blessing transmission.",
    "howToWear": "Delivered to your WhatsApp as detailed audio messages along with angel card photo.",
    "benefits": [
      "5 in-depth question readings covering all life aspects",
      "Bonus channeled Angel Card guidance & protection message",
      "Practical timelines and affirmative steps",
      "High spiritual accuracy and emotional relief"
    ]
  },
  {
    "handle_key": "Product_c5832491-0560-46a7-bf7f-549f05449c18",
    "handle": "rune-reading",
    "title": "Ancient Nordic Rune Reading Session",
    "category": "readings",
    "categoryLabel": "Sacred Divination",
    "intention": "protection clarity career wisdom",
    "badge": "Sacred Ancient Art",
    "rating": 5.0,
    "reviewsCount": 142,
    "img": "assets/product-rune-reading.jpg",
    "images": ["assets/product-rune-reading.jpg"],
    "sacredSignificance": "Elder Futhark sacred runes cast to reveal fate, destiny alignments, hidden obstacles, and primal elemental currents.",
    "howToWear": "Delivered as a detailed 30-minute consultation or audio report. Submit query upon confirmation.",
    "benefits": [
      "Ancient Elder Futhark rune casting",
      "Deep insight into karmic influences and ancestral path",
      "Clear guidance on decisions requiring resolute strength",
      "Protective runic charms and guidance"
    ]
  },
  {
    "handle_key": "Product_7886c389-510e-4cb9-b9a1-fd646846467c",
    "handle": "personalised-energy-circle",
    "title": "Personalised Sacred Energy Circle",
    "category": "readings",
    "categoryLabel": "Energy Transmission",
    "intention": "dhanlabh peace protection healing",
    "badge": "Transformational",
    "rating": 5.0,
    "reviewsCount": 278,
    "img": "assets/product-energy-circle.jpg",
    "images": ["assets/product-energy-circle.jpg"],
    "sacredSignificance": "Sacred geometric energy circle infused with specific switchwords, sacred numbers, and intention codes designed for your exact goal.",
    "howToWear": "High-resolution energized digital energy circle delivered with detailed activation instructions for phone wallpaper, altar, or printing.",
    "benefits": [
      "Custom channeled for your specific intention (wealth, relationship, health, peace)",
      "Infused with cosmic switchwords & sacred frequencies",
      "Continuous subtle energetic realignment in your space",
      "Includes complete activation ritual guidelines"
    ]
  },
  {
    "handle_key": "Product_e36e273b-d653-4425-9ab1-da949d5e2e39",
    "handle": "career-crystal-bundle",
    "title": "Career Breakthrough Reading + Energized Crystal Bundle",
    "category": "readings",
    "categoryLabel": "Sacred Bundle",
    "intention": "career dhanlabh clarity prosperity",
    "badge": "Complete Breakthrough",
    "rating": 5.0,
    "reviewsCount": 186,
    "img": "assets/product-career-bundle.jpg",
    "images": ["assets/product-career-bundle.jpg"],
    "sacredSignificance": "Synergistic combination of in-depth professional tarot guidance and an authentic energized gemstone to magnetize career success.",
    "howToWear": "Reading delivered via WhatsApp; energized physical crystal shipped securely to your doorstep.",
    "benefits": [
      "Full career, promotion & business tarot reading",
      "Energized natural crystal hand-selected for career elevation",
      "Clear timing on job offers, salary jumps & transitions",
      "Dual benefit of spiritual insight and physical talisman"
    ]
  },
  {
    "handle_key": "Product_81936c8c-09f8-407e-ad23-57bc359f8025",
    "handle": "career-reading-labradorite-bundle",
    "title": "Career Reading + Energized Labradorite Crystal Bundle",
    "category": "readings",
    "categoryLabel": "Sacred Bundle",
    "intention": "career protection clarity dhanlabh",
    "badge": "Bestseller Bundle",
    "rating": 5.0,
    "reviewsCount": 340,
    "img": "assets/product-career-labradorite-bundle.png",
    "images": ["assets/product-career-labradorite-bundle.png"],
    "sacredSignificance": "Labradorite, the stone of magic and perseverance, paired with Kavita's career consultation to unlock professional breakthroughs.",
    "howToWear": "Consultation conducted via WhatsApp; genuine charged Labradorite stone shipped with energization instructions.",
    "benefits": [
      "Targeted career roadmap reading uncovering latent opportunities",
      "Genuine iridescent Labradorite crystal charged with Kavita's mantras",
      "Shields against workplace politics and self-doubt",
      "Amplifies intuition and leadership presence"
    ]
  },
  {
    "handle_key": "manual-cord-cutting",
    "handle": "distance-cord-cutting-healing",
    "title": "Distance Cord-Cutting Healing Session",
    "category": "readings",
    "categoryLabel": "Aura & Karma Cleansing",
    "intention": "protection emotional-release healing karma clarity",
    "badge": "Master Healing",
    "rating": 5.0,
    "reviewsCount": 240,
    "price_override": 5001,
    "compare_price_override": 7500,
    "img": "assets/product-cord-cutting.jpg",
    "images": ["assets/product-cord-cutting.jpg", "assets/official-reading-menu.jpg"],
    "description_override": "A powerful distance energy healing session designed to energetically release toxic attachments, past relationship residue, and psychic draining ties, freeing your vital energy and restoring peace.\n\n✦ Complete Healing Session: ₹5,001/-\n✦ Conducted remotely by Kavita with sacred Vedic beeja mantras & cord severing ritual.\n✦ ⚡ Urgent Voice Note Reading also available (Answer in 24 hrs — ₹499/voice note).\n✦ 100% Confidential & Sacred (Prepaid online booking only — No COD for Readings).",
    "sacredSignificance": "Severs ethereal cords connecting you to past lovers, toxic workplaces, or draining friendships while preserving genuine unconditional love and restoring your personal sovereignty.",
    "howToWear": "Performed remotely via deep meditative energetic channeling by Kavita. Photo confirmation and channeled voice note summary sent to your WhatsApp.",
    "benefits": [
      "Sever toxic etheric attachment cords and energetic drainers",
      "Release lingering past relationship trauma and soul fatigue",
      "Restore aura vibrancy and emotional tranquility",
      "Channeled post-session voice note with energetic diagnosis"
    ]
  },

  # 2. HEALING GEMSTONE BRACELETS (8 items)
  {
    "handle_key": "Product_9e8e86ac-8bbf-4f41-ace0-b0d42bbf0688",
    "handle": "kunzite-bracelet",
    "title": "Kunzite Bracelet – Embrace Love, Peace & Emotional Healing",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "love peace emotional healing",
    "badge": "Premium Gemstone",
    "rating": 5.0,
    "reviewsCount": 215,
    "img": "assets/product-kunzite-bracelet.jpg",
    "images": ["assets/product-kunzite-bracelet.jpg"],
    "sacredSignificance": "Exquisite high-frequency Kunzite crystal radiating divine unconditional love, dispelling emotional grief and opening the heart.",
    "howToWear": "Wear on the left wrist to receive gentle emotional soothing and heart-centered peace throughout the day.",
    "benefits": [
      "Relieves deep emotional stress, heartbreak and anxious thoughts",
      "Opens the heart chakra to give and receive unconditional love",
      "Enhances gentle communication and inner serenity",
      "Handcrafted with genuine natural Kunzite beads"
    ]
  },
  {
    "handle_key": "Product_812aa665-eef2-4342-b741-efa535e36337",
    "handle": "seven-chakra-bracelet",
    "title": "Seven Chakra Natural Stone Energy Alignment Bracelet",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "peace protection harmony healing",
    "badge": "Customer Favorite",
    "rating": 5.0,
    "reviewsCount": 540,
    "img": "assets/product-seven-chakra-bracelet.png",
    "images": ["assets/product-seven-chakra-bracelet.png"],
    "sacredSignificance": "Harmonizes all 7 chakras from Root to Crown, ensuring your aura remains vibrant, aligned, and resilient against fatigue.",
    "howToWear": "Wear daily on either wrist. Cleanse once a month under moonlight or incense smoke to recharge its vitality.",
    "benefits": [
      "Balances all 7 primary energetic centers of the body",
      "Promotes mental clarity, vitality and peaceful focus",
      "Combines genuine Amethyst, Lapis, Turquoise, Aventurine, Tiger Eye, Carnelian & Onyx",
      "Energized and ready to wear out of the box"
    ]
  },
  {
    "handle_key": "Product_9f177a80-8e18-468c-8abe-bc1b9a9cd67e",
    "handle": "pyrite-money-success-bracelet",
    "title": "Pyrite Money & Success Bracelet – Unlock Prosperity! 💰✨",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "dhanlabh career wealth confidence",
    "badge": "Money Magnet",
    "rating": 5.0,
    "reviewsCount": 490,
    "img": "assets/product-pyrite-money-bracelet.jpg",
    "images": ["assets/product-pyrite-money-bracelet.jpg"],
    "sacredSignificance": "Golden Pyrite is the ultimate money stone, igniting the Solar Plexus chakra for unshakeable confidence, sales, and wealth creation.",
    "howToWear": "Wear on your dominant (right) wrist for action, wealth generation, business meetings, and financial manifestation.",
    "benefits": [
      "Attracts unexpected wealth, business growth and financial windfalls",
      "Strengthens willpower, focus, and ambitious goal pursuit",
      "Shields against negative financial drained thoughts",
      "Made with genuine shimmering golden Pyrite beads"
    ]
  },
  {
    "handle_key": "Product_386075a3-4fb4-489d-9048-8536f16ae5b1",
    "handle": "pixiu-money-luck-abundance-bracelet",
    "title": "Pixiu Money Luck & Abundance Bracelet",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "dhanlabh wealth luck prosperity",
    "badge": "Abundance Talisman",
    "rating": 4.9,
    "reviewsCount": 380,
    "img": "assets/product-pixiu-abundance-bracelet.jpg",
    "images": ["assets/product-pixiu-abundance-bracelet.jpg"],
    "sacredSignificance": "Features the sacred mythological Pixiu beast that gathers wealth from all directions and protects the wearer from wealth leakage.",
    "howToWear": "Wear on the left wrist with the Pixiu facing outward to draw wealth into your personal space.",
    "benefits": [
      "Attracts good luck, sudden gains and financial opportunities",
      "Guards accumulated savings and prevents financial loss",
      "Empowers business owners, traders, and ambitious professionals",
      "Charged with ancient prosperity mantras"
    ]
  },
  {
    "handle_key": "Product_c59189b1-657e-4878-80aa-e89b8a635d65",
    "handle": "black-tourmaline-bracelet",
    "title": "Black Tourmaline Bracelet: A Gateway to Protection & Positive Energy",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "protection grounding shani peace",
    "badge": "Psychic Shield",
    "rating": 5.0,
    "reviewsCount": 410,
    "img": "assets/product-black-tourmaline-bracelet.jpg",
    "images": ["assets/product-black-tourmaline-bracelet.jpg"],
    "sacredSignificance": "The premier stone of psychic defense, creating an impenetrable energetic boundary against nazar, negative people, and EMF.",
    "howToWear": "Wear on the left wrist for absorbing and repelling toxic energies in crowded or stressful work environments.",
    "benefits": [
      "Deflects evil eye (nazar), psychic attacks, and draining energies",
      "Provides intense grounding and emotional stability",
      "Clears heavy electromagnetic radiation from computers and phones",
      "100% genuine natural Black Tourmaline beads"
    ]
  },
  {
    "handle_key": "Product_5159fa36-b6bb-4729-b4f3-4915352b396b",
    "handle": "amethyst-clear-quartz-bracelet",
    "title": "Amethyst and Clear Quartz Mixed Harmony Bracelet",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "peace clarity spiritual growth",
    "badge": "Clarity & Calm",
    "rating": 4.9,
    "reviewsCount": 230,
    "img": "assets/product-amethyst-clear-quartz-bracelet.jpg",
    "images": ["assets/product-amethyst-clear-quartz-bracelet.jpg"],
    "sacredSignificance": "Harmonious union of calming Amethyst and amplifying Clear Quartz for deep mental tranquility and heightened spiritual intuition.",
    "howToWear": "Wear on either wrist during meditation, stressful days, or before sleep for peaceful dreams.",
    "benefits": [
      "Soothes overthinking, insomnia and nervous tension",
      "Amplifies personal clarity and decision-making capabilities",
      "Activates the Crown and Third-Eye chakras",
      "Handmade with premium high-clarity natural beads"
    ]
  },
  {
    "handle_key": "Product_ac5433aa-2bf4-4abc-8878-6539184cd03a",
    "handle": "amethyst-clear-rose-quartz-bracelet",
    "title": "Amethyst, Clear Quartz & Rose Quartz Triad Bracelet",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "love peace clarity healing",
    "badge": "Sacred Triad",
    "rating": 5.0,
    "reviewsCount": 315,
    "img": "assets/product-amethyst-clear-rose-bracelet.jpg",
    "images": ["assets/product-amethyst-clear-rose-bracelet.jpg"],
    "sacredSignificance": "The ultimate trinity of self-love, mental peace, and spiritual illumination in a single elegant wristwear piece.",
    "howToWear": "Wear daily on the left wrist to nurture gentle compassion, inner peace, and emotional release.",
    "benefits": [
      "Heals heart chakra wounds and dissolves self-doubt",
      "Calms racing thoughts while promoting self-worth",
      "Blends soft pastel pink, deep purple and crystal-clear luster",
      "Perfect gift for loved ones needing warmth and care"
    ]
  },
  {
    "handle_key": "Product_22e5cdd1-0b70-444a-96f0-319118d6a629",
    "handle": "aventurine-bracelet",
    "title": "Green Aventurine Prosperity & Luck Bracelet",
    "category": "bracelets",
    "categoryLabel": "Healing Gemstone Bracelet",
    "intention": "dhanlabh luck love healing",
    "badge": "Stone of Opportunity",
    "rating": 4.9,
    "reviewsCount": 190,
    "img": "assets/product-aventurine-bracelet.jpg",
    "images": ["assets/product-aventurine-bracelet.jpg"],
    "sacredSignificance": "Known as the Stone of Opportunity, thought to be the luckiest of all crystals for manifesting prosperity and new ventures.",
    "howToWear": "Wear on the left wrist when starting new jobs, signing contracts, or seeking fresh romantic beginnings.",
    "benefits": [
      "Attracts winning energy in competitive endeavors and interviews",
      "Releases old emotional patterns so new growth can occur",
      "Soothes the heart and restores optimism",
      "Smooth polished soothing green aventurine gemstone beads"
    ]
  },

  # 3. SACRED CHARGED RAKHIS (7 items)
  {
    "handle_key": "Product_f86fd72e-a630-4474-95a6-6ee261e390c4",
    "handle": "money-magnet-rakhi-1",
    "title": "Money Magnet Crystal Rakhi (Classic Edition)",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "dhanlabh wealth protection",
    "badge": "Festive Sacred",
    "rating": 5.0,
    "reviewsCount": 310,
    "img": "assets/product-rakhi-money-magnet-1.jpg",
    "images": ["assets/product-rakhi-money-magnet-1.jpg"],
    "sacredSignificance": "Handcrafted sacred thread woven with natural abundance crystals to bless your brother with endless financial prosperity.",
    "howToWear": "Tie on your brother's right wrist during Raksha Bandhan. Can be kept in wallet or altar afterwards as a wealth charm.",
    "benefits": [
      "Infused with wealth-attracting gemstones (Pyrite & Aventurine)",
      "Traditional sacred thread blessed with Vedic prosperity mantras",
      "Keeps brother protected and financially flourishing",
      "Can be repurposed as a sacred wrist charm all year round"
    ]
  },
  {
    "handle_key": "Product_19de4d91-0ea1-416e-a3b2-38b72e67ef21",
    "handle": "money-magnet-rakhi-2",
    "title": "Money Magnet Crystal Rakhi (Golden Aura Edition)",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "dhanlabh wealth career",
    "badge": "Festive Sacred",
    "rating": 5.0,
    "reviewsCount": 280,
    "img": "assets/product-rakhi-money-magnet-2.jpg",
    "images": ["assets/product-rakhi-money-magnet-2.jpg"],
    "sacredSignificance": "Elevated gold-toned finish woven with sparkling genuine prosperity crystals for brother's business success.",
    "howToWear": "Tie on the right wrist with heartfelt prayers for growth, luck, and victory.",
    "benefits": [
      "Enhances brother's career luck and money attraction",
      "Premium silky threads with gold-beaded crystal centerpiece",
      "Consecrated with divine Lakshmi energy",
      "Arrives in special protective sacred packaging"
    ]
  },
  {
    "handle_key": "Product_fbc47d21-a301-4162-8b51-0dcc06d48fbb",
    "handle": "triple-protection-rakhi",
    "title": "Triple Protection Sacred Crystal Rakhi",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "protection peace health shani",
    "badge": "Shield Rakhi",
    "rating": 5.0,
    "reviewsCount": 420,
    "img": "assets/product-rakhi-triple-protection.jpg",
    "images": ["assets/product-rakhi-triple-protection.jpg"],
    "sacredSignificance": "Combines Tiger Eye, Black Obsidian, and Hematite to form an invincible shield guarding your brother against negative energies.",
    "howToWear": "Tie on the right wrist to protect against travel hazards, evil eye, and workplace envy.",
    "benefits": [
      "Triple gemstone combination for total energetic defense",
      "Shields from nazar, psychic negativity, and bad vibes",
      "Grounds your brother's vitality and gives him courage",
      "A meaningful token of lifelong sisterly protection"
    ]
  },
  {
    "handle_key": "Product_07f1ff15-eea8-40b7-90be-c569933ff239",
    "handle": "seven-chakra-rakhi",
    "title": "Seven Chakra Balance & Harmony Crystal Rakhi",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "healing peace protection",
    "badge": "Vitality Rakhi",
    "rating": 5.0,
    "reviewsCount": 260,
    "img": "assets/product-rakhi-seven-chakra.jpg",
    "images": ["assets/product-rakhi-seven-chakra.jpg"],
    "sacredSignificance": "Seven genuine natural gemstones representing the full rainbow spectrum of health, mental calm, and spiritual alignment.",
    "howToWear": "Tie on the right wrist to energize all energy centers and bless your brother with health and vitality.",
    "benefits": [
      "Promotes full-body wellness and emotional balance",
      "Contains seven authentic certified crystal beads",
      "Blessed with peace and long-life mantras",
      "Vibrant sacred design honoring ancient traditions"
    ]
  },
  {
    "handle_key": "Product_8ba7be7e-8283-4882-9c03-30c0017e3f30",
    "handle": "bhai-bhabhi-rudraksha-rakhi",
    "title": "Bhai Bhabhi Sacred Rudraksha Rakhi Pair",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "protection peace love",
    "badge": "Couple Rakhi Pair",
    "rating": 5.0,
    "reviewsCount": 350,
    "img": "assets/product-rakhi-bhai-bhabhi-rudraksha.jpg",
    "images": ["assets/product-rakhi-bhai-bhabhi-rudraksha.jpg"],
    "sacredSignificance": "A sacred duo set featuring genuine Shiva Panchamukhi Rudraksha beads for your brother and a matching Lumba for your Bhabhi.",
    "howToWear": "Tie the Rakhi on your brother's right wrist and the beautiful hanging Lumba on your Bhabhi's bangle/wrist.",
    "benefits": [
      "Blessed with Lord Shiva's divine grace and marital bliss",
      "Includes 1 Bhai Rakhi + 1 elegant designer Bhabhi Lumba",
      "Strengthens family harmony and auspiciousness",
      "Authentic natural Rudraksha beads with intricate detailing"
    ]
  },
  {
    "handle_key": "Product_348e12c4-eb96-4016-bdf0-6287ba45130c",
    "handle": "bhai-bhabhi-money-magnet-rakhi",
    "title": "Bhai Bhabhi Money Magnet Crystal Rakhi Pair",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "dhanlabh wealth love prosperity",
    "badge": "Prosperity Pair",
    "rating": 5.0,
    "reviewsCount": 390,
    "img": "assets/product-rakhi-bhai-bhabhi-money-magnet.jpg",
    "images": ["assets/product-rakhi-bhai-bhabhi-money-magnet.jpg"],
    "sacredSignificance": "A matching prosperity crystal Rakhi and Lumba set crafted to invite joint abundance, financial expansion, and love into their home.",
    "howToWear": "Tie during auspicious Raksha Bandhan muhurta to invite Lakshmi blessings into their household.",
    "benefits": [
      "Dual wealth attraction set for brother and sister-in-law",
      "Features natural wealth-drawing gemstone beads and tassels",
      "Radiates warmth, togetherness, and opulent energy",
      "Comes packaged together with roli-chawal pouch"
    ]
  },
  {
    "handle_key": "Product_c62a073c-8576-4c4d-a0c0-9071ede4b0d0",
    "handle": "triple-protection-bhai-bhabhi-rakhi",
    "title": "Triple Protection Bhai Bhabhi Rakhi Pair",
    "category": "rakhis",
    "categoryLabel": "Sacred Charged Rakhi",
    "intention": "protection peace love health",
    "badge": "Shielding Pair",
    "rating": 5.0,
    "reviewsCount": 290,
    "img": "assets/product-rakhi-bhai-bhabhi-triple-protection.jpg",
    "images": ["assets/product-rakhi-bhai-bhabhi-triple-protection.jpg"],
    "sacredSignificance": "Comprehensive couple protection set weaving Tiger Eye, Obsidian, and Hematite to protect your brother and bhabhi from evil eye.",
    "howToWear": "Tie simultaneously on brother's wrist and bhabhi's wrist with prayers for their unbroken marital joy.",
    "benefits": [
      "Guards the couple against household conflicts and jealousy",
      "Includes brother rakhi and coordinated hanging lumba",
      "Made with genuine protective natural gemstones",
      "Consecrated with protective Kavach energies"
    ]
  },

  # 4. NATURAL CRYSTALS & SACRED CARVINGS
  {
    "handle_key": "manual-meditation-crystal-tumbles",
    "handle": "meditation-crystal-tumbles",
    "title": "Meditation Crystal Tumbles",
    "category": "crystals",
    "categoryLabel": "Healing Crystals & Carvings",
    "intention": "peace clarity protection meditation dhanlabh",
    "badge": "Bestseller · Energy Harmonizer",
    "rating": 5.0,
    "reviewsCount": 285,
    "price_override": 999,
    "compare_price_override": 1888,
    "img": "assets/product-meditation-tumbles.jpg",
    "images": [
      "assets/product-meditation-tumbles.jpg"
    ],
    "description_override": "Immerse your daily spiritual practice with our consecrated Meditation Crystal Tumbles set. Handpicked and polished to tactile perfection, this sacred collection of authentic tumbled stones features Clear Quartz, Amethyst, Rose Quartz, and Citrine—specifically selected to balance the chakras, deepen breathwork, and quiet the racing mind during meditation and prayer.\n\nEach stone is spiritually cleansed with white sage and energized by Kavita with Vedic Beeja mantras before dispatch.\n\nHow to Use:\nHold gently in palm during meditation, place over specific chakras while lying down, or carry in your pocket to sustain an aura of grounded calm throughout the day.",
    "sacredSignificance": "Smooth rounded river-tumbled crystalline vibrations radiating gentle, steady frequencies that release tension, harmonize aura fields, and assist deep inner quietude.",
    "howToWear": "Keep on your personal altar, hold in your left (receptive) palm during japa or mindfulness, or place near your bedside for peaceful sleep.",
    "benefits": [
      "Set of authentic natural polished crystal tumbles",
      "Includes Master Healer Clear Quartz, Amethyst & Rose Quartz",
      "Consecrated with Vedic peace mantras by Kavita",
      "Enhances deep meditation, focus, and stress release",
      "100% Certified authentic natural gemstones"
    ]
  },
  {
    "handle_key": "Product_2202c12d-405a-4dfd-88bb-1c74be051fff",
    "handle": "rose-quartz-small-angel",
    "title": "Rose Quartz Handcrafted Crystal Angel – Guardian of Love & Healing",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "love peace emotional healing",
    "badge": "Sacred Guardian",
    "rating": 5.0,
    "reviewsCount": 380,
    "img": "assets/product-rose-quartz-angel.jpg",
    "images": ["assets/product-rose-quartz-angel.jpg"],
    "sacredSignificance": "Carved from tender translucent Rose Quartz, this angel figurine acts as an emissary of celestial comfort, self-compassion, and gentle peace.",
    "howToWear": "Place on your bedside table, meditation altar, or work desk to anchor constant comforting vibrations.",
    "benefits": [
      "Brings unconditional love and gentle emotional soothing into any space",
      "Deepens connection with personal guardian angels during prayer",
      "Dispels nightmares and fosters peaceful restful sleep",
      "Exquisite hand-carved natural crystal figurine"
    ]
  },
  {
    "handle_key": "Product_5a0e7a99-9c3c-465d-ad19-7c6d8c35c793",
    "handle": "pyrite-golden-energy-booster",
    "title": "Pyrite: The Golden Energy Booster & Wealth Magnet",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "dhanlabh wealth career confidence",
    "badge": "Abundance Booster",
    "rating": 5.0,
    "reviewsCount": 470,
    "img": "assets/product-pyrite-booster.png",
    "images": ["assets/product-pyrite-booster.png"],
    "sacredSignificance": "A glittering powerhouse of raw mineral gold, Pyrite stimulates the intellect, attracts lucrative deals, and overcomes financial scarcity.",
    "howToWear": "Keep on your cash register, office desk, or North-East wealth zone in your living room.",
    "benefits": [
      "Supercharges financial manifestation and lucrative clients",
      "Boosts physical vitality, drive, and focused willpower",
      "Deflects negative corporate politics and competitor jealousy",
      "Natural unheated golden metallic luster"
    ]
  },
  {
    "handle_key": "Product_6474f300-8708-42f7-bf3c-1d4da4941b7a",
    "handle": "citrine-stone-of-joy-abundance",
    "title": "Citrine: The Stone of Joy, Abundance & Success",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "dhanlabh joy career success",
    "badge": "Merchant's Stone",
    "rating": 5.0,
    "reviewsCount": 510,
    "img": "assets/product-citrine.png",
    "images": ["assets/product-citrine.png"],
    "sacredSignificance": "Known across ancient trade routes as the Merchant's Stone, Citrine carries the warm energy of the sun and never holds negative energy.",
    "howToWear": "Place in your purse, cash box, or study room to magnify optimistic ideas and cash flow.",
    "benefits": [
      "Draws constant commercial prosperity and business opportunities",
      "Clears seasonal blues, lethargy, and low self-esteem",
      "Never requires energetic clearing; naturally cleanses nearby stones",
      "Golden amber radiant gemstone specimen"
    ]
  },
  {
    "handle_key": "Product_04ceb900-85e9-4a65-849d-ba42ca3eba17",
    "handle": "clear-quartz-master-healer",
    "title": "Clear Quartz: The Master Healer & Energy Amplifier",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "clarity healing spiritual growth",
    "badge": "Master Healer",
    "rating": 5.0,
    "reviewsCount": 360,
    "img": "assets/product-clear-quartz.jpg",
    "images": ["assets/product-clear-quartz.jpg"],
    "sacredSignificance": "The most versatile and programmable crystal on Earth, capable of amplifying any intention, thought, or crystal placed near it.",
    "howToWear": "Hold during meditation while stating your affirmations, or keep at the center of your sacred grid.",
    "benefits": [
      "Amplifies personal intentions, prayers and manifestation power",
      "Cleanses stagnant auras and mental fog",
      "Enhances memory, psychic intuition and divine communication",
      "High-vibration natural prismatic quartz crystal"
    ]
  },
  {
    "handle_key": "Product_9778bd5c-1b38-445d-821a-63ca6b0f4d90",
    "handle": "sulemani-hakik-shield-stabilizer",
    "title": "Sulemani Hakik: The Sacred Shield & Spiritual Stabilizer",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "protection shani grounding peace",
    "badge": "Nazar Raksha",
    "rating": 5.0,
    "reviewsCount": 430,
    "img": "assets/product-sulemani-hakik.png",
    "images": ["assets/product-sulemani-hakik.png"],
    "sacredSignificance": "Revered in Vedic and Sufi traditions as the ultimate stone of divine protection, neutralizing Saturn malefic effects and evil eye.",
    "howToWear": "Keep in your pocket or home entrance to establish an energetic shield that repels harmful vibrations.",
    "benefits": [
      "Dissolves strong evil eye (buri nazar) and curses",
      "Calms inner turmoil, fears and recurring nightmares",
      "Grounds turbulent emotions and provides mental resilience",
      "Deep natural banded black and smoky agate"
    ]
  },
  {
    "handle_key": "Product_46dd0e0c-5bb8-4c54-a956-865f5ef97c9a",
    "handle": "malachite-transformation-protection",
    "title": "Malachite: The Stone of Transformation & Protection",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "protection love healing emotional peace",
    "badge": "Deep Transformation",
    "rating": 5.0,
    "reviewsCount": 275,
    "img": "assets/product-malachite.png",
    "images": ["assets/product-malachite.png"],
    "sacredSignificance": "With its mesmerizing concentric green bands, Malachite ruthlessly extracts deeply buried emotional blockages and guards against danger.",
    "howToWear": "Hold over the heart chakra while doing release breathwork, or place in living areas to absorb electromagnetic smog.",
    "benefits": [
      "Powerful emotional purge stone that encourages bold positive changes",
      "Shields travelers from physical and psychic mishaps",
      "Absorbs negative radiation and pollutants from home environments",
      "Striking emerald-green banded natural mineral"
    ]
  },
  {
    "handle_key": "Product_22809a45-cf51-4d07-af99-b8df42881adc",
    "handle": "rose-quartz-raw",
    "title": "Rose Quartz Natural Crystal – The Heart Stone",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "love peace emotional healing",
    "badge": "Heart Stone",
    "rating": 4.9,
    "reviewsCount": 420,
    "img": "assets/product-rose-quartz.png",
    "images": ["assets/product-rose-quartz.png"],
    "sacredSignificance": "The quintessence of unconditional love, dissolving feelings of rejection, anger, and grief to restore trusting relationship harmony.",
    "howToWear": "Place in the southwest corner of the bedroom or hold over your chest to awaken self-love.",
    "benefits": [
      "Attracts gentle, supportive romantic and platonic relationships",
      "Heals emotional heartbreak and dissolves resentment",
      "Encourages deep self-forgiveness and inner sweetness",
      "Pure delicate pink natural crystal specimen"
    ]
  },
  {
    "handle_key": "Product_383f8b18-c8ec-4d70-9ce5-7f82c3f084e2",
    "handle": "rose-quartz-stone-of-universal-love",
    "title": "Rose Quartz: The Stone of Universal Love (Large Raw Specimen)",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "love peace harmony healing",
    "badge": "Master Heart Healer",
    "rating": 5.0,
    "reviewsCount": 310,
    "img": "assets/product-rose-quartz-love.png",
    "images": ["assets/product-rose-quartz-love.png"],
    "sacredSignificance": "Substantial natural raw Rose Quartz chunk radiating an omnipresent field of love, compassion, and divine motherly care.",
    "howToWear": "Anchor in the family living area or marital bedroom for continuous aura cleansing and domestic peace.",
    "benefits": [
      "Restores mutual understanding between partners and family members",
      "Fills large living rooms with warm, nurturing frequencies",
      "Soothes hyperactive nerves and restless tension",
      "Generous hand-selected authentic raw crystal specimen"
    ]
  },
  {
    "handle_key": "Product_3f61dd84-cb60-40f1-87e0-e32f862c55ca",
    "handle": "tiger-eye-stone-of-courage",
    "title": "Tiger Eye Crystal – The Stone of Courage & Confidence",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "protection dhanlabh career confidence",
    "badge": "Warrior Stone",
    "rating": 4.9,
    "reviewsCount": 395,
    "img": "assets/product-tiger-eye.png",
    "images": ["assets/product-tiger-eye.png"],
    "sacredSignificance": "Golden-brown chatoyant stone integrating solar and earthly energies for grounded bravery, sharp focus, and practical problem solving.",
    "howToWear": "Keep on your desk or study table when preparing for exams, interviews, or bold negotiations.",
    "benefits": [
      "Dispels fear, self-doubt, and hesitation in vital moments",
      "Sharpens intellectual discernment and strategic planning",
      "Harmonizes solar plexus and root chakras for fearless action",
      "Gorgeous shimmering golden-brown banded chatoyancy"
    ]
  },
  {
    "handle_key": "Product_66c0d427-ac17-4511-bad7-3565f7dc405e",
    "handle": "carnelian-vitality-stone",
    "title": "Carnelian Natural Crystal – The Flame of Vitality & Passion",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "career passion confidence healing",
    "badge": "Creative Fire",
    "rating": 4.9,
    "reviewsCount": 260,
    "img": "assets/product-carnelian.jpg",
    "images": ["assets/product-carnelian.jpg"],
    "sacredSignificance": "Vibrant sunset-orange gemstone that stimulates the sacral chakra, reigniting motivation, artistic inspiration, and sexual vitality.",
    "howToWear": "Place on creative work spaces or wear close to the lower abdomen for an instant surge in drive.",
    "benefits": [
      "Overcomes creative blocks, procrastination, and lack of enthusiasm",
      "Boosts physical endurance and healthy metabolic vitality",
      "Inspires bold public speaking and theatrical expression",
      "Fiery orange-red natural gemstone"
    ]
  },
  {
    "handle_key": "Product_7d567df3-26e2-4fc9-935d-2ef214a2784b",
    "handle": "red-jasper-strength-stability",
    "title": "Red Jasper: Stone of Physical Strength & Stability",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "grounding protection health stability",
    "badge": "Supreme Nurturer",
    "rating": 4.9,
    "reviewsCount": 235,
    "img": "assets/product-red-jasper.jpg",
    "images": ["assets/product-red-jasper.jpg"],
    "sacredSignificance": "Deep terra-cotta red stone connecting directly to the earth's molten core, bringing physical stamina, endurance, and calm fortitude.",
    "howToWear": "Hold in the palm during stressful crises to ground adrenaline and maintain level-headed poise.",
    "benefits": [
      "Anchors chaotic thoughts into stable practical execution",
      "Aids physical recovery, detoxification, and blood circulation",
      "Provides unwavering emotional support during tough times",
      "Rich deep natural brick-red gemstone"
    ]
  },
  {
    "handle_key": "Product_381df618-95a9-4ef0-a109-72f5bd1222d8",
    "handle": "rhodonite-emotional-balance",
    "title": "Rhodonite: The Rescue Stone of Emotional Balance",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "love emotional healing peace",
    "badge": "Heart Rescue",
    "rating": 5.0,
    "reviewsCount": 180,
    "img": "assets/product-rhodonite.png",
    "images": ["assets/product-rhodonite.png"],
    "sacredSignificance": "Striking pink and black manganese silicate stone famed for clearing emotional scars, past insults, and panic attacks.",
    "howToWear": "Place in quiet spaces to promote forgiveness, mutual respect, and resolution in strained relationships.",
    "benefits": [
      "Soothes emotional shock, past trauma and feelings of betrayal",
      "Encourages mutual forgiveness and loving boundaries",
      "Activates hidden talents and altruistic heart callings",
      "Natural rose-pink stone with dramatic black dendritic veining"
    ]
  },
  {
    "handle_key": "Product_be0284c8-d957-45ef-951c-e061ef7ec208",
    "handle": "smoky-quartz-grounding-protector",
    "title": "Smoky Quartz: The Grounding Protector & Negativity Transmuter",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "protection grounding shani peace",
    "badge": "Aura Purifier",
    "rating": 5.0,
    "reviewsCount": 240,
    "img": "assets/product-smoky-quartz.png",
    "images": ["assets/product-smoky-quartz.png"],
    "sacredSignificance": "Transmutes dense, dark, negative energies into neutral light while providing steady roots during periods of major upheaval.",
    "howToWear": "Place pointing downward at your workstation or altar to channel away environmental stress.",
    "benefits": [
      "Dissolves depression, anxious dread, and heavy psychological baggage",
      "Superior protection against psychic vampires and toxic colleagues",
      "Restores pragmatic grounded focus to flighty thinkers",
      "Translucent smoky brown to dark cognac crystal crystal"
    ]
  },
  {
    "handle_key": "Product_3e7e2fe5-87bc-4e3d-a92d-e289cca5c6e4",
    "handle": "unakite-the-gentle-healer",
    "title": "Unakite: The Gentle Healer of Mind, Heart & Spirit",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "healing love peace spiritual growth",
    "badge": "Heart & Vision",
    "rating": 4.9,
    "reviewsCount": 170,
    "img": "assets/product-unakite.png",
    "images": ["assets/product-unakite.png"],
    "sacredSignificance": "A sacred combination of green Epidote and pink Feldspar that marries heart wisdom with third-eye vision for peaceful rebirth.",
    "howToWear": "Keep nearby during spiritual therapy, shadow work, or pregnancy for peaceful nurturing energy.",
    "benefits": [
      "Releases past blockages inhibiting present-day happiness",
      "Assists in overcoming self-sabotage and addictive habits",
      "Brings balance to emotional extremes and physical health",
      "Unique moss-green and salmon-pink marbled mineral"
    ]
  },
  {
    "handle_key": "Product_8bdcb8c0-9689-4792-beb9-26a0999f2cd9",
    "handle": "lapis-lazuli-third-eye-wisdom",
    "title": "Lapis Lazuli: The Royal Stone of Truth & Third-Eye Wisdom",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "wisdom clarity spiritual growth protection",
    "badge": "Royal Wisdom",
    "rating": 5.0,
    "reviewsCount": 320,
    "img": "assets/product-lapis-lazuli.jpg",
    "images": ["assets/product-lapis-lazuli.jpg"],
    "sacredSignificance": "Prized by ancient Egyptian pharaohs and priests, Lapis awakens the Third Eye, promoting honest self-expression, truth, and intuition.",
    "howToWear": "Place on the throat or forehead during meditation to stimulate clear visionary clarity.",
    "benefits": [
      "Encourages fearless authentic expression of your truth",
      "Stimulates wisdom, memory, intellectual clarity, and psychic vision",
      "Protects against mental control and psychic manipulation",
      "Celestial deep blue with gleaming natural golden Pyrite specks"
    ]
  },
  {
    "handle_key": "Product_4cb5e825-19ad-475d-8948-f00a8296619e",
    "handle": "amazonite-courage-truth",
    "title": "Amazonite: The Stone of Courage, Truth & Soothing Calm",
    "category": "crystals",
    "categoryLabel": "Natural Healing Crystal",
    "intention": "peace clarity healing communication",
    "badge": "Stone of Truth",
    "rating": 4.9,
    "reviewsCount": 210,
    "img": "assets/product-amazonite.jpg",
    "images": ["assets/product-amazonite.jpg"],
    "sacredSignificance": "Named after the legendary Amazon warrior women, this turquoise-green stone balances masculine and feminine energies with soothing calm.",
    "howToWear": "Place on your desk or hold during difficult conversations to speak with clear, calm conviction.",
    "benefits": [
      "Dispels worries, fears, and internal emotional conflict",
      "Filters out cell phone electromagnetic radiation and geophatic stress",
      "Aligns the Throat and Heart chakras for compassionate dialogue",
      "Vibrant seafoam turquoise-green natural crystal specimen"
    ]
  },

  # 5. SACRED PROTECTION TALISMANS (Moved into Crystals)
  {
    "handle_key": "Product_bdcb9a95-4234-4b57-88d8-66b4d4b66b5d",
    "handle": "wulou-and-5-coins-keychain",
    "title": "Feng Shui Wulou & 5 Emperor Coins Protection Keychain",
    "category": "crystals",
    "categoryLabel": "Sacred Healing Talisman",
    "intention": "dhanlabh protection health luck",
    "badge": "Feng Shui Talisman",
    "rating": 4.9,
    "reviewsCount": 330,
    "img": "assets/product-wulou-keychain.jpg",
    "images": ["assets/product-wulou-keychain.jpg"],
    "sacredSignificance": "A revered Feng Shui combination: the holy brass Wulou gourd protects health and life force, while 5 Emperor coins attract wealth from all five directions.",
    "howToWear": "Attach to your house keys, car keys, work bag, or purse for constant mobile protection and wealth activation.",
    "benefits": [
      "Wards off illness qi, accident energy, and sudden financial drains",
      "Invites wealth, authority, and prosperity wherever you go",
      "Crafted with durable sacred red knotting and polished brass charms",
      "Ideal daily protection charm for family members and drivers"
    ]
  },

  # 6. SIGNATURE TAROT READING & HEALING PACKAGES (8 items)
  {
    "handle_key": "manual-package-no-contact-5card",
    "handle": "no-contact-situation-5-card-reading",
    "title": "No Contact Situation Tarot Reading (5 Card Spread)",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "love relationship no-contact clarity reunion",
    "badge": "Bestseller · Relationship",
    "rating": 5.0,
    "reviewsCount": 310,
    "price_override": 799,
    "compare_price_override": 1499,
    "img": "assets/packages/package-no-contact-5card.jpg",
    "images": ["assets/packages/package-no-contact-5card.jpg"],
    "description_override": "When your person has pulled away and you need clarity.\n\n✦ Includes 5 Card Deep Spread:\n• What they feel but don't say\n• Will they contact again & when\n• What's blocking communication\n• Advice from the Universe\n• 💌 Understand the silence and know if reunion is written in destiny\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "Pierces the energetic veil between separated souls to reveal unspoken emotions, hidden intentions, and destiny timelines.",
    "howToWear": "Delivered as a detailed, channeled 5-10 minute voice recording directly to your WhatsApp. Enter your name and partner's name at checkout.",
    "benefits": [
      "Understand what they truly feel but aren't saying",
      "Exact predictions on whether & when they will reach out",
      "Root blockages keeping communication halted",
      "Universal guidance on the highest outcome for reunion"
    ]
  },
  {
    "handle_key": "manual-package-future-spouse",
    "handle": "future-spouse-reading",
    "title": "Future Spouse & Destined Connection Tarot Reading",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "love marriage spouse soulmate destiny",
    "badge": "Destined Connection",
    "rating": 5.0,
    "reviewsCount": 460,
    "price_override": 1499,
    "compare_price_override": 2499,
    "img": "assets/packages/package-future-spouse.jpg",
    "images": ["assets/packages/package-future-spouse.jpg"],
    "description_override": "Perfect for singles curious about their divine partner or destined connection.\n\n✦ Channeled In This Reading:\n• Who Your Future Spouse Is (Personality, Looks, Aura)\n• Nature & Emotional Traits\n• How & Where You'll Meet\n• Timeline of Union\n• Connection Energy & Soul Purpose\n• Future Married Life\n• Angel Guidance & Divine Message\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "Tuning into the akashic marriage grid to reveal the signature traits and arrival timeline of your destined life partner.",
    "howToWear": "Delivered as a comprehensive, channeled voice note recording directly to your WhatsApp with angel cards and timing guidance.",
    "benefits": [
      "Vivid personality, physical vibe & aura traits of your future spouse",
      "Probable settings & synchronistic circumstances of how you will meet",
      "Divine timeline prediction for meeting, proposal & marriage",
      "Angel guidance and sacred remedies to attract union"
    ]
  },
  {
    "handle_key": "manual-package-love-marriage-8q",
    "handle": "love-marriage-pack-8-questions",
    "title": "Love & Marriage Pack (8 Questions In-Depth Reading)",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "love marriage proposal commitment union",
    "badge": "High Accuracy · Marriage",
    "rating": 5.0,
    "reviewsCount": 520,
    "price_override": 1999,
    "compare_price_override": 3499,
    "img": "assets/packages/package-love-marriage-8q.jpg",
    "images": ["assets/packages/package-love-marriage-8q.jpg"],
    "description_override": "A detailed, intuitive, and soulful reading designed for those manifesting commitment and divine union with their true partner.\n\n✦ 8 Questions Explored:\n1. What is the current energy of your love/relationship?\n2. What are your partner's true feelings and intentions?\n3. Will this connection lead to marriage or long-term commitment?\n4. What is the divine timeline for marriage or proposal?\n5. Will it be a love or an arranged marriage?\n6. What blockages or fears are delaying union?\n7. What karmic lesson or past connection influences this relationship?\n8. Remedies, crystals & angel guidance for smooth marriage alignment ✨\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "Comprehensive marital matrix scan exploring current dynamics, partner subconscious intent, karmic chords, and timeline for union.",
    "howToWear": "Delivered directly as an extensive, multi-part voice note recording to your WhatsApp. Enter both partners' names or details at checkout.",
    "benefits": [
      "Answers all 8 core questions regarding commitment, marriage & timeline",
      "Uncovers whether it will be love or arranged marriage",
      "Identifies hidden subconscious blockages delaying proposal",
      "Customized Vedic remedies and crystal recommendations for alignment"
    ]
  },
  {
    "handle_key": "manual-package-no-contact-4q",
    "handle": "no-contact-situation-pack-4-questions",
    "title": "No Contact Situation Pack (4 Questions Reading)",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "love no-contact reconciliation clarity",
    "badge": "Reconnection Clarity",
    "rating": 5.0,
    "reviewsCount": 275,
    "price_override": 799,
    "compare_price_override": 1299,
    "img": "assets/packages/package-no-contact-4q.jpg",
    "images": ["assets/packages/package-no-contact-4q.jpg"],
    "description_override": "Perfect for those waiting for clarity and reconnection.\n\n✦ 4 Questions Reading:\n• Why no-contact happened\n• What they're feeling for you now\n• Will they reach out again & when\n• Angel guidance to handle the situation\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "Brings immediate emotional peace by revealing the psychological and energetic root of sudden silence and the probability of reconciliation.",
    "howToWear": "Channeled directly into a personalized 5-8 minute voice note sent to your WhatsApp number.",
    "benefits": [
      "Clarity on why communication stopped",
      "Insight into partner's emotional state right now",
      "Specific timeline on when reconnection is likely",
      "Angel advice on what actions to take or avoid"
    ]
  },
  {
    "handle_key": "manual-package-heart-consultation",
    "handle": "heart-consultation-private-healing",
    "title": "Heart Consultation: 1:1 Private Healing & Transformation",
    "category": "readings",
    "categoryLabel": "1:1 Private Healing Consultation",
    "intention": "healing heart emotional relationship chakra transformation",
    "badge": "VIP Exclusive · Deep Healing",
    "rating": 5.0,
    "reviewsCount": 180,
    "price_override": 8888,
    "compare_price_override": 12999,
    "img": "assets/packages/package-heart-consultation.jpg",
    "images": ["assets/packages/package-heart-consultation.jpg"],
    "description_override": "🌹 A sacred healing journey for your heart — personally guided by Kavita.\n\nPerfect for souls going through deep emotional healing, relationship pain, heartbreak, or seeking total life transformation.\n\n✦ What is Included:\n• 1:1 Private Consultation (30–45 mins Voice or Video Call; extra charges for video call)\n• ✨ Past-Present-Future Reading: Uncover emotional patterns shaping love & life journey\n• ✨ Energy + Chakra Scan: Identify blockages within your aura & heart centre\n• ✨ Healing Rituals & Remedies: Customized practices, affirmations & crystal guidance\n• ✨ 7-Day Follow-up Support: For continued alignment and emotional integration",
    "sacredSignificance": "The most comprehensive 1-on-1 private healing and psychic diagnostic package, combining live channeled reading, chakra surgery, and a full week of personalized energetic support.",
    "howToWear": "Conducted live 1-on-1 via private appointment. Slot booked upon checkout; 7-day follow-up provided via dedicated WhatsApp channel.",
    "benefits": [
      "30-45 Minutes 1:1 private live session directly with Kavita",
      "Complete Past-Present-Future tarot diagnosis and root block scan",
      "Chakra scanning & customized energetic healing rituals",
      "7-Day continuous follow-up WhatsApp support for full emotional integration"
    ]
  },
  {
    "handle_key": "manual-package-career-growth",
    "handle": "career-growth-reading",
    "title": "Career Growth & Professional Trajectory Tarot Reading",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "career business job success wealth financial clarity",
    "badge": "Career & Wealth",
    "rating": 5.0,
    "reviewsCount": 390,
    "price_override": 1099,
    "compare_price_override": 1899,
    "img": "assets/packages/package-career-growth.jpg",
    "images": ["assets/packages/package-career-growth.jpg"],
    "description_override": "Perfect for career confusion, job changes, promotion decisions, and business clarity.\n\n✦ Channeled In This Reading:\n• Current Career Energy\n• Hidden Strengths & Talents\n• Opportunities & Challenges Ahead\n• Financial Outlook & Stability\n• Divine Guidance for Long-Term Success\n• Remedies & Manifestation Tips\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "Activates the Solar Plexus and Crown chakras to clear career indecision, align with professional abundance, and anticipate corporate or business crossroads.",
    "howToWear": "Channeled voice note sent directly to your WhatsApp. Include current role or business field at checkout.",
    "benefits": [
      "Direct guidance on job switch, promotion, or new venture timing",
      "Reveals untapped strengths and lucrative upcoming opportunities",
      "Accurate forecast of financial stability and income shifts",
      "Vedic remedies and manifestation affirmations for career luck"
    ]
  },
  {
    "handle_key": "manual-package-reunion-reading",
    "handle": "reunion-reading",
    "title": "Reunion Reading: Path to Reconnection & Next Move",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "reunion love ex-partner reconcile timeline feelings",
    "badge": "Reunion & Timing",
    "rating": 5.0,
    "reviewsCount": 415,
    "price_override": 1099,
    "compare_price_override": 1899,
    "img": "assets/packages/package-reunion-reading.jpg",
    "images": ["assets/packages/package-reunion-reading.jpg"],
    "description_override": "Perfect for those hoping to reconnect with their person.\n\n✦ Comprehensive Breakdown:\n• Current Connection Energy\n• Their Hidden Feelings\n• Intentions & Next Move\n• Chances of Reunion (If Yes: full reunion guidance. If No: ask any 3 custom questions of your choice!)\n• Timeline & Divine Signs\n• Spiritual Guidance & Remedies\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "Examines the mutual cord ties and soul contracts between separated lovers, determining if reunion is divinely supported and how to facilitate it.",
    "howToWear": "Channeled voice note sent directly to your WhatsApp with honest, compassionate clarity on the real chances of reunion.",
    "benefits": [
      "Honest evaluation of whether reunion is written in destiny",
      "Uncovers your person's unspoken feelings and planned next moves",
      "Guaranteed flexibility: If reunion isn't favored, ask 3 custom questions",
      "Divine signs to watch for and spiritual remedies to clear friction"
    ]
  },
  {
    "handle_key": "manual-package-deep-insight-8q",
    "handle": "deep-insight-reading-8-questions",
    "title": "Deep Insight Reading (8 Custom Questions of Your Choice)",
    "category": "readings",
    "categoryLabel": "Signature Voice Note Reading",
    "intention": "clarity soul purpose destiny all-areas comprehensive",
    "badge": "Comprehensive · Multi-Deck",
    "rating": 5.0,
    "reviewsCount": 580,
    "price_override": 1999,
    "compare_price_override": 3299,
    "img": "assets/packages/package-deep-insight-8q.jpg",
    "images": ["assets/packages/package-deep-insight-8q.jpg"],
    "description_override": "🌠 A complete soul guidance session — when you're ready for clarity on all fronts.\n\nPerfect for those seeking answers on multiple areas: love, career, destiny, purpose, finances, and life crossroads.\n\n✦ What is Included:\n• 8 Custom Questions of Your Own Choice\n• Multi-deck intuitive spread (Tarot, Oracle & Angel decks)\n• Remedies & energetic alignment guidance\n\n✦ Delivery Format: Detailed Voice Note Reading sent directly to your WhatsApp within 3–4 Days.",
    "sacredSignificance": "A holistic multi-deck divination spread addressing every dimension of your life without topic restrictions.",
    "howToWear": "Send your 8 questions via WhatsApp or add them in the notes at checkout. Kavita channels each question thoroughly.",
    "benefits": [
      "Ask any 8 questions across any life topics (love, money, family, future)",
      "Multi-deck reading combining Tarot, Lenormand and Angel cards",
      "Detailed, thorough 15-20 minute comprehensive voice note",
      "Personalized remedies, chakra alignment tips and timeline forecasts"
    ]
  }
]

# Build JSON array (only visible items from CSV)
products_list = []
curr_id = 1

for item in catalog_defs:
    hkey = item["handle_key"]
    # Hide Rakhis from visible store per user instruction (data preserved in Shopify)
    if item.get("category") == "rakhis":
        print(f"Hiding Rakhi product from visible catalog: {item['handle']} ({item['title']})")
        continue

    raw_r = row_by_handle.get(hkey, {})
    if not hkey.startswith("manual-") and raw_r.get("visible", "false").lower() != "true":
        print(f"Skipping hidden product: {item['handle']} ({item['title']})")
        continue

    # Get price (supports price_override)
    if "price_override" in item:
        price_val = item["price_override"]
        compare_price = item.get("compare_price_override", price_val)
    else:
        csv_price_str = raw_r.get("price", "0")
        try:
            price_val = float(csv_price_str)
            if price_val.is_integer():
                price_val = int(price_val)
        except:
            price_val = 999

        # Strikethrough price
        strike_str = raw_r.get("strikethroughPrice", "")
        compare_price = None
        if strike_str:
            try:
                val = float(strike_str)
                compare_price = int(val) if val.is_integer() else val
            except:
                compare_price = None

    # Description (supports description_override)
    if "description_override" in item:
        csv_desc = item["description_override"]
    else:
        csv_desc = clean_html(raw_r.get("plainDescription", ""))
        if not csv_desc:
            csv_desc = item.get("sacredSignificance", "")

    discount_str = None
    if compare_price and compare_price > price_val:
        pct = round(((compare_price - price_val) / compare_price) * 100)
        discount_str = f"{pct}% OFF"

    prod_obj = {
        "id": curr_id,
        "handle": item["handle"],
        "title": item["title"],
        "category": item["category"],
        "categoryLabel": item["categoryLabel"],
        "intention": item["intention"],
        "price": price_val,
        "comparePrice": compare_price if compare_price else price_val,
        "discount": discount_str,
        "rating": item["rating"],
        "reviewsCount": item["reviewsCount"],
        "badge": item["badge"],
        "img": item["img"],
        "images": item["images"],
        "description": csv_desc,
        "sacredSignificance": item["sacredSignificance"],
        "howToWear": item["howToWear"],
        "benefits": item["benefits"]
    }
    if "durations" in item:
        prod_obj["durations"] = item["durations"]

    products_list.append(prod_obj)
    curr_id += 1

print(f"Built {len(products_list)} product definitions successfully!")

# Format store-data.js content
js_content = """/* ==========================================================================
   KAVITA TAROT READER — OFFICIAL AUTHENTIC CATALOG & COMMERCE ENGINE
   Synchronized directly with Authentic Business CSV Export (Visible Offerings Only)
   Total Verified Visible Offerings: """ + str(len(products_list)) + """
   ========================================================================== */

const STORE_PRODUCTS = """ + json.dumps(products_list, indent=2) + """;

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
    window.dispatchEvent(new CustomEvent("kavita:cart-updated", { detail: items }));
  },
  addItem(productId, quantity = 1, options = {}) {
    const p = STORE_PRODUCTS.find(x => x.id === Number(productId));
    if (!p) return;

    let price = p.price;
    let title = p.title;

    // Handle session durations if consultation
    if (options.duration && p.durations) {
      const match = p.durations.find(d => d.duration === options.duration);
      if (match) {
        price = options.tier === "premium" ? match.premiumPrice : match.standardPrice;
        title = `${p.title} (${options.duration}${options.tier === "premium" ? " - Premium" : ""})`;
      }
    }

    const cart = this.getCart();
    const existing = cart.find(x => x.id === p.id && x.title === title);
    if (existing) {
      existing.quantity += quantity;
    } else {
      cart.push({
        id: p.id,
        handle: p.handle,
        title: title,
        price: price,
        img: p.img,
        quantity: quantity,
        category: p.category,
        categoryLabel: p.categoryLabel,
        options: options
      });
    }
    this.setCart(cart);
  },
  removeItem(index) {
    const cart = this.getCart();
    cart.splice(index, 1);
    this.setCart(cart);
  },
  updateQty(index, qty) {
    const cart = this.getCart();
    if (qty <= 0) {
      this.removeItem(index);
    } else {
      cart[index].quantity = qty;
      this.setCart(cart);
    }
  },
  getTotal() {
    return this.getCart().reduce((sum, item) => sum + (item.price * item.quantity), 0);
  },
  getCount() {
    return this.getCart().reduce((sum, item) => sum + item.quantity, 0);
  },
  updateBadges() {
    const count = this.getCount();
    const badges = document.querySelectorAll(".cart-count-badge, #mobileCartCount");
    badges.forEach(b => {
      b.textContent = count;
      b.style.display = count > 0 ? "inline-flex" : "none";
    });
  }
};

// Initial badge update on load
document.addEventListener("DOMContentLoaded", () => {
  CartEngine.updateBadges();
});
"""

out_path = os.path.join(ROOT, 'assets', 'store-data.js')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully written {out_path} ({os.path.getsize(out_path):,} bytes)!")

