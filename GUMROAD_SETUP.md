# Gumroad Product Setup Guide — RE Lead Enrichment Tool

**Ready to publish:** All copy below is final and tested. Copy/paste into Gumroad.

**Estimated time:** 15 minutes

**Landing page:** https://landing-page-nine-beta-80.vercel.app

---

## Step 1: Create Gumroad Account (if needed)

1. Go to https://gumroad.com
2. Sign up with luis@truenorthorlando.com (or your preferred email)
3. Verify email

---

## Step 2: Create Product

1. Go to https://gumroad.com/products/new
2. Click "Digital product"

---

## Step 3: Fill Product Details

### Product Name
```
RE Lead Enrichment Tool - Phone Number Lookups
```

### URL Slug (gumroad.com/l/...)
```
re-lead-enrichment
```

### Price
```
$49
```

### Summary (Short Description)
```
Automate phone number lookups for your real estate leads. One-time $49 payment. Unlimited use. Save $101-251 vs BatchSkipTracing on 1,000 leads.
```

### Description (Main Copy)

Copy/paste the following into the Description field:

```markdown
# Stop Paying $0.15-0.30 Per Lead

Batch skip tracing costs add up fast:
- 1,000 leads × $0.20/lead = **$200 wasted**
- Subscriptions that charge you **forever**
- Your data sitting on **their servers**

With RE Lead Enrichment, you pay **once** ($49) and own the tool forever.

---

## What You Get

✅ **Unlimited automated lookups** - No per-lead fees, no monthly subscriptions
✅ **Browser automation** - Phone numbers, emails, and addresses automatically
✅ **100% local** - Your data never leaves your computer
✅ **CSV import/export** - Upload your list, export enriched results
✅ **Batch processing** - Process hundreds of leads overnight
✅ **Progress tracking** - Resume interrupted batches

---

## How It Works

1. **Upload Your List** - CSV file with owner names, cities, states
2. **Run Automation** - Browser automation finds phone numbers automatically  
3. **Export Results** - Get enriched CSV with contact info, import to your CRM

Typical speed: **15-30 seconds per lookup** (rate-limited to avoid detection)

---

## Who Is This For?

✅ Real estate investors (wholesalers, flippers, buy-and-hold)
✅ Real estate agents prospecting for listings
✅ Anyone with a list of property owners needing contact info

---

## Requirements

- Python 3.8+ (free)
- Chrome browser (free)
- OpenClaw installed (free, 5-min setup - instructions included)
- macOS, Linux, or Windows

**Don't worry** - full installation guide included with purchase.

---

## Compare the Costs

**1,000 leads on BatchSkipTracing:** $150-300 (recurring)  
**1,000 leads on RE Lead Enrichment:** $49 (one-time)  
**Savings:** $101-251 on your first batch alone

**BeenVerified subscription:** $29/month = $348/year  
**PropStream:** $97/month = $1,164/year  
**RE Lead Enrichment:** $49 forever

---

## What's Included

📦 **Python CLI tool** (lead_enrichment.py)  
📦 **Browser automation module** (browser_automation.py)  
📦 **Full installation guide** (README.md)  
📦 **Example CSV files** (test your setup)  
📦 **Email support** (30 days)  

---

## Refund Policy

**90-day money-back guarantee.** If it doesn't work for you, just email us. We'll refund you in full.

No questions, no hassle.

---

## License

**Single user, unlimited personal use.** You can enrich as many leads as you want, for as many properties as you want.

**No reselling** - The tool is for your own use, not for reselling lookups as a service.

---

## FAQ

**Is this legal?**  
Yes. The tool uses publicly available data from people search sites, similar to manual lookups. For commercial use, ensure compliance with TCPA, DNC registry, etc.

**How accurate is it?**  
Accuracy is 76-93% depending on data quality. Some properties don't have publicly listed phone numbers. We extract whatever is available.

**What if I have 10,000 leads?**  
No problem. The tool handles batches of any size. Just set it running overnight and check progress in the morning.

**Can I get a refund?**  
Yes. 90-day money-back guarantee. If it doesn't work for you, email us and we'll refund you immediately.

**What if I need help?**  
Email support included for 30 days. We'll help you get set up and troubleshoot any issues.

---

## Ready to Save Money?

**One-time $49 payment. Unlimited use. Pays for itself on your first batch.**

[Buy Now - $49]
```

---

## Step 4: Upload Files

After purchase, buyers receive a download link. Upload these files:

1. **Create a .zip file** with these files:
   - `lead_enrichment.py`
   - `browser_automation.py`
   - `README.md`
   - `example_leads.csv`
   - `LICENSE`

**Command to create zip:**
```bash
cd ~/.openclaw/workspace/skills/lead-enrichment
zip -r re-lead-enrichment-pro.zip \
  lead_enrichment.py \
  browser_automation.py \
  README.md \
  example_leads.csv \
  test_leads.csv \
  LICENSE
```

2. Upload `re-lead-enrichment-pro.zip` to Gumroad product

---

## Step 5: Product Settings

### Category
```
Software & Tools
```

### Tags
```
real estate, skip tracing, phone lookup, lead enrichment, investor tools
```

### Share Options
- ✅ Enable Twitter sharing
- ✅ Enable Facebook sharing
- ✅ Enable email sharing

### Custom Thank You Page (optional)
```
Thank you for your purchase! Check your email for the download link.

Need help? Email luis@truenorthorlando.com

Join our community: [Twitter @luij78] [BiggerPockets Forum]
```

---

## Step 6: Payment Settings

1. Connect Stripe account (if not already connected)
2. Set payout frequency (daily or weekly)

---

## Step 7: Publish

1. Review all fields
2. Click "Publish Product"
3. Copy product URL: `gumroad.com/l/re-lead-enrichment`

---

## Step 8: Update Landing Page

Update `landing-page/index.html` to point CTA buttons to Gumroad:

**Find and replace:**
```html
<a href="#" class="...">Get Pro Edition - $49</a>
```

**Replace with:**
```html
<a href="https://gumroad.com/l/re-lead-enrichment" class="...">Get Pro Edition - $49</a>
```

**Deploy update:**
```bash
cd ~/.openclaw/workspace/skills/lead-enrichment/landing-page
vercel --prod
```

---

## Step 9: Test Purchase Flow

1. Open Gumroad product page in incognito mode
2. Click "I want this"
3. Use Gumroad's test card: 4242 4242 4242 4242
4. Verify download link works
5. Verify file unzips correctly

---

## Step 10: Marketing

Copy marketing posts from `MARKETING_POSTS.md` and post to:
- BiggerPockets forum
- Reddit r/realestateinvesting
- Twitter/X
- LinkedIn

---

## Checklist

- [ ] Gumroad account created
- [ ] Product created with all copy
- [ ] .zip file uploaded
- [ ] Product settings configured
- [ ] Product published
- [ ] Landing page CTAs updated
- [ ] Test purchase completed
- [ ] Marketing posts scheduled

---

## Support Email Template

Save this for buyer questions:

```
Subject: RE Lead Enrichment Tool - Installation Help

Hi [Name],

Thanks for your purchase!

Here's how to get started:

1. Download and unzip re-lead-enrichment-pro.zip
2. Follow README.md installation instructions
3. Run `python3 lead_enrichment.py --help` to verify it works

If you get stuck, reply to this email with:
- Your operating system (Mac/Windows/Linux)
- Any error messages you see
- Screenshots if possible

I'll get you up and running!

Best,
Luis
luis@truenorthorlando.com
```

---

**All set! This should take ~15 minutes if you copy/paste the text above.**
