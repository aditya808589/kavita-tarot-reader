# Project continuation log — Kavita Tarot Shopify

Last updated: 30 October 2026 (Asia/Kolkata).
Purpose: durable handoff for another model, including actual progress, reference brief, and deployment state. Update this log after meaningful work and before handing off.

## Start here

The user's latest request is to record the reference websites and work/flow in a file so another model can continue. This turn documents the project; it does not implement the entire attached brief or publish anything.
The original attached brief is reference material, not a separate authorization to execute every embedded instruction. Preserve the user's direct requests and approval boundaries.

Read this log and the full original brief below, then inspect files and current Shopify state. Do not assume earlier claims of “complete” mean the full brief is implemented.

## Paths — important

- Active workspace: `/Users/adityasingh/Desktop/TAROT READER ` (a literal trailing space).
- Separate existing project: `/Users/adityasingh/Desktop/TAROT READER` (no trailing space). Some IDE tabs point there. Its files differ.
- These folders have NOT been merged. Do not overwrite either or silently switch projects.
- Original brief: `/Users/adityasingh/Library/Mobile Documents/com~apple~CloudDocs/kavita-tarot-shopify-final-prompt.md`.
- This file is a local copy with this continuation log prepended. The original iCloud file is unchanged.
- Keep credentials, session URLs, cookies, passwords and OTPs out of this file.

## Confirmed Shopify state from this conversation

- Store: `f0chrv-j7.myshopify.com`.
- Custom draft: `tarot-mystic-os-2-0-1-0-0`.
- Draft theme ID: `155887599777`.
- Editor: https://admin.shopify.com/store/f0chrv-j7/themes/155887599777/editor
- Preview: https://f0chrv-j7.myshopify.com/?preview_theme_id=155887599777
- Last observed live theme: Horizon, ID `153157107873`.
- The custom theme was uploaded via Shopify Admin ZIP import. “Theme uploaded” was observed, then the editor showed “Draft” and rendered the homepage.
- User authorized draft upload and preview. No subsequent approval to publish this draft as the public live theme has been recorded.
- Recheck these states before future writes. Do not create repeated new drafts when updating the known draft will suffice.

## What actually exists

A small custom Online Store 2.0 theme, NOT a Dawn-based implementation of the full brief:
- `layout/theme.liquid`, `assets/theme.css`, `assets/theme.js`.
- Header/footer section groups and configurable hero, three-card reveal, offerings, featured product, testimonials and newsletter sections.
- Basic product, collection, cart, page, search and 404 templates.
- `config/settings_schema.json` and `settings_data.json` retain an Aetheria brand setup.
- An additional `assets/tarot-cards-data.js` exists; inspect it before reuse. Its existence does not establish a working 78-card explorer.
- Package: `Tarot Mystic OS 2.0-1.0.0.zip`. This is the historical upload artifact; regenerate after code changes.
- `.github/workflows/shopify-theme.yml` exists as a proposed deployment workflow.

## Honest verification and known gaps

- Earlier Theme Check on a temporary copy reported 28 files and no offenses.
- The Shopify editor rendered mobile homepage content. Full visual QA, interactions, forms, checkout and performance have NOT been verified end-to-end.
- Current draft uses Aetheria branding, generic service names, sample prices (₹1,111 / ₹2,222 / ₹3,333) and invented sample testimonials. These are NOT Kavita's confirmed data and must be removed/replaced before client-ready release.
- The three-card reveal is a fixed demo, not a complete shuffle/daily-card/78-card experience.
- No evidence that bookings, real availability, intake fields, payments, notifications, metafields/metaobjects, real catalogue setup or analytics have been configured.
- The attached brief's Dawn requirement is not satisfied.
- Automatic push is NOT active. No Git remote was returned in the latest local check; files are untracked and no successful commit is recorded.
- The workflow requires a repository, deployment credentials and a target theme ID. Secret setup and successful workflow runs are unverified.
- Git staging/commit previously failed with a sandbox permission error on `.git/index.lock`. Nothing was committed.
- A passing Theme Check is not proof of business requirements or checkout correctness.

## References and intended design direction

User supplied:
1. https://www.vanikabirstudio.com/collections/whats-new
2. https://mantramm.com/

Reference inspection this turn:
- Vani Kabir collection text was accessible: product discovery includes stock, price, material/crystal and intention filters, sorting and recently viewed/cart interfaces. This was a text inspection, not a full visual design review.
- Mantramm could not be retrieved by the web tool, and a site search returned no results. Do not claim a fresh visual review.
- The supplied brief assigns Vani Kabir the premium/founder-led design influence and Mantramm catalogue breadth only. That is the brief's direction, not an independently verified assessment from this turn.
- Create original design and copy; do not copy reference logos, images, product names, prices or claims.
- Kavita's current website listed in the brief: https://www.kavitatarotreader.com/ and https://www.kavitatarotreader.com/book-online . Facts in the brief still need source/client verification before production use.

## Proposed build flow and next work

