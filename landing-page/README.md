# Landing Page Deployment

## Quick Deploy to Vercel

1. **Install Vercel CLI** (if not already):
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd /Users/luisgarcia/.openclaw/workspace/skills/lead-enrichment/landing-page
   vercel --prod
   ```

3. **Set custom domain** (optional):
   ```bash
   vercel domains add releadenrichment.com
   ```

## Alternative: Netlify

1. **Drag and drop** the `landing-page` folder to [app.netlify.com/drop](https://app.netlify.com/drop)

2. Or use **Netlify CLI**:
   ```bash
   npm install -g netlify-cli
   cd landing-page
   netlify deploy --prod
   ```

## Alternative: GitHub Pages

1. **Create repo** `yourusername/re-lead-enrichment`

2. **Enable GitHub Pages** in repo settings → Pages → Source: main branch

3. **Push landing page:**
   ```bash
   cd landing-page
   git init
   git add .
   git commit -m "Initial landing page"
   git remote add origin https://github.com/yourusername/re-lead-enrichment.git
   git push -u origin main
   ```

4. **Access:** `https://yourusername.github.io/re-lead-enrichment/`

## Post-Deployment Checklist

- [ ] Update Gumroad links (replace placeholder URLs)
- [ ] Update GitHub repo link
- [ ] Update support email
- [ ] Test all CTA buttons
- [ ] Test mobile responsiveness
- [ ] Add Google Analytics (optional)
- [ ] Submit sitemap to Google Search Console

## Environment Variables (if needed later)

For future dynamic features (contact forms, etc.):

```bash
# Vercel
vercel env add GUMROAD_API_KEY

# Netlify
netlify env:set GUMROAD_API_KEY your_key_here
```

## Performance Optimization

Current setup (static HTML + Tailwind CDN) is already optimized:
- ✅ No build step
- ✅ CDN-served assets
- ✅ Minimal dependencies
- ✅ Fast page load (<1s)

For further optimization:
- Use [Tailwind CSS CLI](https://tailwindcss.com/docs/installation) to purge unused classes
- Minify HTML with `html-minifier`
- Add image optimization for product screenshots

## Analytics (Optional)

Add Google Analytics before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Or use [Plausible Analytics](https://plausible.io/) for privacy-friendly tracking:

```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>
```

## Estimated Time

- Vercel deploy: **2 minutes**
- Update links in HTML: **3 minutes**
- Test deployment: **2 minutes**
- **Total: ~7 minutes**
