# GitHub Pages einrichten – "There isn't a GitHub Pages site here"

Wenn du diese Meldung siehst, ist Pages noch nicht aktiv oder nicht richtig konfiguriert. So richtest du es ein:

## 1. Prüfen: Sind die Dateien auf GitHub?

- Öffne **https://github.com/messianopizzapasta/lightlanguage-website**
- Du solltest **index.html** und **README.md** im Root sehen (nicht in einem Unterordner).
- Wenn nicht: aus dem Ordner **Desktop/website** die Git-Befehle ausführen (git init, add, commit, remote add, push).

## 2. GitHub Pages aktivieren

1. Im Repo **messianopizzapasta/lightlanguage-website** oben auf **Settings** klicken.
2. Links in der Sidebar zu **Pages** gehen (unter "Code and automation").
3. Unter **Build and deployment**:
   - **Source:** **Deploy from a branch** auswählen (nicht "GitHub Actions").
   - **Branch:** im Dropdown deinen Branch wählen (meist **main**, manchmal **master**).
   - **Folder:** **/ (root)** wählen.
   - Auf **Save** klicken.

## 3. Warten

- Nach dem Speichern erscheint oft: "Your site is ready to be published at …" oder "Your site is live at …".
- Es kann **1–2 Minuten** dauern, bis die Seite unter  
  **https://messianopizzapasta.github.io/lightlanguage-website/** erreichbar ist.
- Wenn es länger dauert: Seite neu laden oder kurz warten und nochmal probieren.

## 4. Wenn es immer noch nicht geht

- **Branch-Name:** Wenn du mit `git branch -M main` gearbeitet hast, muss unter Pages der Branch **main** gewählt sein. Wenn dein Branch **master** heißt, dann **master** wählen.
- **Leeres Repo:** Wenn das Repo beim Anlegen von GitHub mit README/Lizenz gefüllt wurde, kann es sein, dass dein Push in einen anderen Branch ging. Prüfe unter **Code** → Branch-Dropdown, ob **main** (oder **master**) deine **index.html** enthält.
- **URL:** Die Adresse ist immer:  
  `https://<username>.github.io/<repo-name>/`  
  also: **https://messianopizzapasta.github.io/lightlanguage-website/**

## Kurz-Checkliste

- [ ] Repo enthält **index.html** im Root (nicht in einem Unterordner).
- [ ] **Settings → Pages** → Source: **Deploy from a branch**.
- [ ] Branch: **main** (oder **master**) und Folder: **/ (root)**.
- [ ] **Save** geklickt.
- [ ] 1–2 Minuten gewartet, dann die URL im Browser geöffnet.