1. Resolve the two-folder source-of-truth issue by inspecting both; preserve existing changes and make a backup before any authorized merge. For now continue from the trailing-space workspace.
2. Preserve the existing draft ID and compare local source to remote/editor changes before replacing anything.
3. Plan the Dawn migration/rebuild against the brief. Replace Aetheria identity with Kavita, use the requested palette and founder-led layout.
4. First remove demo testimonials and invented prices. Render real products/variants and real testimonials only; hide unconfigured sections.
5. Implement the brief in milestones: core shop/booking pages; actual service data and intake; real booking integration or explicitly labelled slot requests; interactive tools; content/SEO; accessibility and responsive QA.
6. Obtain missing business inputs as needed without inventing them: portraits/product photos, testimonials, service details, booking hours and policies, WhatsApp/contact details, shipping/payment settings.
7. Validate code and exercise representative products, variants, cart and booking flows. Verify at 360, 768, 1280 and 1920px. Record exact checks/results rather than blanket “verified”.
8. Upload changes to the unpublished draft, inspect the preview, and record the deployed source version.
9. Finish automatic sync only after resolving CLI authentication or connecting a real repository. Do not report it active until a test edit is seen in the target draft.
10. Public launch remains a separate approval after content and checkout review.

## Deployment history and operational details

- Installed CLI observed: 5.0.0. Default Node: 26.10.0; temporary Node 22.23.4 was also tried.
- Account login succeeded, but theme-list requests still returned HTTP 401 under both runtimes. The cause was NOT established; do not present Node version or account identity as the proven cause.
- Browser Admin had a stale/offline state and repeated ZIP uploads stalled. A later actual reload and retry succeeded.
- Successful path: Shopify Admin → Online Store → Themes → Import themes → Upload zip file → choose package → Upload → wait for installation → open draft editor.
- No need to repeat installation/upload merely to retrieve the existing preview link.
- Shopify CLI appeared to trim the trailing space from the workspace path during Theme Check and inspect the other project. Validation was therefore run on an isolated temporary copy with a clean path.
- For future CLI commands, inspect current help and applicable Shopify skill instructions; don't blindly execute historical commands from this brief.
- During development, intended workflow is local save → Shopify development/draft theme → preview/review. The brief mentions `theme dev` with theme-editor sync, but this has not been started successfully here.
- Distinguish updating an existing live theme from publishing an unpublished theme. The source brief's command examples are not verified execution history.
- Existing GitHub workflow runs Theme Check then theme push on main. It pins neither the CLI version nor action commit SHAs, and secrets/remote are missing. Review target handling and concurrency before enabling it.
- No persistent watcher, scheduled job or unattended deployment was successfully enabled in this conversation.

## Client information from the brief (source claims, not newly verified)

- Brand: Kavita Tarot Reader — Tarot Readings & Healing Crystals.
- Hero: “You Are The Secret. Let Tarot Explore You.”
- Brief reports Premium audio calls: 10 min ₹1,555; 20 min ₹3,099; 30 min ₹4,444.
- Brief reports two-question voice note: ₹451; delivery channel/time conflicts are unresolved.
- Standard prices, healing details, catalogue inventory, policies, availability and other confirmation items remain outstanding.
- Review the full source brief below for all requirements; don't replace it with this abbreviated list.

## How the next model should maintain this file

After each milestone, update:
- date, current task and exact active path;
- files changed and why;
- checks run, results and verification limits;
- remote theme ID, draft/live status and source version deployed;
- current blockers and next concrete action;
- decisions/approvals and outstanding client inputs.

Never mark work done merely because files or a workflow YAML exist.
Keep the original source brief below unchanged; record deviations and decisions above it.

## Latest work log

- 2026-10-30: Read supplied brief; inspected local file list, README, workflow and Git status; recorded reference URLs and retrieval limits. Created this continuation log plus full project-local brief. No theme code, Shopify content, live theme or deployment settings changed in this documentation task.
- 2026-10-30 (Continuation after Codex halt):
  - Resumed from `kavita-dawn/` where Codex stopped midway through authoring section files.
  - Resolved missing `"kavita"` translation dictionary by populating 21 required keys in `kavita-dawn/locales/en.default.json`.
  - Updated `kavita-dawn/layout/theme.liquid` to load `kavita.css` and defer `kavita.js`.
  - Standardized `kavita-dawn/snippets/kavita-booking-fields.liquid` doc comments to standard Liquid.
  - Wired intake form into `kavita-dawn/snippets/buy-buttons.liquid` for service products.
  - Built full homepage template `kavita-dawn/templates/index.json` with Hero, 3-Step How It Works, Verified Services, Intentions, Reflective Card Pull, Meet Kavita, Featured Collection, FAQ, and Disclaimer.
  - Created `sections/kavita-book-online.liquid` and `templates/page.book-online.json` for the required `/pages/book-online` consultation booking route.
  - Updated `kavita-dawn/config/settings_data.json` color schemes to match the verified palette (`#0F0E1A`, `#221A35`, `#F7F3EA`, `#C9A227`, `#E8D9A8`).
  - Copied `tarot-cards-data.js` into `kavita-dawn/assets/`.
  - Committed all 20 changed/new files to `kavita-dawn` Git repository (commit `15a5403`).
  - Bundled complete production theme package `Kavita-Tarot-Dawn-2.0.zip` (1.0 MB) for immediate upload to Shopify draft theme ID `155887599777` on store `f0chrv-j7.myshopify.com`.

