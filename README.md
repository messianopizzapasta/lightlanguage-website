# Light Language – Website (SEO-ready)

This folder contains a single-page, SEO-optimized website for the Light Language app.

## What's included for SEO

- **Title & meta description** – Good for Google snippets
- **Keywords** – For search engines
- **Open Graph tags** – Nice previews when shared on Facebook, LinkedIn, etc.
- **Twitter Card tags** – Nice previews when shared on Twitter/X
- **JSON-LD (SoftwareApplication)** – Helps Google understand it's an app
- **Semantic HTML** – Header, main, sections, footer
- **Canonical URL** – Avoids duplicate-content issues

## Before you publish

1. **Replace `YOUR-SITE-URL.com`**  
   In `index.html`, search for `YOUR-SITE-URL.com` and replace with your real domain (e.g. your GitHub Pages URL: `messianopizzapasta.github.io/lightlanguage-website`).

2. **App Store link**  
   The App Store link is already set to: `https://apps.apple.com/us/app/light-language-grid-maker/id6758808761`

3. **Optional: App icon for social sharing**  
   Add a file `app-icon.png` (e.g. 512×512 or 1200×630) in this folder. If you host on GitHub Pages, the full URL is `https://messianopizzapasta.github.io/lightlanguage-website/app-icon.png`.

4. **Optional: Developer link**  
   Replace `YOUR-TEAM-ID` in the footer with your Apple Developer ID or your website URL.

## Deploy to GitHub Pages

1. In Terminal, go to this folder and run:
   ```bash
   cd ~/Desktop/website
   git init
   git add .
   git commit -m "Light Language website"
   git branch -M main
   git remote add origin https://github.com/messianopizzapasta/lightlanguage-website.git
   git push -u origin main
   ```
2. On GitHub: **Settings → Pages** → Source: **Deploy from a branch** → Branch **main**, folder **/ (root)** → Save.
3. Site is live at: **https://messianopizzapasta.github.io/lightlanguage-website/**

## After publishing

- Submit your site to Google: [Google Search Console](https://search.google.com/search-console) → Add property → your URL.
- Replace `YOUR-SITE-URL.com` in `index.html` with `messianopizzapasta.github.io/lightlanguage-website` (with https://), then commit and push again.
