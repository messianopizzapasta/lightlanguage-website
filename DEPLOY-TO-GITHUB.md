# Deploy to GitHub (lightlanguage-website)

Your repo: **https://github.com/messianopizzapasta/lightlanguage-website**

Do this **once** from Terminal. Use a **new folder** so only the website files go to GitHub (not the whole Xcode project).

## Steps

1. **Create a folder and copy the website files**
   ```bash
   mkdir -p ~/Desktop/lightlanguage-website
   cp "/Users/hannesmessner/Documents/Light Language/website/index.html" ~/Desktop/lightlanguage-website/
   cp "/Users/hannesmessner/Documents/Light Language/website/README.md" ~/Desktop/lightlanguage-website/
   ```

2. **Go into the folder and push to GitHub**
   ```bash
   cd ~/Desktop/lightlanguage-website
   git init
   git add .
   git commit -m "Light Language website"
   git branch -M main
   git remote add origin https://github.com/messianopizzapasta/lightlanguage-website.git
   git push -u origin main
   ```

3. **Turn on GitHub Pages**
   - On GitHub: open **messianopizzapasta/lightlanguage-website**
   - **Settings** → **Pages**
   - Under **Source**: choose **Deploy from a branch**
   - Branch: **main**, folder **/ (root)** → **Save**
   - After a minute the site is live at:  
     **https://messianopizzapasta.github.io/lightlanguage-website/**

## Later: update the site

After you change `index.html` or `README.md` in your **Light Language** project’s `website/` folder:

```bash
cp "/Users/hannesmessner/Documents/Light Language/website/index.html" ~/Desktop/lightlanguage-website/
cp "/Users/hannesmessner/Documents/Light Language/website/README.md" ~/Desktop/lightlanguage-website/
cd ~/Desktop/lightlanguage-website
git add .
git commit -m "Update website"
git push
```