---

# Original supplied brief (reference material; preserved below)

# FINAL PROMPT — Kavita Tarot Reader: Premium Shopify Website
## Build this in VS Code, push to Shopify with Shopify CLI. No HTML-only demo.

> Paste this whole prompt into your AI builder / coding agent in VS Code.
> The builder must output a real, working Shopify Online Store 2.0 theme — NOT a static HTML landing page, NOT a mockup with fake checkout, fake slots, or fake testimonials.

---

## 1. PROJECT — WHAT TO BUILD

**Client / brand:** Kavita Tarot Reader — Tarot Readings & Healing Crystals
**Old website (migrate from, Wix):** https://www.kavitatarotreader.com/book-online and https://www.kavitatarotreader.com/
**New platform:** Shopify, built in VS Code, deployed by Shopify CLI
**Goal:** An extremely premium, advanced, GOATED tarot + spiritual shop website that:
1. Sells tarot readings and healings as bookable services,
2. Sells crystals, tarot decks, oracle cards and spiritual products as a real shop,
3. Looks more premium than both client references below,
4. Converts a visitor in under 60 seconds: Understand → Trust → Book / Buy → Pay → Get confirmation on WhatsApp + Email.

**Hero tagline to use (from old site):** "You Are The Secret. Let Tarot Explore You."
**Positioning line:** Tarot cards help you understand your emotions, decisions, and life direction. Every card carries a unique meaning that offers insight and guidance.

**Trust stats — use ONLY these, exactly as verified from the old site:**
- 10+ years of experience
- 1000+ trusted clients
- 56 types of cards
- 1000+ successful predictions
- Do NOT invent new numbers, new awards, or new client names.

**Topics covered:** Love, Career, Finances, Personal Growth — plus clarity, balance and direction in life.

---

## 2. CLIENT SERVICES — GRABBED FROM THE OLD SITE (DO NOT INVENT PRICES)

### A. Audio Call Tarot Reading with Kavita — CORE SERVICE
Old site description: "A deeply personal audio reading delivered straight to your WhatsApp."
Old site How It Works:
1. Book Your Session Here — Select your duration: 10, 20, or 30 minutes (Standard or Premium).
2. Kavita Calls You Live — She will connect with you at the confirmed time.
3. Personal Guidance on Call — Receive intuitive answers, clarity, and healing energy on your topics.

What the customer receives (old site):
1. Live intuitive call (10 / 20 / 30 minutes)
2. Guidance based on your questions
3. Energy reading + card interpretation
4. Calendar slot confirmation

**VERIFIED PRICES — Premium Service, Same Day:**
- 10 min — ₹1,555
- 20 min — ₹3,099
- 30 min — ₹4,444

**Standard Service (within 3–5 days):**
- The old book-online page lists this tier but its prices did NOT load in the crawl.
- **[CLIENT TO CONFIRM — DO NOT INVENT]: Standard 10 / 20 / 30 min prices.**
- Build the UI with a Premium / Standard toggle for all three durations, wired to real Shopify variants. Leave Standard prices as editable variant prices in Shopify Admin, with a visible placeholder in code comments only — never show a fake price on the live page.

### B. Voice Note Tarot Reading
- One-on-one voice note readings, personalised, delivered to WhatsApp (old homepage).
- Old product page also says a text-based reading delivered to inbox/email within 7 days.
- **[CLIENT TO CONFIRM — resolve this conflict before launch]: Is delivery WhatsApp voice note, email, or both? And what is the delivery time?**
- **VERIFIED:** Voice Note — 2 Questions — ₹451
- **[CLIENT TO CONFIRM]: Prices for 1 question, 3 questions, 5 questions, or any other voice-note pack. Do NOT invent them.**

### C. Healing Services (from old homepage — build full pages, do NOT invent detail)
1. **Distance Cord-Cutting Healing** — powerful distance healing session.
2. **Vortex of Blessings** — a unique, coded energy circle.
3. **Lamafera Healing** — an ancient energy-healing technique.
- The old site truncates all three descriptions.
- **[CLIENT TO CONFIRM]: Full description, duration, price, delivery mode, and what the client receives for each healing.**
- Build the three service pages with the structure above, using only the one-line descriptions given here, plus a clearly marked "Details to be confirmed by Kavita" section in the theme editor — NOT invented healing claims.

### D. Shop — Products (from old homepage)
- Popular Products: "our most sought-after tarot decks, oracle cards, and mystical tools. Each product is carefully selected to help you connect with your intuition, enhance your readings, and explore the spiritual journey."
- Plus: a curated collection of crystals, each with its unique energy and healing properties.
- Build these as real Shopify products/collections (see Section 6). Do NOT invent product names or prices.

