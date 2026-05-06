# Publish at apps.justbe.works

The site is set up to use **https://apps.justbe.works** (canonical URL, Open Graph, etc.). The **CNAME** file in this folder tells GitHub Pages to serve the site on that domain.

## 1. DNS (where you manage justbe.works)

Add a **CNAME** record:

| Type  | Name/Host | Value/Points to        |
|-------|-----------|------------------------|
| CNAME | apps      | messianopizzapasta.github.io |

- **Name:** `apps` (so the full host is `apps.justbe.works`)
- **Value:** `messianopizzapasta.github.io` (no `https://`, no path)

If your DNS has a “subdomain” field, use `apps`; if it wants the full name, use `apps.justbe.works`.

## 2. GitHub repo

1. Commit and push the **CNAME** file (it must be in the repo root, next to `index.html`).
2. **Settings → Pages** → **Custom domain**: enter **apps.justbe.works** → Save.
3. Wait for DNS to propagate (up to 48 hours, often a few minutes).
4. When GitHub shows “DNS check successful”, enable **Enforce HTTPS**.

## 3. Optional: app icon for social sharing

Add **app-icon.png** (e.g. 512×512 or 1200×630) to this folder. It will be used at **https://apps.justbe.works/app-icon.png** for link previews (already set in `index.html`).
