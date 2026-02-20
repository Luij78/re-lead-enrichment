# 🏠 RE Lead Enrichment Tool

## 💰 Stop Paying $0.15-0.30 Per Lead

**The Problem:** You've got a list of property owners (names, addresses) but no way to contact them. Skip tracing services charge $0.15-0.30 per lead minimum. For 1,000 leads, that's $150-$300.

**The Solution:** RE Lead Enrichment Tool finds phone numbers and emails for your leads — for a **one-time $49 payment**.

On your first 500-lead batch, you save **$75-$150** vs. traditional skip tracing.

---

## ✨ Features

### Free Tier
- ✅ 5 manual lookups per day
- ✅ Phone number extraction
- ✅ Progress tracking (resume anytime)
- ✅ CSV export

### Pro Tier ($49 one-time)
- ✅ **Unlimited automated batch processing**
- ✅ Phone + email discovery
- ✅ 500 lookups/month
- ✅ PropertyGlance integration (property value, ownership, zoning)
- ✅ Export to Repal CRM

### Enterprise ($149 one-time)
- ✅ Everything in Pro
- ✅ **Unlimited lookups**
- ✅ Priority support
- ✅ API access

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/re-lead-enrichment.git
cd re-lead-enrichment

# No dependencies needed - pure Python 3!
chmod +x lead_enrichment.py
```

### Usage

```bash
# Free tier: Manual lookup (5/day)
./lead_enrichment.py my_leads.csv

# Pro tier: Automated batch processing
./lead_enrichment.py my_leads.csv --license REPRO-xxxxxxxxxxxx --batch
```

---

## 📊 Input Format

Your CSV needs at least these columns:

```csv
Name,Address,City,State
John Smith,123 Main St,Orlando,FL
Jane Doe,456 Oak Ave,Tampa,FL
```

Accepted column names (auto-detected):
- **Name:** Name, full_name, Owner_Name, or first_name + last_name
- **Address:** Address, address, Property_Address, Mailing_Address
- **City:** City, city
- **State:** State, State_Abbr, state (defaults to FL if missing)

---

## 📈 Output Format

```csv
Name,Address,City,State,Phone,Email,Enrichment_Status
John Smith,123 Main St,Orlando,FL,(407) 555-1234,john@example.com,manual_enriched
Jane Doe,456 Oak Ave,Tampa,FL,(813) 555-5678,,manual_enriched
```

---

## 💡 How It Works

### Free Tier (Manual)
1. Tool generates optimized search queries for each lead
2. You copy/paste into TruePeopleSearch or FastPeopleSearch
3. Paste back the phone number/email
4. Repeat (5 per day limit)

### Pro Tier (Automated)
1. Tool uses browser automation to search multiple sources
2. Extracts phone numbers and emails automatically
3. Validates data quality
4. Exports clean CSV

**Speed:** ~20-30 seconds per lead in automated mode

---

## 🎯 Who This Is For

✅ Real estate wholesalers doing direct mail campaigns  
✅ Investors looking for off-market deals  
✅ Agents working FSBOs or expired listings  
✅ Property managers building tenant databases  
✅ Anyone tired of paying monthly skip tracing fees

---

## 💸 Pricing

| Tier | Price | Lookups/Month | Features |
|------|-------|---------------|----------|
| Free | $0 | 5/day | Manual, phone only |
| Pro | **$49** one-time | 500 | Automated, phone + email, CSV export |
| Enterprise | **$149** one-time | Unlimited | Everything + PropertyGlance + API |

**Why one-time?** You own the tool forever. No subscriptions, no hidden fees.

---

## 🔒 Privacy & Legal

- **Your data stays local** — We don't collect or store your leads
- **Public records only** — Uses publicly available data sources
- **Compliant** — Follows FCRA guidelines (for commercial use only)

⚠️ **Disclaimer:** This tool is for business/commercial use only (B2B prospecting, real estate investing). Not for consumer credit decisions or personal information collection.

---

## 🛠️ Advanced Usage

### Resume interrupted batch

Progress is auto-saved to `.progress.json`:

```bash
# If interrupted, just run again - it picks up where it left off
./lead_enrichment.py my_leads.csv --license REPRO-xxx --batch
```

### Export to Repal CRM

```bash
# Pro/Enterprise only - auto-formats for Repal import
./lead_enrichment.py my_leads.csv --license REPRO-xxx --export-repal
```

---

## 📞 Support

- **Issues/Bugs:** Open a GitHub issue
- **Feature Requests:** GitHub discussions
- **Enterprise:** email support@yourdomain.com

---

## 🎁 Limited Time Offer

**Launch Special:** First 100 buyers get Pro for **$29** (save $20)

Use code `LAUNCH29` at checkout.

---

## 📄 License

Pro/Enterprise license required for commercial use.

Free tier is MIT licensed for personal evaluation.

---

**Ready to stop overpaying for skip tracing?**

👉 [Get Pro Access ($49)](https://gumroad.com/yourproduct) 👈

---

Built with ❤️ for real estate investors who value their time and money.