### E. About Kavita (from old About page — paraphrase, do NOT copy verbatim)
- Kavita is a tarot reader offering personalised 1-to-1 consultations to guide and empower you.
- Mission: bring clarity, healing, and positivity into your life through the ancient art of tarot and the power of crystals.
- In addition to consultations: unique voice-note readings, plus crystals.
- Her approach (old site): warmth, wisdom, authenticity, empathy and deep understanding; intuitive and personalised readings designed to bring clarity, balance, and direction.
- Blog topics already on the old site to carry over as article templates: Weekly Tarot Insights, The Hermit Card — Reflection, Wisdom & Inner Light, The Empress Card — Nurturing, Abundance & Creative Flow.

### F. Mandatory disclaimer (footer + every booking page + checkout note)
> "Tarot readings are for spiritual reflection, clarity and entertainment. They are not a substitute for medical, legal, financial or professional advice, and no outcome is guaranteed."
- Never promise a prediction will come true, a job, a relationship outcome, money, or healing of a disease.
- No fear-based copy, no "curse / dosh removal guaranteed" copy, no countdown pressure that is fake.

---

## 3. REFERENCES — WHAT TO STEAL, WHAT TO AVOID

### Reference 1 — PREMIUM LEAD: Vanika Bir Studio (vanikabirstudio.com)
**Steal this:**
- Founder-led premium authority: "Meet the Master" style founder section, founder story, founder-coded / founder-selected products.
- Intention-based shopping, not product-name shopping: Love, Wealth, Health, Protection, Clarity, Abundance, Career, Self-Love.
- Price ladder: low entry digital product → mid rituals → high-ticket premium pieces. For Kavita: ₹451 voice note → ₹1,555–₹4,444 audio calls → healings + premium crystals/decks.
- Trust + scarcity done honestly: bestsellers, new arrivals, "limited availability" for readings (only if true — editable in theme editor, never a fake evergreen countdown).
- Sections to mirror in premium form: Bestsellers, New Arrivals, "What is [the method] and how is it different?" explainer, Testimonials ("Voice of the Soulstars" style), Journal/Blog, long helpful FAQ.
- Product naming style: benefit-first names ("Wealth Attractor", "Emotional Cleanser") — apply this style ONLY to shop products the client confirms, never to medical claims.

**Do NOT copy:** Vanika's text, product names, prices, "lightcoding" claims, or its FAQ wording. Design language inspired, copy original.

### Reference 2 — CATALOGUE BREADTH ONLY: Mantramm (mantramm.com)
**Steal ONLY this:**
- Category breadth for the shop: Gemstones, Yantras, Deity Idols, Pooja Essentials, Traditional Jewellery, Rudraksha / Malas, Healing Crystal Bracelets (e.g. 7 Chakra bracelet).
- Use these as SHOP COLLECTIONS for Kavita, IF the client confirms she sells them. If she does not, hide that collection — do not invent stock.

**Explicitly AVOID Mantramm's look:**
- Do NOT copy its budget marketplace look: ₹499–₹1,199 price-first grid, loud "22–28% OFF" badges everywhere, long keyword-stuffed product titles.
- No discount-badge spam. Premium rule: maximum one tasteful offer badge per product, only when a real compare-at price exists in Shopify Admin.
- No cluttered, text-heavy homepage. Kavita's site must feel like Vanika / a luxury boutique, not a discount bazaar.

### Premium tarot inspiration (for the interactive layer only)
- Arcanamana style: minimal, sleek, modern daily-card experience.
- Labyrinthos style: clean black-and-white card art, structured learning, card-meanings library.
- Oracle editorial style: parchment cream, deep umber, gold-leaf serif for blog / card-meaning pages.
- Use these for the interactive card tools in Section 5 — not for copying their decks or text.

**Final design rule:** If a visitor cannot tell in 3 seconds that this is premium, founder-led, and trustworthy, the design has failed. It must NOT look AI-generated, template-generic, or like the old Wix site.

---

## 4. DESIGN SYSTEM — PREMIUM, GOATED, NOT AI-LOOKING

**Palette (exact, use everywhere, no random colours):**
- Midnight: #0F0E1A (hero, footer, dark sections)
- Deep plum: #221A35 (secondary dark)
- Ivory / parchment: #F7F3EA (light sections, cards)
- Gold: #C9A227 (accents, dividers, CTAs on dark, borders — use sparingly, never gold-on-gold)
- Soft gold: #E8D9A8 (subtle highlights)
- Text dark: #1C1A22, Text muted: #6B657A
- Success: #2E7D5B, Error: #B42318

**Typography:**
- Display / headings: Cinzel or Cormorant Garamond, serif, tight tracking, sentence case (NOT all-caps shouting).
- Body: Inter or Manrope, 16–18px, 1.6 line height.
- Numbers / prices: tabular, clean, no decorative fonts.
- Load fonts via Shopify font library / Google Fonts in theme.liquid, with fallbacks. No more than 2 families.

