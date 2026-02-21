# Launch Checklist — RE Lead Enrichment Tool

**Goal:** First sale by end of Feb 21, 2026  
**Target:** $49 (one Pro sale) to prove product-market fit  
**Estimated total time:** 2 hours (all materials ready, just execute)

---

## ✅ Pre-Launch (DONE)

- [x] Browser automation built (Feb 20 12:40 AM)
- [x] Landing page deployed (Feb 20 11:03 PM)
- [x] Gumroad setup guide written (GUMROAD_SETUP.md)
- [x] Product .zip file created (re-lead-enrichment-pro.zip)
- [x] Product Hunt template ready (PRODUCT_HUNT.md)
- [x] Marketing posts written (MARKETING_POSTS.md)
- [x] Demo video script ready (DEMO_VIDEO_SCRIPT.md)
- [x] GitHub repo created (github.com/Luij78/re-lead-enrichment)

**Status:** READY TO LAUNCH 🚀

---

## 🔍 Step 1: QA Browser Automation (30 min)

**Why:** Verify browser automation works before selling to customers

**Tasks:**
- [ ] Open Chrome browser
- [ ] Click OpenClaw extension icon (attach Chrome relay)
- [ ] Run test lookup:
  ```bash
  cd ~/.openclaw/workspace/skills/lead-enrichment
  python3 lead_enrichment.py enrich-batch test_leads.csv --profile chrome
  ```
- [ ] Verify results:
  - [ ] Phone numbers extracted correctly
  - [ ] Email addresses extracted (if available)
  - [ ] Addresses extracted (if available)
  - [ ] CSV export works
- [ ] Fix any bugs found
- [ ] Re-test until clean run

**Success Criteria:** 3/5 test leads return valid phone numbers

---

## 💰 Step 2: Create Gumroad Product (15 min)

**Instructions:** Follow GUMROAD_SETUP.md step-by-step

**Tasks:**
- [ ] Go to gumroad.com/products/new
- [ ] Copy/paste product name, description from GUMROAD_SETUP.md
- [ ] Set price: $49
- [ ] Upload re-lead-enrichment-pro.zip
- [ ] Configure product settings (category, tags)
- [ ] Connect Stripe (if not already)
- [ ] Publish product
- [ ] Copy product URL: `gumroad.com/l/re-lead-enrichment`
- [ ] Test purchase with test card (4242 4242 4242 4242)
- [ ] Verify download works

**Success Criteria:** Product is live and purchase flow works

---

## 🌐 Step 3: Update Landing Page CTAs (5 min)

**Why:** Point "Get Pro Edition" buttons to live Gumroad product

**Tasks:**
- [ ] Open `~/.openclaw/workspace/skills/lead-enrichment/landing-page/index.html`
- [ ] Find all instances of `<a href="#"` in CTA buttons
- [ ] Replace with `<a href="https://gumroad.com/l/re-lead-enrichment"`
- [ ] Save file
- [ ] Deploy update:
  ```bash
  cd ~/.openclaw/workspace/skills/lead-enrichment/landing-page
  vercel --prod
  ```
- [ ] Verify buttons work (click through to Gumroad)

**Success Criteria:** All CTA buttons link to live Gumroad product

---

## 🚀 Step 4: Product Hunt Launch (30 min)

**Instructions:** Follow PRODUCT_HUNT.md template

