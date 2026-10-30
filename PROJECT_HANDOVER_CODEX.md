# KAVITA — TAROT & SPIRITUALS
## Comprehensive Project Handover & Architecture Document (For Codex / AI Models)

> **Document Purpose:** Single source of truth for the entire codebase. Any AI model or developer reading this file can instantly understand what has been built, how files interact, the design system, real catalogue data, and the Shopify 2.0 implementation.

---

### 1. Brand Identity & Design Direction
- **Brand Name:** Kavita — Tarot & Spirituals (Kavita Tarot Reader)
- **Official Client Website (Source of Truth):** `https://www.kavitatarotreader.com/`
- **Aesthetic Inspiration:**
  - **Rajvira Jewellery:** Clean luxury white/cream canvas, deep royal velvet red accents (`#7d0a28`), warm celestial gold borders (`#d4af37`), refined understated serif typography, clean spacing, no cheap discount badges.
  - **Vani Kabir Spiritual Boutique:** Spiritual authenticity, founder-led warmth, sacred Vedic energization, elegant card layouts.
- **Logo:** Authentic gold lotus icon (`assets/kavita-logo-gold.png`).
- **Celestial Ice Effect:** Delicate circular glowing ice particles drifting across the background via a lightweight 60fps canvas (`assets/ice-effect.js`).

---

### 2. Workspace Directory Structure

```
TAROT READER/
├── PROJECT_HANDOVER_CODEX.md       <-- THIS FILE (Master handover specification)
├── index.html                      <-- Main luxury homepage
├── collections.html                <-- All offerings & products with category filter
├── consultations.html              <-- Live Tarot Readings & Energy Healing sessions
├── product.html                    <-- Product detail & booking page template
├── about.html                      <-- About Kavita & spiritual journey
├── contact.html                    <-- Contact & booking enquiry form
├── faq.html                        <-- Authentic client FAQ
├── Kavita-Tarot-Dawn-2.0.zip       <-- Complete ready-to-upload Shopify 2.0 theme zip (16MB)
│
├── assets/                         <-- Static frontend assets (CSS, JS, WebP/JPG images)
│   ├── vanikabir.css               <-- Master stylesheet (desktop & mobile responsive rules)
│   ├── ice-effect.js               <-- Celestial circular floating ice particle engine
│   ├── store-data.js               <-- Real product/consultation catalog and mock cart
│   ├── banner-1-desktop.jpg        <-- Rajvira-style desktop hero banner 1
│   ├── banner-1-mobile.jpg         <-- Mobile hero banner 1
│   ├── banner-2-desktop.jpg        <-- Desktop hero banner 2
│   ├── banner-2-mobile.jpg         <-- Mobile hero banner 2
│   ├── kavita-logo-gold.png        <-- Official Kavita gold lotus emblem
│   └── product-*.jpg               <-- Curated luxury product & reading images
│
└── kavita-dawn/                    <-- Unzipped Shopify 2.0 Dawn-based Theme
    ├── config/
    │   ├── settings_data.json      <-- Shopify theme settings & colors
    │   └── settings_schema.json
    ├── layout/
    │   └── theme.liquid            <-- Master theme template with mobile bar & scripts
    ├── sections/
    │   ├── kavita-interactive-slider-hero.liquid  <-- Rajvira banner slider with customizer
    │   ├── kavita-premium-hero.liquid             <-- 3D floating tarot card hero
    │   ├── header.liquid                          <-- Header with mobile logo-only behavior
    │   └── footer.liquid                          <-- Luxury 4-column footer
    ├── snippets/
    │   ├── kavita-mobile-bottom-nav.liquid        <-- Floating sticky mobile navigation
    │   └── whatsapp-button.liquid                 <-- Direct client WhatsApp chat trigger
    └── assets/                                    <-- Shopify theme assets mirror
```

---

### 3. Real Product & Service Catalogue (Exclusively from Client's Site)

All dummy/marketplace items were removed. Only authentic offerings from `kavitatarotreader.com` are present in `assets/store-data.js`:

#### A. Tarot Readings & Consultations (High-Value Services)
1. **Live Audio Tarot Consultation (45 Min)** — ₹3,999 (Regular ₹4,999)
   - Real-time deep dive into Love, Career, Life Path, and Blockages with Kavita.
2. **WhatsApp Voice Note Reading (3 Detailed Questions)** — ₹2,499
   - Audio notes sent within 24–48 hours with card photos.
3. **Urgent Situational Tarot Reading (1 Priority Question)** — ₹1,999
   - Fast-track 12-hour turnaround for urgent crossroads decisions.
4. **Cord Cutting & Karmic Release Consultation** — ₹4,499
   - Energetic detachment ritual for past relationships, trauma, and negative ties.
5. **Vortex of Blessings Energy Ritual** — ₹3,499
   - Sacred Vedic fire & intention ceremony to manifest abundance and protection.
6. **Tibetan Lamafera Sacred Distance Healing** — ₹5,499
   - Powerful ancient monk healing system for deep aura and chakra restoration.

#### B. Spiritual Tools & Energized Products
1. **Uruguayan Deep Purple Amethyst Cluster** — ₹3,299
   - High-grade natural geode for meditation, crown chakra, and negative energy absorption.