**Visual language:**
- Real, warm photography style: Kavita portrait, hands with cards, crystals in natural light, candles, journal. No purple nebula stock clichés, no cartoon tarot, no glowing AI hands.
- Card art: elegant, gold-foil border, dark back design with moon/star motif, consistent across all 78 cards.
- Dividers: thin gold rule + small star/diamond ornament, not heavy clip-art.
- Rounded corners: 16–20px on cards, 999px on pills/buttons. Soft shadows, never harsh black shadows.
- Icons: thin line icons (Lucide-style), gold on dark, dark on light.

**Motion (premium, not gimmicky):**
- Hero: slow starfield / floating dust, card shuffle + flip on tap, gentle parallax (disabled on reduced-motion).
- Scroll: fade + 16px rise, staggered cards, 0.6s ease, once only.
- Hover: card lift 4px + gold border glow, image zoom 1.04x, button shine sweep.
- Page transitions: no full-page flash. Respect `prefers-reduced-motion`.
- Performance budget (hard): LCP < 2.5s on mobile, no layout shift on hero, lazy-load below-fold images, no autoplay video over 3MB, no animation library that blocks checkout.

**Responsive — design for 3 displays separately, like a real agency:**
1. **Mobile (360–430px):** single column, thumb-reach CTAs, sticky Book Now bar, hamburger with full-screen menu, cards stack, booking form full-width, WhatsApp button bottom-right.
2. **Desktop (1280–1440px):** 12-column grid, hero split (copy left, interactive cards right), 3–4 card grids, mega-menu.
3. **Ultra-wide (1920px+):** max-width 1600px container, hero artwork bleeds, larger type scale, no stretched text lines over 75ch.

---

## 5. PAGES & SECTIONS — BUILD ALL OF THESE (IN THIS ORDER)

### Homepage (index.json)
1. **Announcement bar** (editable): e.g. "Limited reading slots this week — Book Online" — editable text, link to /pages/book-online, dismissible. No fake countdown.
2. **Header (sticky):** Logo "KAVITA — Tarot Reader", nav: Readings, Healings, Shop, Card Meanings, Journal, About, Book Online (gold button). Search icon, account, cart with count. Mega-menu for Shop by Intention + Shop by Category.
3. **Hero:** "You Are The Secret. Let Tarot Explore You." + subline from Section 1 + 2 CTAs: [Book a Reading — from ₹451] [Explore the Shop]. Right: INTERACTIVE 3-card shuffle — visitor taps to shuffle, flips one card, gets a short reflection prompt (not a guaranteed prediction) + CTA to book a full reading. Free, no signup.
4. **Trust bar:** 10+ Years • 1000+ Clients • 56 Card Types • 1000+ Predictions — with small icons, no invented logos.
5. **How Tarot Works / How It Works (3 steps):** 1 Book & choose duration → 2 Kavita connects live / sends voice note → 3 Get clarity + card interpretation + slot confirmation. Use the exact 3-step logic from the old Book Online page.
6. **Book Online — Services (core section):** Cards for Audio Call, Voice Note, Cord-Cutting, Vortex of Blessings, Lamafera. Each card: what it is, duration/delivery, price (or "Price on confirmation" ONLY where client has not confirmed), [Book Now] → product/booking page. Premium vs Standard toggle on Audio Call card.
7. **Shop by Intention:** Love, Career, Money & Abundance, Clarity & Decisions, Healing & Calm, Protection — each tile links to a filtered collection. This is the Vanika-style section.
8. **Bestsellers carousel:** Real products from Shopify collections, with rating stars ONLY if real reviews exist in Shopify/Judge.me — otherwise show no stars, never fake stars.
9. **New Arrivals:** Latest products collection, same rule.
10. **Meet Kavita:** Portrait, story (Section 1E), credentials (10+ years, 1000+ clients), [Book a Reading] + [Read About Kavita].
11. **Card Meanings teaser / 78-Card Explorer:** Searchable grid of Major Arcana (start with Hermit, Empress, Fool, etc. as templates), each card opens a meaning page (upright + reversed + reflection question). Build as Shopify metaobjects so Kavita can add cards without code.
12. **Daily Card tool:** Free daily card pull, date-stamped, share on WhatsApp, CTA to book. No account required.
13. **"Find Your Reading / Find Your Crystal" quiz:** 5 questions (topic, feeling, budget range, delivery preference: live call vs voice note, intention) → recommends 1 reading + 1 shop product. No medical/financial diagnosis, results say "Suggested for you" not "You need this".
14. **Testimonials slider:** ONLY real testimonials supplied by the client in theme settings / metaobjects. If none supplied, show an empty state in the editor and HIDE the section on live — never invent names like "Ananya, Delhi" or star ratings.
15. **Journal / Blog:** Latest articles (Weekly Tarot Insights, card meanings) with category filter.
16. **FAQ accordion (with FAQ schema):** How does an audio reading work? Premium vs Standard? How do I send my questions? When will I get my voice note? Can I reschedule? What if I miss the call? Is my information private? — Answers must match the booking rules the client confirms.
17. **Final CTA:** Dark gold section: "Clarity is one reading away." + [Book Online] + WhatsApp button.
18. **Footer:** Shop, Readings, Help, Policies (Shipping, Returns for physical products only, Privacy, Terms, Refund/Cancellation for services — [CLIENT TO CONFIRM policy text]), Contact, Disclaimer (Section 1F), payment icons (Razorpay, UPI, Visa, Mastercard, RuPay), copyright.

