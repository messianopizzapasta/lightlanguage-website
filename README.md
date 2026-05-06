# Light Language – Website (SEO-ready)

This folder contains a **multilingual** static site (English at `/`, plus `de/`, `es/`, `fr/`, `it/`, `pt/`) with shared styling in `assets/`, marketing screenshots in `assets/images/`, **one-page PDF study summaries** in `assets/pdfs/` (generated script: `scripts/generate_manual_summaries.py`; requires `fpdf2`), `sitemap.xml`, and `robots.txt`. Deploy the **entire** `website` folder so paths like `/assets/…` and `/de/` resolve correctly.

## What’s included for SEO

- **Title & meta description** – Good for Google snippets
- **Keywords** – For search engines
- **Open Graph tags** – Nice previews when shared on Facebook, LinkedIn, etc.
- **Twitter Card tags** – Nice previews when shared on Twitter/X
- **JSON-LD (SoftwareApplication)** – Helps Google understand it’s an app
- **Semantic HTML** – Header, main, sections, footer
- **Canonical URL** – Avoids duplicate-content issues

## Before you publish

1. **Replace `YOUR-SITE-URL.com`**  
   In `index.html`, search for `YOUR-SITE-URL.com` and replace with your real domain (e.g. `lightlanguage.app` or your GitHub/Netlify URL).

2. **App Store link**  
   The App Store link is set to: `https://apps.apple.com/us/app/light-language-grid-creator/id6758855353` (price varies by country; the US listing showed a paid tier at the time of writing).

3. **Optional: App icon for social sharing**  
   Add a file `app-icon.png` (e.g. 512×512 or 1200×630) in this folder and keep the `og:image` / `twitter:image` URLs pointing to it. If you host on GitHub Pages, the full URL is `https://YOUR-USERNAME.github.io/YOUR-REPO/app-icon.png`.

4. **Optional: Developer link**  
   Replace `YOUR-TEAM-ID` in the footer with your Apple Developer ID or your website URL.

## Deploy for free

### Option A: GitHub Pages

1. Create a new repo (e.g. `lightlanguage-website`).
2. Upload the contents of this `website` folder (e.g. `index.html` and optional `app-icon.png`).
3. In the repo: **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main` (or `master`) → folder **/ (root)** → Save.
4. Your site will be at `https://YOUR-USERNAME.github.io/lightlanguage-website/`.
5. (Optional) Add a custom domain under **Settings → Pages → Custom domain**.

### Option B: Netlify

1. Go to [netlify.com](https://www.netlify.com) and sign up (free).
2. Drag and drop this `website` folder onto the Netlify deploy area, or connect a Git repo that contains this folder.
3. You get a URL like `https://random-name.netlify.app`. You can change it or add a custom domain in **Domain settings**.

### Option C: Vercel / Cloudflare Pages

Same idea: create a project, connect the folder or repo, and deploy. All have free tiers and work well with static HTML.

## After publishing

- Submit your site to Google: [Google Search Console](https://search.google.com/search-console) → Add property → your URL.
- Share the link on social media; Open Graph and Twitter tags will improve how the link looks.
