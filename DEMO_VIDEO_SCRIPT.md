# Demo Video Script — RE Lead Enrichment Tool

**Duration:** 60-90 seconds  
**Format:** Screen recording with voiceover  
**Goal:** Show value prop + how it works + call to action

---

## Hook (0-5 seconds)

**VISUAL:** Title card with text overlay  
**TEXT ON SCREEN:** "Stop paying $0.15-0.30 per lead"

**VOICEOVER:**
> "Still paying for skip tracing? Here's a better way."

---

## Problem (5-15 seconds)

**VISUAL:** Screenshot of BatchSkipTracing pricing page (or competitor)  
**TEXT ON SCREEN:** "1,000 leads × $0.20 = $200 wasted"

**VOICEOVER:**
> "Services like BatchSkipTracing charge 15 to 30 cents per lead. For a thousand leads, that's $150 to $300. Every single time."

---

## Solution (15-25 seconds)

**VISUAL:** Landing page hero section  
**TEXT ON SCREEN:** "RE Lead Enrichment Tool — $49 one-time"

**VOICEOVER:**
> "RE Lead Enrichment finds phone numbers and emails for your property owner lists. One-time $49 payment. Unlimited use."

---

## Demo Part 1: Upload (25-35 seconds)

**VISUAL:** Terminal or GUI showing CSV import  
**COMMAND:**
```bash
python3 lead_enrichment.py import leads.csv
```

**OUTPUT:**
```
✅ Loaded 25 leads from leads.csv
📊 Ready to enrich 25 leads
```

**VOICEOVER:**
> "Upload your CSV file with owner names and cities. The tool handles the rest."

---

## Demo Part 2: Automation (35-50 seconds)

**VISUAL:** Terminal showing batch processing in action  
**COMMAND:**
```bash
python3 lead_enrichment.py enrich-batch leads.csv
```

**OUTPUT:**
```
🔍 Enriching leads (batch mode)...
✅ John Smith (Orlando) → (407) 555-1234, john.smith@email.com
✅ Jane Doe (Tampa) → (813) 555-5678, jane.doe@email.com
✅ Bob Johnson (Miami) → (305) 555-9012
⏳ Progress: 3/25 (12%) | ETA: 4 min 30 sec
```

**VOICEOVER:**
> "Browser automation finds phone numbers, emails, and addresses automatically. 15 to 30 seconds per lead."

---

## Demo Part 3: Export (50-60 seconds)

**VISUAL:** Terminal showing export, then CSV file opened in Excel/Numbers  
**COMMAND:**
```bash
python3 lead_enrichment.py export leads.csv enriched_leads.csv
```

**CSV PREVIEW (in spreadsheet):**
| Name | City | State | Phone | Email | Address |
|------|------|-------|-------|-------|---------|
| John Smith | Orlando | FL | (407) 555-1234 | john.smith@email.com | 123 Main St |
| Jane Doe | Tampa | FL | (813) 555-5678 | jane.doe@email.com | 456 Oak Ave |

**VOICEOVER:**
> "Export enriched results to CSV. Import to your CRM or dialer. Start calling."

---

## Savings Comparison (60-70 seconds)

**VISUAL:** Side-by-side comparison graphic  
**TEXT ON SCREEN:**
```
BatchSkipTracing: 1,000 leads × $0.20 = $200 (recurring)
RE Lead Enrichment: 1,000 leads = $49 (one-time)
💰 You Save: $151
```

**VOICEOVER:**
> "On a thousand-lead batch, you save $101 to $251 compared to BatchSkipTracing. One-time payment. Unlimited use."

---

## Call to Action (70-90 seconds)

**VISUAL:** Landing page with pricing tiers  
**TEXT ON SCREEN:**
- Free: 5/day manual lookups
- Pro: $49 one-time, unlimited automated
- Enterprise: $149 one-time, PropertyGlance integration

**VOICEOVER:**
> "Get started for free. Upgrade to Pro for 49 bucks. No subscriptions. No per-lead fees. Link in the description."

**FINAL TEXT ON SCREEN:**
```
🌐 landing-page-nine-beta-80.vercel.app
💰 Get Pro Edition: gumroad.com/l/re-lead-enrichment
```

---

## Screen Recording Checklist

- [ ] Record in 1920x1080 (1080p)
- [ ] Use clean terminal (no distractions in background)
- [ ] Terminal font size 16-18pt (readable on mobile)
- [ ] Use macOS Terminal or iTerm2 with clean theme
- [ ] Slow down typing (don't paste, type at normal speed)
- [ ] Add subtle background music (royalty-free, low volume)
- [ ] Export as MP4 (H.264, high quality)
- [ ] Add captions for accessibility

---

## Recording Tools

**macOS:**
- QuickTime (built-in, free)
- ScreenFlow ($169, professional)
- OBS Studio (free, open-source)

**Voiceover:**
- GarageBand (macOS, free)
- Audacity (free, cross-platform)

**Editing:**
- iMovie (macOS, free)
- DaVinci Resolve (free)
- Final Cut Pro ($299, professional)

---

## Alternative: Loom Recording (Faster)

If you want to skip video editing:

1. Sign up for Loom (free tier: 5-min videos)
2. Record screen + webcam + voiceover in one take
3. Upload to Loom, get shareable link
4. Embed on Product Hunt, landing page, Twitter

**Pros:** Fast (no editing), looks personal (face on camera), easy sharing  
**Cons:** 5-min limit on free tier, less polished

---

## Sample Loom Flow (60 seconds)

1. **Intro (5s):** Hi, I'm Luis. I built this tool because I was tired of paying for skip tracing.
2. **Problem (10s):** BatchSkipTracing charges 15-30 cents per lead. For a thousand leads, that's $150-300 every time.
3. **Solution (10s):** RE Lead Enrichment finds phone numbers for $49 one-time. Let me show you.
4. **Demo (30s):** [Screen share] Upload CSV → Run automation → Export results
5. **CTA (5s):** Link in the description. Try the free tier, upgrade to Pro for $49. Thanks!

---

## Estimated Time to Create

**Option 1: Polished video (iMovie/DaVinci)**  
- Screen recording: 10 min
- Voiceover recording: 5 min
- Editing (cuts, transitions, music): 30 min
- **Total: 45 minutes**

**Option 2: Loom one-take**  
- Script review: 5 min
- Recording (one take, maybe 2-3 tries): 10 min
- **Total: 15 minutes**

**Recommendation:** Start with Loom for speed, upgrade to polished video later if needed.

---

## Where to Use This Video

1. **Product Hunt submission** (required for launch)
2. **Landing page hero section** (embed YouTube/Loom)
3. **Twitter/X post** (native video upload)
4. **LinkedIn post** (native video upload)
5. **Reddit r/realestateinvesting** (link to YouTube)
6. **BiggerPockets forum** (embed YouTube)
7. **Email to leads** (link to Loom/YouTube)

---

**Ready to record? Follow this script and you'll have a demo video in 15-45 minutes.**