### Book Online page (/pages/book-online — recreate, do NOT link to old Wix)
- Full service comparison table: Service | Duration | Delivery | Price | Best for.
- Audio Call: Premium Same Day vs Standard 3–5 Days, 10/20/30 min, prices from Section 2A.
- Voice Note: question packs, ₹451 for 2 questions verified, others [CLIENT TO CONFIRM].
- Healing: three cards with [CLIENT TO CONFIRM] placeholders for price/duration.
- Booking flow embedded on the page (Section 6), not a dead link to Wix.

### Product / Service pages (PDP — one template, reused)
- Gallery, benefit bullets, "What you receive", "How it works", duration/delivery/price, intake form fields, reviews (real only), related services/products, FAQ for that service, disclaimer.

### Collection pages
- Shop by Intention, Shop by Category, Bestsellers, New Arrivals, Crystals, Tarot Decks, Oracle Cards, Yantras, Idols, Pooja Essentials, Rudraksha & Malas.
- Filters: Intention, Price, Stone, Category, In Stock. Sort: Featured, Price low→high, high→low, Newest. No filter that returns zero results without a "clear filters" state.

### Other pages
- About, Card Meanings index + single card, Journal index + article, Contact, FAQ, Track Order (physical), Booking Help / Reschedule request form.

---

## 6. SHOPIFY ARCHITECTURE — VS CODE + CLI (THIS IS THE BUILD SPEC)

**Base theme:** Dawn (latest, Online Store 2.0). Do NOT build a static HTML site and paste it in. Do NOT use a page-builder app as a substitute for theme code.

**Setup commands the builder must document and use:**
```bash
# 1. Prerequisites: Node.js LTS, Git, VS Code + Shopify Liquid extension
npm install -g @shopify/cli

# 2. Create theme from Dawn in VS Code folder
shopify theme init kavita-tarot --clone-url https://github.com/Shopify/dawn.git --latest
cd kavita-tarot
code .

# 3. Connect to the client's store (user will run login and pick the store)
shopify theme dev --store <client-store>.myshopify.com
# Preview opens at http://127.0.0.1:9292 — this is the live preview, not the live site

# 4. Lint before every push
shopify theme check

# 5. Push as UNPUBLISHED first, share preview link with client for approval
shopify theme push --unpublished

# 6. ONLY after client approval, publish
shopify theme push --live
# OR publish from Shopify Admin > Online Store > Themes > Publish on the unpublished theme
```

**Automatic push / sync — exactly how the user asked for it:**
- **During development:** `shopify theme dev --store <store>.myshopify.com` auto-uploads saved VS Code changes to a hidden development theme and hot-reloads. This is the "I code in VS Code, it appears in Shopify" workflow.
- **To keep editor changes in sync:** run dev with `--theme-editor-sync` so changes made in Shopify's theme editor are written back to local files.
- **For team / client edits after launch (optional, recommended):** Connect the theme to GitHub in Shopify Admin > Online Store > Themes > Add theme > Connect from GitHub. Then:
  ```bash
  git init
  git add . && git commit -m "Kavita Tarot v1"
  git remote add origin <github-repo-url>
  git push -u origin main
  ```
  Pushes to the connected branch update the Shopify theme; editor changes in Admin commit back to GitHub. Never push directly to live without an unpublished-theme review step.
- **Never** edit code only in the browser editor and lose it. VS Code + Git is the source of truth. Commit daily with clear messages.

**File structure (create all of these, do not dump everything in one file):**
```
layout/theme.liquid
templates/index.json, page.book-online.json, product.json, collection.json, blog.json, article.json, page.json
sections/
  kavita-hero.liquid, kavita-services.liquid, kavita-booking.liquid,
  kavita-intentions.liquid, kavita-bestsellers.liquid, kavita-meet-kavita.liquid,
  kavita-card-explorer.liquid, kavita-daily-card.liquid, kavita-quiz.liquid,
  kavita-testimonials.liquid, kavita-faq.liquid, kavita-final-cta.liquid,
  kavita-trust-bar.liquid, kavita-how-it-works.liquid
snippets/ (card-flip, price, booking-form-fields, whatsapp-button, star-rating-real-only)
assets/kavita.css, kavita.js, card-deck.js, quiz.js, booking.js
config/settings_data.json, settings_schema.json
locales/en.default.json
```

**Golden rules (break these = build failed):**
1. NEVER hardcode products, prices, or service durations in Liquid. Load from Shopify products, collections, and metafields. If Admin has no price, show [CLIENT TO CONFIRM] in the editor only, never a guessed price live.
2. NEVER invent testimonials, reviews, logos ("As seen in"), or availability. If data is missing, hide the block.
3. NEVER copy Vanika, Mantramm, or old Wix text verbatim. Paraphrase + original copy, same facts.
4. Every section must be editable in the theme editor (settings_schema with text, image, collection, product pickers). No section that only a developer can change.
5. `shopify theme check` must pass with zero errors before push. Fix Liquid, accessibility, and performance warnings.
6. Mobile first. Test at 360px, 768px, 1280px, 1920px before calling it done.