**Tasks:**
- [ ] Go to producthunt.com/posts/new
- [ ] Copy/paste product details from PRODUCT_HUNT.md:
  - [ ] Name: RE Lead Enrichment Tool
  - [ ] Tagline: Stop paying $0.15-0.30/lead for skip tracing
  - [ ] Description (full copy from PRODUCT_HUNT.md)
  - [ ] First comment (maker's comment from PRODUCT_HUNT.md)
- [ ] Upload thumbnail image (create simple graphic)
- [ ] Upload gallery images (screenshots of tool in action)
- [ ] Link to landing page: https://landing-page-nine-beta-80.vercel.app
- [ ] Link to Gumroad: https://gumroad.com/l/re-lead-enrichment
- [ ] Add topics: real estate, developer tools, productivity
- [ ] Schedule launch for 12:01 AM PT (best time for visibility)
- [ ] (Optional) Upload demo video if created

**Success Criteria:** Product Hunt listing is live and accepting upvotes

---

## 📣 Step 5: Marketing Posts (30 min)

**Instructions:** Use pre-written copy from MARKETING_POSTS.md

### BiggerPockets Forum (10 min)
- [ ] Go to biggerpockets.com/forums
- [ ] Post in "Technology" or "General Real Estate Investing" forum
- [ ] Copy/paste BiggerPockets post from MARKETING_POSTS.md
- [ ] Add links to landing page + Gumroad
- [ ] Post

### Reddit r/realestateinvesting (5 min)
- [ ] Go to reddit.com/r/realestateinvesting
- [ ] Create new post
- [ ] Copy/paste Reddit post from MARKETING_POSTS.md
- [ ] Add links
- [ ] Post

### Twitter/X Thread (10 min)
- [ ] Go to twitter.com
- [ ] Create thread (6 tweets)
- [ ] Copy/paste Twitter thread from MARKETING_POSTS.md
- [ ] Add landing page link in final tweet
- [ ] Post thread

### LinkedIn (5 min)
- [ ] Go to linkedin.com
- [ ] Create new post
- [ ] Copy/paste LinkedIn post from MARKETING_POSTS.md
- [ ] Add landing page link
- [ ] Post

**Success Criteria:** 4 marketing posts live on different platforms

---

## 🧪 Step 6: Dogfooding (Optional, 1-2 hours)

**Why:** Test tool on real data, find bugs, create case study

**Tasks:**
- [ ] Load Luis's 2,421 homestead leads:
  ```bash
  python3 lead_enrichment.py import ~/Documents/homestead-leads-filtered.csv
  ```
- [ ] Run batch enrichment (overnight if needed):
  ```bash
  python3 lead_enrichment.py enrich-batch homestead-leads.csv --profile chrome
  ```
- [ ] Monitor progress, fix bugs
- [ ] Export results:
  ```bash
  python3 lead_enrichment.py export homestead-leads.csv homestead-enriched.csv
  ```
- [ ] Calculate metrics:
  - [ ] % of leads with phone numbers found
  - [ ] % with emails found
  - [ ] Time per lead
  - [ ] Total cost savings vs BatchSkipTracing
- [ ] Write case study for marketing (optional)

**Success Criteria:** 2,421 leads enriched, ready to import to REPal

---

## 📊 Step 7: Track Metrics (Ongoing)

**Metrics to Watch:**
- [ ] Gumroad sales (check daily)
- [ ] Landing page traffic (Vercel analytics)
- [ ] Product Hunt upvotes (check hourly on launch day)
- [ ] Marketing post engagement (comments, upvotes)
- [ ] GitHub stars

**Tools:**
- Gumroad dashboard: gumroad.com/dashboard
- Vercel analytics: vercel.com/luij78s-projects/landing-page
- Product Hunt: producthunt.com (notifications)

---

## 🎯 Success Metrics

**Day 1 (Feb 21):**
- [ ] Product Hunt listing live
- [ ] 4+ marketing posts published
- [ ] Landing page traffic >50 visits
- [ ] **First sale ($49)** 🎉

**Week 1 (Feb 21-27):**
- [ ] 10 Pro sales ($490)
- [ ] 5 Enterprise sales ($745)
- [ ] **Total: $1,235** (exceeds $1K Feb target)

**Month 1 (Feb 21 - Mar 21):**
- [ ] 50 Pro sales ($2,450)
- [ ] 10 Enterprise sales ($1,490)
- [ ] Product Hunt feature (if high engagement)
- [ ] 100+ GitHub stars

---

## 🚨 Troubleshooting

**If Gumroad sales are slow:**
- [ ] Check landing page conversion rate (Vercel analytics)
- [ ] A/B test pricing ($39 vs $49)
- [ ] Add testimonials (ask early buyers for reviews)
- [ ] Create demo video (follow DEMO_VIDEO_SCRIPT.md)
- [ ] Run Reddit ads (r/realestateinvesting, $20 budget)

**If browser automation fails:**
- [ ] Check OpenClaw browser tool is working (`openclaw tool browser --action status`)
- [ ] Verify Chrome relay is connected (click extension icon)
- [ ] Check TruePeopleSearch isn't blocking (try different search)
- [ ] Add retry logic (already in code, may need tuning)

**If buyers report issues:**
- [ ] Check OpenClaw installation instructions in README
- [ ] Offer 1-on-1 setup call (15 min, free)
- [ ] Create troubleshooting FAQ (add to landing page)
- [ ] Issue refund if can't resolve (maintain 100% satisfaction)

---

## 📝 Post-Launch Checklist

**After First Sale:**
- [ ] Thank buyer (email or Twitter DM)
- [ ] Ask for feedback (what worked, what didn't)
- [ ] Request testimonial (offer $10 discount on next product)
- [ ] Add testimonial to landing page + GUMROAD_LISTING.md

**After 10 Sales:**
- [ ] Analyze buyer demographics (where did they come from?)
- [ ] Double down on highest-converting channel
- [ ] Create case study blog post
- [ ] Consider building Enterprise features (API, PropertyGlance)

**After $1K Revenue:**
- [ ] Celebrate 🎉 (Feb goal achieved)
- [ ] Analyze metrics (conversion rate, traffic sources)
- [ ] Plan next product (use revenue-pipeline skill)
- [ ] Reinvest profits into marketing (Reddit ads, Product Hunt boost)

---

## ⏱️ Time Estimate Summary

| Step | Time | Status |
|------|------|--------|
| 1. QA Browser Automation | 30 min | ⏳ To Do |
| 2. Create Gumroad Product | 15 min | ⏳ To Do |
| 3. Update Landing Page CTAs | 5 min | ⏳ To Do |
| 4. Product Hunt Launch | 30 min | ⏳ To Do |
| 5. Marketing Posts | 30 min | ⏳ To Do |
| 6. Dogfooding (optional) | 1-2 hrs | ⏸️ Optional |
| **Total (required)** | **1 hr 50 min** | |

**All materials are ready. Just execute the checklist. First sale possible by end of day Feb 21.**

---

## 🎯 Priority for Feb 21

1. **QA browser automation** (30 min) — Must work before selling
2. **Create Gumroad product** (15 min) — Enables first sale
3. **Update landing page CTAs** (5 min) — Drives traffic to Gumroad
4. **Product Hunt launch** (30 min) — Primary traffic source
5. **Marketing posts** (30 min) — Secondary traffic sources

**Total: 1 hr 50 min → First sale possible by 2 PM on Feb 21**

Then focus on Gold Coast if time permits.
