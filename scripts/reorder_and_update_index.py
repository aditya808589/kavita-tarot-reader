import re

with open('index.html') as f:
    text = f.read()

# 1. Extract the consultations section
cons_pattern = re.compile(r'<!-- =+\s*6\. INTERACTIVE SLIDER 1.*?<\/section>', re.DOTALL)
cons_match = cons_pattern.search(text)
assert cons_match, 'Could not find consultations section'

# Remove the consultations section from its current position
text_without_cons = text[:cons_match.start()] + text[cons_match.end():]

# Construct the enhanced consultations-slider (without the urgent banner, with Live Video Call slide added, labels set to Urgent Within 24 Hrs)
new_consultations_block = '''<!-- =========================================================
       6. INTERACTIVE SLIDER: FEATURED 1-ON-1 READINGS & ENERGY HEALING
       ✦ Personal Guidance Directly with Kavita ✦ (Placed After Zodiac Section)
  ========================================================= -->
  <section id="consultations-slider" class="section-wrap" style="background: #FFFFFF;">
    <div class="container">
      <div class="section-header">
        <div class="section-kicker">✦ Personal Guidance Directly with Kavita ✦</div>
        <h2 class="section-title">Featured Consultations & Energy Sessions</h2>
        <p class="section-sub">Private 1-on-1 intuitive audio and video readings straight to WhatsApp, alongside master distance energy healing sessions.</p>
      </div>

      <div class="kavita-carousel-outer">
        <!-- Navigation Chevrons -->
        <button class="kavita-carousel-arrow prev" onclick="moveCarousel('consultationsTrack', -1)" aria-label="Previous Offerings">‹</button>
        <button class="kavita-carousel-arrow next" onclick="moveCarousel('consultationsTrack', 1)" aria-label="Next Offerings">›</button>

        <!-- Carousel Track -->
        <div class="kavita-carousel-track" id="consultationsTrack">

          <!-- 1. Live Audio Call Tarot Reading -->
          <div class="kavita-carousel-slide">
            <div class="product-card" style="height: 100%; display: flex; flex-direction: column;">
              <div class="product-media">
                <span class="product-badge-flag">Live Audio Consultation</span>
                <button type="button" class="product-wishlist-heart" aria-label="Add to Wishlist" onclick="toggleWishlist(this, 1)">♡</button>
                <a href="product.html?id=1">
                  <img loading="lazy" decoding="async" class="product-img" src="assets/product-call-10min.jpg" alt="Live Audio Call Tarot Reading">
                </a>
              </div>
              <div class="product-info-wrap" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div class="product-category-sub">1-on-1 Live WhatsApp Audio</div>
                  <h4 class="product-title">
                    <a href="product.html?id=1">Live Audio Call Tarot Reading with Kavita</a>
                  </h4>
                  <div class="product-reviews-stars">★★★★★ <span class="product-reviews-count">(420 reviews)</span></div>
                  <div class="product-pricing-row">
                    <span class="current-price">₹999 – ₹4,444</span>
                    <span class="discount-pill">Urgent (Within 24 Hrs) Avail.</span>
                  </div>
                  <div class="product-features-bullet">
                    <span>10 Mins (₹999 / ₹1,555) · 20 Mins (₹2,299 / ₹3,099) · 30 Mins (₹3,369 / ₹4,444)</span>
                    <span>Direct intuitive answers to pressing love, career & life questions</span>
                  </div>
                </div>
                <div class="product-card-actions">
                  <button class="btn btn-maroon" onclick="openBookingModal('Live Audio Call Tarot Reading')">
                    ✦ Book Call
                  </button>
                  <a href="consultations.html" class="btn btn-outline">
                    Details
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- 2. Live Video Call Tarot Reading with Kavita -->
          <div class="kavita-carousel-slide">
            <div class="product-card" style="height: 100%; display: flex; flex-direction: column; border: 1.5px solid #D4AF37;">
              <div class="product-media">
                <span class="product-badge-flag" style="background: #80142B; color: #FFF;">Face to Face Clarity</span>
                <button type="button" class="product-wishlist-heart" aria-label="Add to Wishlist" onclick="toggleWishlist(this, 3)">♡</button>
                <a href="consultations.html">
                  <img loading="lazy" decoding="async" class="product-img" src="assets/product-call-30min.jpg" alt="Live Video Call Tarot Reading with Kavita">
                </a>
              </div>
              <div class="product-info-wrap" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div class="product-category-sub">Direct WhatsApp Video Session</div>
                  <h4 class="product-title">
                    <a href="consultations.html">Live Video Call Tarot Reading with Kavita</a>
                  </h4>
                  <div class="product-reviews-stars">★★★★★ <span class="product-reviews-count">(340 reviews)</span></div>
                  <div class="product-pricing-row">
                    <span class="current-price">₹1,888 – ₹5,499</span>
                    <span class="discount-pill">Standard & Urgent (24 Hrs)</span>
                  </div>
                  <div class="product-features-bullet">
                    <span>10 Mins: Standard ₹1,888 | Urgent (Within 24 Hrs) ₹2,199</span>
                    <span>30 Mins: Standard ₹4,499 | Urgent (Within 24 Hrs) ₹5,499</span>
                  </div>
                </div>
                <div class="product-card-actions">
                  <button class="btn btn-gold" onclick="openBookingModal('Live Video Call Tarot Reading')">
                    ✦ Book Video Call
                  </button>
                  <a href="consultations.html" class="btn btn-outline">
                    Details
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- 3. WhatsApp Voice Note Tarot Reading -->
          <div class="kavita-carousel-slide">
            <div class="product-card" style="height: 100%; display: flex; flex-direction: column;">
              <div class="product-media">
                <span class="product-badge-flag">From ₹299 · 7 Days Delivery</span>
                <button type="button" class="product-wishlist-heart" aria-label="Add to Wishlist" onclick="toggleWishlist(this, 4)">♡</button>
                <a href="product.html?id=4">
                  <img loading="lazy" decoding="async" class="product-img" src="assets/product-voice-2q.jpg" alt="WhatsApp Voice Note Tarot Reading">
                </a>
              </div>
              <div class="product-info-wrap" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div class="product-category-sub">WhatsApp Voice Memo</div>
                  <h4 class="product-title">
                    <a href="product.html?id=4">Personalised WhatsApp Voice Note Reading</a>
                  </h4>
                  <div class="product-reviews-stars">★★★★★ <span class="product-reviews-count">(520 reviews)</span></div>
                  <div class="product-pricing-row">
                    <span class="current-price">From ₹299</span>
                    <span class="discount-pill">Urgent in 24 Hrs ₹499</span>
                  </div>
                  <div class="product-features-bullet">
                    <span>1 Q ₹299 · 2 Qs ₹399 · 3 Qs ₹499 · Extra Qs ₹299 each</span>
                    <span>Delivered as voice note in 7 days (or 24-hr urgent)</span>
                  </div>
                </div>
                <div class="product-card-actions">
                  <button class="btn btn-maroon" onclick="openBookingModal('WhatsApp Voice Note Reading (from ₹299)')">
                    ✦ Book Note
                  </button>
                  <a href="consultations.html" class="btn btn-outline">
                    Details
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- 4. Distance Cord-Cutting Healing -->
          <div class="kavita-carousel-slide">
            <div class="product-card" style="height: 100%; display: flex; flex-direction: column;">
              <div class="product-media">
                <span class="product-badge-flag">Complete Healing Session</span>
                <button type="button" class="product-wishlist-heart" aria-label="Add to Wishlist" onclick="toggleWishlist(this, 10)">♡</button>
                <a href="product.html?id=10">
                  <img loading="lazy" decoding="async" class="product-img" src="assets/product-cord-cutting.jpg" alt="Distance Cord-Cutting Healing">
                </a>
              </div>
              <div class="product-info-wrap" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div class="product-category-sub">Remote Pranic Healing</div>
                  <h4 class="product-title">
                    <a href="product.html?id=10">Distance Cord-Cutting Healing Session</a>
                  </h4>
                  <div class="product-reviews-stars">★★★★★ <span class="product-reviews-count">(194 reviews)</span></div>
                  <div class="product-pricing-row">
                    <span class="current-price">₹5,001</span>
                    <span class="compare-price">₹7,500</span>
                    <span class="discount-pill">33% OFF</span>
                  </div>
                  <div class="product-features-bullet">
                    <span>Severs ethereal ties to past relationships & toxic ties</span>
                    <span>Restores emotional equilibrium & peace with Beeja Mantras</span>
                  </div>
                </div>
                <div class="product-card-actions">
                  <button class="btn btn-maroon" onclick="openBookingModal('Distance Cord-Cutting Session (₹5,001)')">
                    ✦ Reserve Session
                  </button>
                  <a href="product.html?id=10" class="btn btn-outline">
                    Details
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- 5. Personalised Sacred Energy Circle -->
          <div class="kavita-carousel-slide">
            <div class="product-card" style="height: 100%; display: flex; flex-direction: column;">
              <div class="product-media">
                <span class="product-badge-flag">Coded Energy Circle</span>
                <button type="button" class="product-wishlist-heart" aria-label="Add to Wishlist" onclick="toggleWishlist(this, 8)">♡</button>
                <a href="product.html?id=8">
                  <img loading="lazy" decoding="async" class="product-img" src="assets/product-energy-circle.jpg" alt="Personalised Sacred Energy Circle">
                </a>
              </div>
              <div class="product-info-wrap" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div class="product-category-sub">Sacred Geometric Alignment</div>
                  <h4 class="product-title">
                    <a href="product.html?id=8">Personalised Sacred Energy Circle</a>
                  </h4>
                  <div class="product-reviews-stars">★★★★★ <span class="product-reviews-count">(167 reviews)</span></div>
                  <div class="product-pricing-row">
                    <span class="current-price">₹1,416</span>
                    <span class="compare-price">₹1,888</span>
                    <span class="discount-pill">25% OFF</span>
                  </div>
                  <div class="product-features-bullet">
                    <span>Opens stagnant abundance pathways</span>
                    <span>Personalized sacred symbol and switchword guidance</span>
                  </div>
                </div>
                <div class="product-card-actions">
                  <button class="btn btn-maroon" onclick="openBookingModal('Personalised Sacred Energy Circle')">
                    ✦ Reserve Circle
                  </button>
                  <a href="product.html?id=8" class="btn btn-outline">
                    Details
                  </a>
                </div>
              </div>
            </div>
          </div>

          <!-- 6. Ancient Nordic Rune Reading -->
          <div class="kavita-carousel-slide">
            <div class="product-card" style="height: 100%; display: flex; flex-direction: column;">
              <div class="product-media">
                <span class="product-badge-flag">Elder Futhark</span>
                <button type="button" class="product-wishlist-heart" aria-label="Add to Wishlist" onclick="toggleWishlist(this, 7)">♡</button>
                <a href="product.html?id=7">
                  <img loading="lazy" decoding="async" class="product-img" src="assets/product-rune-reading.jpg" alt="Ancient Nordic Rune Reading">
                </a>
              </div>
              <div class="product-info-wrap" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                  <div class="product-category-sub">Primal Norse Divination</div>
                  <h4 class="product-title">
                    <a href="product.html?id=7">Ancient Nordic Rune Reading Session</a>
                  </h4>
                  <div class="product-reviews-stars">★★★★★ <span class="product-reviews-count">(118 reviews)</span></div>
                  <div class="product-pricing-row">
                    <span class="current-price">₹3,333</span>
                    <span class="compare-price">₹4,999</span>
                    <span class="discount-pill">Special</span>
                  </div>
                  <div class="product-features-bullet">
                    <span>Deep karmic roots, hidden obstacles & primal alignment</span>
                    <span>Detailed photo spread and voice recording included</span>
                  </div>
                </div>
                <div class="product-card-actions">
                  <button class="btn btn-maroon" onclick="openBookingModal('Ancient Nordic Rune Reading')">
                    ✦ Reserve Reading
                  </button>
                  <a href="product.html?id=7" class="btn btn-outline">
                    Details
                  </a>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div style="text-align: center; margin-top: 2.8rem;">
        <a href="consultations.html" class="btn btn-maroon" style="padding: 0.95rem 2.5rem;">
          ✦ View Dedicated Consultations Portal & Intake Form →
        </a>
      </div>
    </div>
  </section>'''

# Find the end of shop-by-zodiac section in text_without_cons
zodiac_start = text_without_cons.find('id="shop-by-zodiac"')
assert zodiac_start != -1, 'Could not find id="shop-by-zodiac"'
zodiac_end = text_without_cons.find('</section>', zodiac_start) + len('</section>')

# Insert new_consultations_block right after zodiac_end
final_text = text_without_cons[:zodiac_end] + '\n\n  ' + new_consultations_block + text_without_cons[zodiac_end:]

with open('index.html', 'w') as f:
    f.write(final_text)

print('SUCCESS: consultations-slider relocated after shop-by-zodiac and updated with video call & urgent labels!')