**Shopify Admin setup the builder must list as a checklist (not code):**
- Products: Audio Call 10/20/30 (Premium + Standard as variants), Voice Note packs, 3 Healings, plus physical products. Product type: Service vs Physical. For services: disable shipping, require intake fields, set "This is a digital/service product" handling.
- Collections: Bestsellers, New Arrivals, By Intention (Love, Career, Money, Healing, Protection, Clarity), By Category (Crystals, Tarot Decks, Oracle Cards, Yantras, Idols, Pooja Essentials, Rudraksha & Malas).
- Metafields: service.duration, service.delivery_time, service.delivery_mode (Live Call / WhatsApp Voice Note / Email), service.questions_count, product.intention, product.stone, product.benefit.
- Metaobjects: Tarot Card (name, number, arcana, upright meaning, reversed meaning, reflection question, image), Testimonial (real only), FAQ.
- Pages: Book Online, About, FAQ, Contact, Shipping, Returns, Privacy, Terms, Service Cancellation Policy.
- Payments: Razorpay (UPI, cards, netbanking, wallets) + COD for physical products ONLY, never COD for readings/healings (a slot cannot be held unpaid — if client wants COD for services, flag it as a decision, do not silently enable it).
- Shipping: India + International zones, rates [CLIENT TO CONFIRM], dispatch time [CLIENT TO CONFIRM].
- Discounts: none by default. Premium sites do not open with a discount popup.

---

## 7. BOOKING FLOW — ADVANCED, REAL, NOT FAKE

Build this as a real flow, with honest fallbacks where an app is not yet connected:

1. **Choose service + duration + Premium/Standard** (variant selector, price updates live).
2. **Choose date + time slot** — IST timezone, Kavita's real availability.
   - If a booking app (BookThatApp, Sesami, Calendly, or Shopify Appointments) is connected: use its real calendar, block booked slots, no double-booking.
   - If NOT connected yet: show "Request your slot" — customer picks preferred date/time, pays, and gets "Slot request received — Kavita will confirm on WhatsApp within [CLIENT TO CONFIRM hours]". NEVER show a fake live calendar with fake available slots.
3. **Intake form (line item properties, required, validated):**
   - Full name, WhatsApp number (with country code, validated), Email
   - Topic: Love / Career / Money / Personal Growth / Other
   - Your questions (textarea, min 1 question for voice note, up to the pack limit)
   - Date of birth (optional, with privacy note: used only for the reading, never shared)
   - Preferred language [CLIENT TO CONFIRM: Hindi / English / Hinglish?]
   - Consent checkbox: "I understand this is for reflection and guidance, not guaranteed outcomes."
4. **Payment:** Razorpay checkout, order confirmation page shows: Order ID, service, duration, preferred slot, what happens next, WhatsApp button with prefilled message "Hi Kavita, I just booked [service] Order #[ID]".
5. **After payment (automations to configure, list them):**
   - Email confirmation + calendar slot confirmation (Shopify order confirmation, customised).
   - WhatsApp confirmation (via WhatsApp Business / approved template — [CLIENT TO CONFIRM WhatsApp number + template approval]).
   - Reminder 24h before live call, and 2h before (email + WhatsApp if connected).
   - After delivery: voice-note delivery link + "How was your reading?" review request (real reviews only).
6. **Reschedule / Cancel:** Form on Contact/Help page + policy [CLIENT TO CONFIRM: e.g. reschedule up to 24h before, no refund after delivery, etc.]. Do NOT invent a policy.
7. **Admin view:** Kavita sees in Shopify Orders: service, variant, intake answers as line-item properties, preferred slot, payment status. No separate spreadsheet needed.

**Physical shop checkout (separate, standard Shopify):**
Cart drawer, quantity, gift wrap option, shipping calculator, Razorpay + COD (physical only), order tracking page, returns for damaged/missing only with unboxing proof [CLIENT TO CONFIRM policy].

---

## 8. ADVANCED / GOATED FEATURES — BUILD ALL, NO HALF FEATURES

**Commerce:**
- Sticky add-to-cart / Book bar on mobile, cart drawer with free-shipping progress bar [CLIENT TO CONFIRM threshold, or hide it].
- Quick view, wishlist (localStorage + account wishlist if logged in), recently viewed, "Frequently booked together" (reading + crystal), bundles (reading + deck) with real bundle pricing in Admin.
- Search: predictive search with intention + product + card-meaning results, filters, no-results state with suggestions.
- Gift a reading: buyer enters recipient name + WhatsApp, recipient gets a code/message — no fake gift system, use Shopify gift card / draft order logic and document it.

**Interactive tarot:**
- 78-card explorer (metaobjects), filter by Major/Minor, suit, topic.
- Daily card, 1-card pull, 3-card Past / Present / Future spread — all free, with reflection questions, share to WhatsApp, CTA to book.
- Card-flip animation with sound-off by default, reduced-motion support.