2. **7 Chakra Energized Gemstone Bracelet** — ₹1,499
   - Handcrafted natural beads infused with Vedic mantras for balance.
3. **Moroccan Selenite Energy Cleansing Wand** — ₹1,299
   - Pure satin-spar selenite for charging tarot decks and cleansing crystals.
4. **Natural Golden Pyrite Abundance Cluster ("Fool's Gold")** — ₹2,199
   - Powerful stone for attracting financial prosperity and business success.
5. **Luxury Gold Foil Celestial Tarot Deck** — ₹2,899
   - 78-card gold gilded deck with custom guidebook and velvet pouch.
6. **Celestial Moonlight Oracle Guidance Cards** — ₹2,499
   - 44 intuitive cards with moon phases and astrological guidance.

---

### 4. Core Features & UX Architecture

#### 1. Header & Navigation
- **Desktop:** Multi-tier luxury header with announcement ticker, logo + brand name, category navigation menu, instant search bar, wishlist, account, and cart drawer counter.
- **Mobile (`< 768px`):**
  - **Logo Only:** Brand name text `KAVITA TAROT READER` is hidden on mobile (`display: none !important`), showing ONLY the gold lotus emblem on the left.
  - **Actions Preserved:** Search button, Wishlist, Account, and Cart are all visible on the right with zero overflow/clipping.

#### 2. Hero Section (Interactive Banner Slider)
- Matches the reference jewellery boutique (Rajvira) layout:
  - Clean edge-to-edge container with rounded luxury radius.
  - Supports separate **Desktop Banner** (`assets/banner-1-desktop.jpg`) and **Mobile Banner** (`assets/banner-1-mobile.jpg`).
  - Next/Previous slide navigation arrows and pagination dots.
  - Call-to-action buttons configured with real URL settings in Shopify Liquid schema.

#### 3. Category Section (Circular Badges)
- Original circular avatar badges (`.categories-circle-row`):
  - Gold gradient ring border around circular images.
  - Full width layout with compact side padding (`0.85rem`) and small gaps (`0.75rem`).
  - Smooth horizontal scrolling on mobile without scrollbar clutter.

#### 4. Product Sliders & Mobile 2-per-Row Grid
- Product carousel (`#consultationsTrack` and `#productsTrack`):
  - Exactly **2 products per row** on mobile view (`calc(50% - 0.35rem)`).
  - Cards are fully visible with zero left/right cutoff or clipping.
  - Card typography: `0.88rem` bold title, `0.98rem` price, touch-friendly primary action buttons (`Book Online` / `Add to Cart`).

#### 5. Typography & Understated Luxury Headings
- Section headings use a subtle, refined luxury scale:
  - Desktop: `clamp(1.25rem, 2.2vw, 1.65rem)`
  - Mobile: `1.15rem`
  - Font: Cormorant Garamond / Playfair Display paired with Montserrat / Inter body font.

#### 6. Mobile Floating Bottom Navigation
- Fixed floating luxury bar on mobile view:
  - **Home** (center highlighted circular button)
  - **Readings** (tarot consultation shortcut)
  - **Shop** (collection shortcut)
  - **Cart** (live drawer opener with badge count)

#### 7. Background Ice Effect
- Implemented in `assets/ice-effect.js`.
- Renders 38 delicate circular ice particles on mobile and 68 on desktop.
- Floats downwards with gentle sine-wave horizontal drift, soft glow, and pauses automatically when the tab is inactive. Pointer-events are set to `none` to avoid blocking user clicks.

---

### 5. Shopify Online Store 2.0 Implementation

- The directory `kavita-dawn/` contains the full Shopify theme based on Dawn architecture.
- Section file `sections/kavita-interactive-slider-hero.liquid` includes:
  - `logo`, `desktop_logo_width`, `mobile_logo_width` image picker settings.
  - Slide blocks supporting `desktop_image`, `mobile_image`, `subheading`, `heading`, `button_label`, and `button_link`.
- Layout `layout/theme.liquid` includes:
  - Master styling: `{{ 'vanikabir.css' | asset_url | stylesheet_tag }}`
  - Celestial particle effect: `<script src="{{ 'ice-effect.js' | asset_url }}" defer="defer"></script>`
  - Mobile bottom nav: `{% render 'kavita-mobile-bottom-nav' %}`
  - WhatsApp quick contact: `{% render 'whatsapp-button' %}`
- Ready-to-upload zip file: **`Kavita-Tarot-Dawn-2.0.zip`** (16MB).

---

### 6. Development & Deployment Reference

- **Local Preview Server:** Port 3000 (`python3 -m http.server 3000`)
- **Active Cloudflare Tunnel:**
  - `cloudflared` standalone binary at `/tmp/cloudflared`
  - Live client view URL: **`https://bra-sunrise-anymore-cardiovascular.trycloudflare.com`**
  - Command to re-run tunnel if restarted:
    ```bash
    /tmp/cloudflared tunnel --url http://localhost:3000
    ```
- **Rebuilding the Shopify Theme Zip:**
  ```bash
  rm -f Kavita-Tarot-Dawn-2.0.zip && (cd kavita-dawn && zip -r -q ../Kavita-Tarot-Dawn-2.0.zip .)
  ```

---
*Created for seamless handoff to OpenAI Codex / LLM agents.*