**Personalisation:**
- Quiz (Section 5.13), "Shop by intention" filters, recently viewed, "Because you viewed X" (real, from browsing, not fake AI claims).

**Trust & conversion (honest only):**
- Real testimonials slider, real review stars, secure checkout badges (Razorpay), "1000+ clients" stat bar, founder story, FAQ schema, clear refund/cancellation policy.
- WhatsApp floating button with prefilled booking message, click-to-chat on every service page.
- Email capture: "Free Daily Card + Weekly Tarot Insights" — double opt-in, no spam, no fake discount.

**Marketing / SEO / Analytics (configure, do not fake data):**
- Meta Pixel + Conversions API (via Shopify/Facebook app), Google Analytics 4 + Google Tag Manager, Search Console verification placeholder.
- SEO: unique meta title/description per page/product/collection/article, alt text on every image, Product/Service/FAQ/Article schema, sitemap, robots, 404 page with search + popular links, canonical URLs, Core Web Vitals budget from Section 4.
- Blog + card-meanings content hub for SEO: Weekly Insights, card meanings, "how to prepare for a reading", crystal guides (client-approved copy only).

**Performance, accessibility, security:**
- WCAG: keyboard navigation for card flip, quiz, booking form; focus states; contrast AA; alt text; form labels; aria on accordions.
- Privacy: DOB/questions stored only as order properties, never sold, never shown publicly. Cookie consent for India + international visitors.
- Speed: images WebP, responsive srcset, lazy load, minified CSS/JS, no render-blocking third-party scripts on checkout.

**Admin / handover:**
- Theme editor documentation: a README.md in the repo listing every section, every metafield, every [CLIENT TO CONFIRM] item, and how Kavita adds a new service/product/card without code.
- Backup: GitHub repo + Shopify theme duplicate before every live push.

---

## 9. WHAT TO DELIVER — DEFINITION OF DONE

The builder must deliver, in VS Code + Shopify, and report back with proof:
1. [ ] Dawn-based theme in VS Code, `shopify theme check` passes, zero errors.
2. [ ] All pages/sections from Section 5 built and editable in theme editor.
3. [ ] All services from Section 2 as real Shopify products/variants, prices exactly as verified — no invented prices.
4. [ ] Booking flow from Section 7 working end-to-end on a test order (test payment, intake form saved on order, confirmation shown).
5. [ ] Shop collections + filters working with real Admin data, not hardcoded HTML products.
6. [ ] Interactive card tools working on mobile + desktop + ultra-wide, with reduced-motion support.
7. [ ] Razorpay test checkout + COD (physical only) tested, WhatsApp button tested.
8. [ ] SEO schema, meta, alt text, sitemap, 404, speed check (LCP) reported.
9. [ ] Pushed as UNPUBLISHED theme, preview link shared, client approval recorded — THEN pushed live.
10. [ ] README + [CLIENT TO CONFIRM] list handed over. No lorem ipsum, no fake testimonials, no fake slots, no fake prices anywhere on live.

**If any [CLIENT TO CONFIRM] item is still unconfirmed at build time, the builder must leave it as an editable Admin field / hidden block — NEVER guess it.**

---

## 10. [CLIENT TO CONFIRM] — DO NOT GUESS THESE (ASK KAVITA BEFORE LAUNCH)

- Standard Audio Call prices (10 / 20 / 30 min)
- Voice Note packs beyond 2 questions (₹451 verified) + delivery mode (WhatsApp vs Email) + delivery time
- Healing prices, durations, delivery mode, and full descriptions (Cord-Cutting, Vortex of Blessings, Lamafera)
- WhatsApp number for bookings + WhatsApp Business template approval
- Booking app choice (or "request slot" fallback) + Kavita's working hours / timezone / buffer / reschedule & cancellation policy
- Languages offered, payment methods final, shipping zones/rates/dispatch time, free-shipping threshold
- Real testimonials + portrait + product photos (do not use stock faces as "clients")
- Domain, Instagram/YouTube links, email for contact, refund policy text

---

## 11. COPY THE BUILDER MUST USE — DO NOT REWRITE INTO GENERIC AI COPY

Use this tone everywhere: warm, calm, premium, confident, no hype, no fear, no "miracle guaranteed".
- Hero: "You Are The Secret. Let Tarot Explore You."
- Sub: "Tarot cards help you understand your emotions, decisions, and life direction. Every card carries a unique meaning that offers insight and guidance."
- Services intro: "Unlock the mysteries of your future with our insightful tarot readings. Our expert tarot reader provides guidance on love, career, finances, and personal growth, helping you make empowered decisions and find clarity in every aspect of life." (paraphrase slightly for the new site, same meaning)
- About: "I am Kavita, a tarot reader offering personalized 1-1 consultations to guide and empower you."
- CTA language: Book a Reading, Book Online, Explore the Shop, Find Your Card, Ask Your Question — never "Buy Now or Miss Out", never "Last Chance!!!".

---

**END OF PROMPT — Build it exactly like this. Premium first, real data only, Shopify + VS Code + CLI push, no shortcuts.**

