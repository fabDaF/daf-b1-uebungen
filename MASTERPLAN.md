# DaF — Masterplan für interaktive HTML-Übungsdateien
## Gültig für: B1.1 (und alle weiteren Niveaus sofern nicht anders angegeben)

Dieses Dokument ist die **einzige verbindliche Referenz** für alle HTML-Übungsdateien.
Es wird **vor jeder Arbeit** an einer HTML-Datei gelesen — ohne Ausnahme.

---

## 0. Vor dem Start — Pflichtlektüre

Bevor eine einzige Zeile Code geschrieben wird, sind folgende Skills zu lesen:

| Skill | Wann |
|-------|------|
| `daf-grammatik-uebungen` | Bei jeder G-Datei |
| `daf-html-layout` | Bei jeder neuen oder migrierten Datei |
| `satzbau-drag-drop` | Wenn Satzbau-Tab enthalten |
| `daf-uebungsformen` | Immer |
| `daf-bilder-pflicht` | Immer (jede Datei braucht Bilder) |
| `textgestaltung-daf` | Wenn Lesetext / Geschichte-Tab enthalten |
| `lesetext-hervorhebung` | Wenn Lesetext enthalten |
| `daf-browser-test` | Nach Fertigstellung — testen bis 0 Fehler |

**Danach:** Browser-Test durchführen. Solange wiederholen, bis keine Fehler mehr gemeldet werden.

---

## 1. Nomenklatur

### Dateiname-Schema

```
DE_B1_LLLLx-thema.html
     ^^  ^^^^
     ||  ||||__ x = Datei-Typ (V, X, G, R, S, W)
     ||  |||___ Lektionsnummer innerhalb der Einheit (1–8)
     ||  ||____ Einheitsnummer (01–07)
     ||  |_____ Kurs (1 = B1.1)
     ||________ Niveau (B1)
     |_________ Sprache
```

Beispiel: `DE_B1_1011X-vorstellungsgespraech.html`

### Quellmaterial
Lingoda-PDFs unter: `Cowork/lingoda/B 1.1/`

### Dashboard
**Es gibt genau ein gültiges Dashboard:**
```
/sessions/eager-great-dirac/mnt/htmlS/dashboard.html
```
auf dem Rechner: `file:///Users/frankburkert/Cowork/htmlS/dashboard.html`

⛔ Alle anderen Dashboard-Dateien (`b1-1-dashboard.html`, `a2-1-dashboard.html` etc.) sind **obsolet** und werden **nie** verwendet oder verlinkt.

---

## 2. Übersicht aller B1.1-Lektionen

| Einheit | Thema | Lektionen |
|---------|-------|-----------|
| 101x | Bewerbung & Arbeit | 1011X 1012G 1013R 1014X 1015G 1016R 1017X 1018S |
| 102x | Umwelt & Gesellschaft | 1021X 1022G 1023R 1024X 1025G 1026R 1027X 1028S |
| 103x | Identität & Sprache | 1031X 1032G 1033R 1034X 1035G 1036R 1037X 1038S |
| 104x | Soziale Netzwerke & Privatsphäre | 1041X 1042G 1043R 1044X |
| 105x | Gesundheit & Gesellschaft | 1045G |

### Fertigstellungsstatus B1.1

| Lektion | Typ | Thema | Status |
|---------|-----|-------|--------|
| 1011X | X | Das Vorstellungsgespräch | ✅ Fertig |
| 1012G | G | Konjunktiv II der Modalverben | ✅ Fertig |
| 1013R | R | Neue Berufe | ✅ Fertig |
| 1014X | X | Einen Vertrag verhandeln | ✅ Fertig |
| 1015G | G | Temporaladverbien | ✅ Fertig |
| 1016R | R | Kulturelle Unterschiede am Arbeitsplatz | ✅ Fertig |
| 1017X | X | Besprechungen in der Firma | ✅ Fertig |
| 1018S | S | Ein Gespräch mit dem Vorgesetzten | ✅ Fertig |
| 1021X | X | Umweltprobleme und Umweltschutz | ✅ Fertig |
| 1022G | G | Zweiteilige Präpositionen | ✅ Fertig |
| 1023R | R | Luftverschmutzung | ✅ Fertig |
| 1024X | X | Umweltschutz und Recycling | ✅ Fertig |
| 1025G | G | Mehr über die Adjektive | ✅ Fertig |
| 1026R | R | Vom Menschen ausgelöste Katastrophen | ✅ Fertig |
| 1027X | X | Naturkatastrophen | ✅ Fertig |
| 1028S | S | Wie umweltbewusst bist du? | ✅ Fertig |
| 1031X | X | Identität und Sprachkultur | ✅ Fertig |
| 1032G | G | Mehr über Lokaladverbien | ✅ Fertig |
| 1033R | R | Berlin – eine multikulturelle Stadt | ✅ Fertig |
| 1034X | X | Multikulturalismus | ✅ Fertig |
| 1035G | G | Infinitivkonstruktionen haben zu / sein zu | ✅ Fertig |
| 1036R | R | Deutsche Traditionen | ✅ Fertig |
| 1037X | X | Globalisierung | ✅ Fertig |
| 1038S | S | Die kulturelle Vielfalt | ✅ Fertig |
| 1041X | X | Privatsphäre in einer vernetzten Welt | ✅ Fertig |
| 1042G | G | Mehr über Pronomen | ✅ Fertig |
| 1043R | R | Partnersuche online | ✅ Fertig |
| 1044X | X | Online einkaufen | ✅ Fertig |
| 1045G | G | Mehr über die Negation | ✅ Fertig |

---

## 3. Datei-Typen und Tab-Struktur

### G — Grammatik (`*G*.html`)

**Zweck:** Grammatikregel entdecken, verstehen, üben.

| Tab | Emoji | Name | Inhalt |
|-----|-------|------|--------|
| 0 | 🔍 | Entdecken | Beispielsätze, Regel ableiten |
| 1 | 📋 | Regel | Regelkarte, Paradigmentabelle |
| 2 | ✏️ | Lückentext | Grammatik-Lückentext, Live-Feedback, Timer |
| 3 | 🧩 | Satzbau | Sätze mit Grammatikfokus ordnen, Timer |
| 4 | 🎯 | Multiple Choice | A/B/C-Auswahl oder Richtig/Falsch |

Skill: `daf-grammatik-uebungen`

### X — Extra-Übungen (`*X*.html`)

**Zweck:** Vertiefung, Anwendung, situative Dialoge.

Tab-Struktur je nach Inhalt variabel — Referenz: `DE_B1_1011X-vorstellungsgespraech.html`

### R — Lesetext (`*R*.html`)

**Zweck:** Lesetext mit Vorentlastung, Verstehensaufgaben, Wortschatz.

| Tab | Emoji | Name | Inhalt |
|-----|-------|------|--------|
| 0 | 🌅 | Vorentlastung | Schlüsselwörter, Bilder, englische Vorabinfo |
| 1 | 📖 | Geschichte | Lesetext (formatiert nach `textgestaltung-daf`) |
| 2 | ❓ | Verständnis | Richtig/Falsch + Fragen |
| 3 | ✏️ | Lückentext | Sätze aus dem Text mit Lücken |
| 4 | 🧩 | Satzbau | Sätze zerlegt, Timer |
| 5 | 🔠 | Wortschatz | Tippen: Artikel + Wort + Plural, Timer |

Skill: `textgestaltung-daf`, `lesetext-hervorhebung`

### V — Vokabular (`*V*.html`)

| Tab | Emoji | Name | Inhalt |
|-----|-------|------|--------|
| 0 | 📸 | Wörter | Foto-Vokabelkarten (10–12): Artikel · Wort · Plural · EN · Beispielsatz |
| 1 | 💬 | Redemittel | Frage-und-Antwort Drag & Drop |
| 2 | ✏️ | Lückentext | 2 Lückentexte, Live-Feedback, Timer |
| 3 | 📖 | Text & Fragen | Lesetext + Richtig/Falsch |
| 4 | 🧩 | Satzbau | 6–8 Sätze, Drag & Drop, Timer |
| 5 | 🔠 | Wortschatz | Tippen: Artikel + Wort + Plural, Timer |

### S — Speaking (`*S*.html`)

Erwartete Elemente: Dialogkarten, Redemittel-Chips, Rollenspiel-Szenarios.
Tab-Struktur wird beim ersten S-File definiert.

### W — Wiederholung (`*W*.html`)

Gemischte Aufgaben aus allen Lektionen, Selbsteinschätzung.
Tab-Struktur wird beim ersten W-File definiert.

---

## 4. Verbindliche Qualitätsregeln

### Layout
- Lila Hintergrund-Gradient (`#667eea` → `#764ba2`) — Skill: `daf-html-layout`
- Weißer Container, max. 1000px, Schatten
- Nav-Buttons: Emoji **über** Text (`nav-emoji` + `nav-label`, `flex-direction: column`)
- Aktiver Nav-Button: Klasse `active` (**nicht** `aktiv`)
- Sichtbare Section: Klasse `aktiv`

### Lücken-Inputs — Placeholder IMMER leer

⛔ `placeholder="___"` ist **verboten**. Keine Striche, Punkte oder Füllzeichen.

```html
<!-- ❌ FALSCH -->
<input placeholder="___">
<!-- ✅ RICHTIG -->
<input placeholder="">
```

### Live-Feedback

Gilt für alle Tipp-Felder — kein Prüfen-Button, niemals.

| Zustand | Farbe |
|---------|-------|
| Leer | grau (neutral) |
| Prefix korrekt | lila |
| Vollständig korrekt | grün (`.ok`) |
| Falsch | rot (`.no`) |

Reihenfolge in JS: erst `val === ans`, dann `ans.startsWith(val)`.

### Timer — EINZIGES GÜLTIGES MUSTER: `.timer-controls`

⛔ `timer-bar` + `btn-row` als getrennte `<div>`s ist **VERBOTEN** — führt zu Buttons am Seitenende.

**Alle Elemente in einer Zeile:** Buttons links (`.tc-buttons`), Zeit rechts (`.tc-times`) — in einem einzigen `<div class="timer-controls">`.

```html
<div class="timer-controls">
  <div class="tc-buttons">
    <button onclick="showLoesung()">💡 Lösungen</button>
    <button onclick="timerResetOne(N); resetXxx()">↺ Neustart</button>
  </div>
  <div class="tc-times">
    <span>⏱ <span class="timer-display" id="timer-N">0:00</span></span>
    <span>🏆 <span class="best-display" id="best-N">–</span></span>
  </div>
</div>
```

```css
.timer-controls { display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; flex-wrap:wrap; gap:6px; }
.tc-buttons { display:flex; gap:6px; }
.tc-buttons button { background:none; border:1px solid #ddd; border-radius:6px; padding:4px 12px; font-size:0.82em; color:#888; cursor:pointer; transition:all 0.15s; font-weight:500; }
.tc-buttons button:hover { background:#f0f0f0; color:#555; }
.tc-times { display:flex; gap:14px; font-size:0.82em; color:#bbb; font-variant-numeric:tabular-nums; }
.timer-display { color:#667eea; font-weight:700; }
.best-display  { color:#f39c12; font-weight:600; }
```

- Startet bei erster Interaktion (`timerAutoStart`), stoppt wenn alle korrekt
- Bestzeit in `localStorage` (Key: `TIMER_PREFIX + N`)

### Satzbau

Verbindlich: Skill `satzbau-drag-drop`
- Variable: `sbDragged`
- IDs: `sb-bank-N` / `sb-row-N` / `sb-fb-N`
- Fisher-Yates-Shuffle
- 500ms-Timeout vor Farb-Feedback

### ⛔ ABSOLUTES VERBOT — Satznummerierung

**Niemals** Satznummern anzeigen. Keine Ausnahmen. Kein `Satz 1`, `Satz 2`, keine `(idx+1)`-Labels, keine `.num`-Spans, keine `.sb-label` mit Zahlen.

```javascript
// ❌ VERBOTEN — in keiner Form:
label.textContent = 'Satz ' + (idx + 1);
lbl.textContent = 'Satz ' + ex.id;
wrapper.appendChild(label); // wenn label eine Nummer enthält
```

Kein Mensch braucht diesen Hinweis. Er stört und wirkt amateurhaft.

### Bilder (Pexels)

URL-Schema:
```
https://images.pexels.com/photos/ID/pexels-photo-ID.jpeg?auto=compress&cs=tinysrgb&w=400&h=300&fit=crop
```

**⚠️ Pflicht: Base64-Einbettung**
Alle Pexels-Bilder müssen als Base64-Data-URLs eingebettet sein. Externe URLs sind nicht zulässig — Dateien müssen offline-fähig sein.

Workflow: Pexels-URL → Browser-Fetch via Chrome-Extension → Base64 → in HTML einbetten.
Skill: `daf-bilder-pflicht`, `pexels-bild-check`

### Copyright-Footer

```html
<span class="author-name">&copy; Frank Burkert</span> &middot; DaF-Materialien &middot;
<a href="mailto:FrankBurkert@fabdaf.onmicrosoft.com">FrankBurkert@fabdaf.onmicrosoft.com</a>
```

⛔ **Niemals ändern.** Keine Verbesserungen, keine Varianten. Nur auf explizite schriftliche Anweisung.

---

## 5. Karim Benali — Narrative Figur (B1.1)

Karim ist die wiederkehrende Erzählfigur in allen B1.1-Lesetexten und Geschichten.

**Biografie:**
- 31 Jahre alt, aus Casablanca, Marokko
- Wirtschaftsingenieur, spricht Arabisch, Französisch, Englisch und nun Deutsch
- Neu in Düsseldorf, hat bei E.ON eine Stelle als Projektkoordinator bekommen
- Ruhige, beobachtende Persönlichkeit — kein Klischee, kein Kitsch

**Stand der Geschichte:**
- 1011X: Bewerbung und Vorstellungsgespräch bei E.ON — „Der richtige Mann"
- 1013R: Sein erster Abend in Düsseldorf — liest einen Artikel über neue Berufe
- 1014X: Gehaltsverhandlung — „Das Angebot"
- 1015G: (folgt — erster Arbeitstag? Kollegen? Moment in der Stadt?)

**Ton:**
- Leise Beobachtung, innere Stimme kursiv + gesperrt (`.gedanke`)
- Keine konkreten Zahlen (kein Gehalt, kein Datum)
- Keine Klischees über Marokko oder Migration
- Grammatikthema muss **organisch** im Text vorkommen — nicht aufgesetzt

**CSS für Gedanken/innere Stimme:**
```css
.gedanke {
  font-style: italic;
  letter-spacing: 0.03em;
  color: #444;
}
```

**Vokabel-Hervorhebung im Text:**
Alle Lernvokabeln mit `<span class="hl">Wort</span>` markieren.
Skill: `lesetext-hervorhebung`

---

### Autor-Prompt — Verbindliche Schreibhaltung für alle Karim-Texte

Bevor eine einzige Zeile der Geschichte geschrieben wird, nimmt Claude diese Haltung ein:

> **Ich bin Autor, nicht Texter.**
> Ich schreibe keine Übungstexte. Ich schreibe Literatur, die zufällig auch eine Grammatikfunktion hat.
> Karim ist kein Platzhalter. Er ist ein Mensch mit Geschichte, Körper, Erinnerungen, Zweifeln.
> Ich beobachte ihn von innen und von außen gleichzeitig.

**Stilprinzipien (nicht verhandelbar):**

1. **Leise Beobachtung** — keine Dramatik, keine Ausrufezeichen des Lebens. Was zählt, sind kleine, präzise Details: das Licht im Büro, das Geräusch einer Schublade, der Geruch von Kaffee.

2. **Innere Stimme als Kontrast** — Karim denkt mehr als er spricht. Gedanken stehen als `.gedanke` (kursiv, gesperrt). Sie kommentieren das Äußere, nicht erklären es.

3. **Kein Klischee, keine Migrationsgeschichte** — Karim ist nicht "der Fremde". Er ist jemand, der anders sozialisiert wurde und das mit Neugier beobachtet — nicht mit Schmerz, nicht mit Bewunderung, sondern mit wacher Aufmerksamkeit.

4. **Grammatikthema organisch** — das Grammatikthema darf nicht spürbar sein. Es muss so natürlich vorkommen, dass ein Leser es übersieht. Erst die Übung macht es sichtbar.

5. **Quasthoff-Sprache** — alle Verb-Nomen-Verbindungen aus dem Kollokationswörterbuch. Kein Satz, der sich nach "Schulbuch" anfühlt.

6. **Narrative Kontinuität** — jede Geschichte schließt an die vorherige an. Den letzten Satz der vorherigen Geschichte kennen und einen unsichtbaren Bogen ziehen.

7. **Länge und Rhythmus** — Absätze sind kurz (3–5 Sätze). Dann ein längerer. Dann wieder kurz. Kein gleichförmiger Takt.

8. **Erzählperspektive** — Enge personale Perspektive (nahe am "Er"-Erzähler, aber mit Zugang zu Karims Gedanken). Kein auktorialer Kommentar.

---

## 6. Tab-Banner und Bilder — Verbindliche Regeln

⛔ **JEDE DaF-HTML-Datei braucht echte Bilder. Kein Commit ohne Bilder. Keine Ausnahme.**

SVG-Platzhalter (wie `data:image/svg+xml,...`) sind **VERBOTEN** in fertigen Dateien.
Sie dürfen nur während der Entwicklung als temporärer Platzhalter existieren —
**vor dem Commit müssen sie durch echte Pexels-Fotos ersetzt werden.**

### Verbindliches CSS (muss in jeder Datei stehen)

```css
.tab-banner {
  width: 100%;
  max-height: 180px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 18px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
@media (max-width: 600px) {
  .tab-banner { max-height: 120px; }
}
```

### HTML-Position (KRITISCH)

Das Banner kommt **direkt nach dem `<section>`-Open-Tag**, **vor** allem anderen:

```html
<section class="section" id="sec-0">
  <img class="tab-banner" src="https://images.pexels.com/photos/ID/pexels-photo-ID.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Beschreibung">
  <!-- Danach: Timer, Übungsinhalt -->
</section>
```

### Mindestanzahl Tab-Banner

| Typ | Tabs | Tab-Banner |
|-----|------|------------|
| R (Lesetext) | 5 | 5 Banner — je eines pro Tab |
| G (Grammatik) | 5 | 5 Banner |
| X (Extra/Kommunikation) | 4–5 | 4–5 Banner |
| V (Vokabular) | 6 | 6 Banner + Vokabelkarten mit Fotos |

### Pexels-Bild-URL-Schema

```
https://images.pexels.com/photos/PEXELS_ID/pexels-photo-PEXELS_ID.jpeg?auto=compress&cs=tinysrgb&w=800
```

Pexels-ID aus URL extrahieren: `https://www.pexels.com/photo/beschreibung-1234567/` → ID = `1234567`

### Suchstrategie (auf Englisch suchen!)

| Tab-Thema | Pexels-Suchbegriff |
|-----------|--------------------|
| Vorentlastung (Themen-spezifisch) | Thema auf Englisch, z.B. `office meeting multicultural` |
| Geschichte / Lesetext | `reading book cozy` oder thematisch |
| Lückentext | `writing studying notebook` |
| Satzbau | `puzzle pieces building blocks` |
| Wortschatz | `books dictionary alphabet` |
| Grammatik-Entdecken | `magnifying glass research curious` |
| Grammatik-Regel | `blackboard notes rules` |

### Bilder suchen — via Chrome-MCP (Batch)

```javascript
(async () => {
  const searches = [
    ['office meeting multicultural', 'Tab 0: Vorentlastung'],
    ['reading book cozy', 'Tab 1: Geschichte'],
    ['writing studying notebook', 'Tab 2: Lückentext'],
    ['puzzle pieces', 'Tab 3: Satzbau'],
    ['books dictionary', 'Tab 4: Wortschatz'],
  ];
  const results = await Promise.all(searches.map(async ([q, desc]) => {
    const resp = await fetch('https://www.pexels.com/search/' + encodeURIComponent(q) + '/?orientation=landscape');
    const text = await resp.text();
    const ids = [...new Set([...text.matchAll(/\/photos\/(\d{5,10})\//g)].map(m => m[1]))].slice(0, 4);
    return desc + ': ' + ids.join(', ');
  }));
  return results.join('\n');
})()
```

### ⛔ Pflicht: Visuelle Prüfung JEDES Bildes im Browser

Pexels-Keywords sind unzuverlässig. Kein Bild darf ungesehen eingebaut werden.

**Nach dem Einbau:** Seite im Browser öffnen, jeden Tab anklicken, Banner-Bild ansehen.
- Passt es thematisch? Ist es hell genug? Landscape-Format? Kein Wasserzeichen?
- Falsche Bilder sofort ersetzen — neue Pexels-ID wählen.

### Selbst-Check (Bilder)

- [ ] SVG-Platzhalter entfernt? (kein `data:image/svg+xml` in fertiger Datei)
- [ ] Jeder Tab hat ein `<img class="tab-banner">` als erstes Element?
- [ ] Alle Bilder sind Pexels-URLs oder Base64 (kein SVG)?
- [ ] `.tab-banner` CSS mit `max-height: 180px` + `object-fit: cover` vorhanden?
- [ ] Jedes Bild visuell im Browser geprüft?

---

## 6a. Verbindlicher Workflow: Pexels-Bilder als Base64 einbetten

⛔ **Dieser Workflow ist Pflicht.** Er wurde nach zwei Stunden Debugging am 21. März 2026 dokumentiert und darf nicht übersprungen oder abgekürzt werden. Jeder Schritt hat einen Grund.

### Kernproblem

Die Cowork-VM hat **keinen Internetzugang** — `urllib`, `requests`, `curl` etc. scheitern alle mit `403 Forbidden`. Nur der Chrome-Browser auf dem Mac kann Pexels erreichen. Aber Chrome-MCP blockiert Base64-Daten in der JS-Rückgabe (`[BLOCKED: Base64 encoded data]`). Der einzige funktionierende Weg ist daher: **Chrome fetcht → Blob → Download als JSON → VM liest JSON.**

### Phase 1: Pexels-IDs sammeln

Alle benötigten Pexels-IDs aus den HTML-Dateien extrahieren:

```python
import re, glob
all_ids = set()
for f in sorted(glob.glob('/pfad/zu/htmlS/B1.1/DE_B1_*.html')):
    with open(f) as fh:
        content = fh.read()
    ids = re.findall(r'images\.pexels\.com/photos/(\d+)/', content)
    all_ids.update(ids)
print(f'{len(all_ids)} einzigartige IDs')
```

### Phase 2: Bilder im Chrome-Browser fetchen und als JSON bündeln

Tab-ID beschaffen: `tabs_context_mcp(createIfEmpty=True)` → ergibt `tabId`

**WICHTIG:** Die Seite muss auf irgendeine Seite navigiert sein (z.B. GitHub Pages). Pexels.com selbst ist durch Cloudflare blockiert, aber `images.pexels.com` (das CDN) ist direkt erreichbar.

```javascript
// Im Chrome-MCP javascript_tool:
(async () => {
  const ids = ['ID1', 'ID2', 'ID3', /* ... alle IDs */];
  const results = {};
  for (const id of ids) {
    try {
      const resp = await fetch(
        `https://images.pexels.com/photos/${id}/pexels-photo-${id}.jpeg?auto=compress&cs=tinysrgb&w=800&h=400&fit=crop`
      );
      const blob = await resp.blob();
      const b64 = await new Promise(resolve => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result);
        reader.readAsDataURL(blob);
      });
      results[id] = b64;
    } catch(e) {
      results[id] = 'ERROR: ' + e.message;
    }
  }
  window._b64cache = results;
  return `Fetched ${Object.keys(results).length} images`;
})()
```

### Phase 3: Download auslösen — MIT Nutzer-Erlaubnis

⛔ **VOR dem Download IMMER den Nutzer fragen.** Dieser Schritt darf NICHT übersprungen werden.

```
Claude: „Darf ich pexels_KURS_all.json (ca. X MB, Y Bilder) in deinen Downloads-Ordner speichern?"
Nutzer: „ja"
```

Erst nach dem „ja" den Download-Code ausführen:

```javascript
// Im Chrome-MCP javascript_tool (gleicher Tab, window._b64cache ist noch da):
const blob = new Blob([JSON.stringify(window._b64cache)], {type:'text/plain'});
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'pexels_b1_all.json';
document.body.appendChild(a);
a.click();
'Download triggered'
```

Die Datei landet im Mac-Downloads-Ordner → in der VM unter `/mnt/Downloads/pexels_b1_all.json`.

### Phase 4: JSON in der VM lesen und Base64 in HTML einsetzen

```python
import json, re, glob, os

# JSON-Cache laden
with open('/pfad/zu/Downloads/pexels_b1_all.json') as f:
    b64data = json.load(f)

# Für jede HTML-Datei: alle Pexels-URLs durch Base64 ersetzen
html_dir = '/pfad/zu/htmlS/B1.1/'
for fpath in sorted(glob.glob(os.path.join(html_dir, 'DE_B1_*.html'))):
    with open(fpath) as f:
        content = f.read()
    changed = 0
    for pid, b64 in b64data.items():
        if not b64 or not b64.startswith('data:image'):
            continue
        # WICHTIG: Regex matcht ALLE URL-Formate (Standard + Slug)
        pattern = rf'https://images\.pexels\.com/photos/{pid}/[^"\']*'
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, b64, content)
            changed += len(matches)
    if changed > 0:
        with open(fpath, 'w') as f:
            f.write(content)
        print(f'  ✓ {os.path.basename(fpath)}: {changed} Bilder eingebettet')
```

### Phase 5: Verifizieren — keine externen URLs mehr

```python
# Muss 0 ergeben:
import glob, re
for f in sorted(glob.glob('/pfad/zu/htmlS/B1.1/DE_B1_*.html')):
    with open(f) as fh:
        count = len(re.findall(r'https://images\.pexels\.com', fh.read()))
    if count > 0:
        print(f'  ⚠ {os.path.basename(f)}: {count} externe URLs!')
```

### Phase 6: Git commit & push

```bash
cd /tmp/b1push
cp /pfad/zu/htmlS/B1.1/DE_B1_*.html .
git add -A && git commit -m "Embed all Pexels banners as Base64 — offline-ready"
git push origin main
```

### Phase 7: Visuelle Verifikation auf GitHub Pages

Jede Datei im Browser öffnen, jeden Tab anklicken, Banner-Bild prüfen:
- Wird das Bild angezeigt? (Base64 korrekt?)
- Passt das Bild thematisch zum Tab?
- GitHub Pages CDN-Cache braucht ca. 5–10 Minuten nach dem Push

### Nachträgliche Einzel-Ersetzungen (falsche Bilder austauschen)

Wenn ein bereits eingebettetes Bild thematisch falsch ist:

1. **Neues Bild finden** — Pexels-Suche via Chrome-MCP
2. **Neues Bild fetchen** — wie Phase 2, aber nur die neuen IDs
3. **Download** — wie Phase 3 (Nutzer-Erlaubnis!)
4. **Alte Base64 durch neue ersetzen:**

```python
import json
# Altes Base64 aus dem großen Cache
with open('pexels_b1_all.json') as f:
    old_cache = json.load(f)
# Neues Base64 aus dem Replacement-Download
with open('pexels_b1_missing.json') as f:
    new_cache = json.load(f)

# In jeder HTML: old_b64 → new_b64
for old_id, new_id in replacement_map.items():
    old_b64 = old_cache[old_id]
    new_b64 = new_cache[new_id]
    content = content.replace(old_b64, new_b64)
```

### Häufige Fehler und ihre Lösung

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| `403 Forbidden` bei `urllib`/`curl` | VM hat kein Internet | Chrome-MCP verwenden |
| `[BLOCKED: Base64 encoded data]` | Chrome-MCP filtert Base64 | Blob → `a.download` → JSON-Datei |
| Download liegt nicht in `/mnt/Downloads/` | Falscher Download-Pfad | Nutzer muss Download bestätigen → landet im Mac-Downloads |
| Slug-Format-URL nicht gematcht | Regex zu eng (`pexels-photo-ID`) | Regex: `rf'/photos/{pid}/[^"\']*'` (matcht jeden Dateinamen) |
| Bild zeigt 404-HTML statt Foto | Pexels-ID gelöscht | Neue ID suchen, neues Bild fetchen |
| Base64 ist `data:text/html;base64,...` | Pexels-ID war 404 → Server lieferte HTML | Prüfen mit `b64.startswith('data:image')` |
| Chrome-Session abgelaufen / `window._b64cache` leer | Seite wurde navigiert | Nochmal fetchen, Daten gehen bei Navigation verloren |

### ⛔ Was NICHT funktioniert (spart Stunden!)

- ❌ `urllib.request` / `requests` / `curl` aus der VM → 403
- ❌ Base64 direkt aus Chrome-MCP-JS-Rückgabe lesen → BLOCKED
- ❌ `window._b64cache` über MCP-Rückgabewert auslesen → BLOCKED
- ❌ Bilder in `/tmp/` oder `/sessions/` speichern via Browser → Chrome speichert NUR in den Downloads-Ordner
- ❌ Download ohne Nutzer-Erlaubnis → verstößt gegen Cowork-Regeln

### ✅ Was FUNKTIONIERT (der goldene Pfad)

1. Chrome-Tab auf eine beliebige Seite navigieren
2. `fetch()` auf `images.pexels.com` CDN (kein Cloudflare!)
3. Blob → FileReader → `window._b64cache`
4. Nutzer fragen → `a.download` → JSON in Downloads
5. VM liest `/mnt/Downloads/*.json` → Python ersetzt in HTML

---

## 6b. Verbindliche visuelle Prüfmethode für Bilder (Chrome-MCP)

⛔ **Diese Methode ist Pflicht nach jedem Bild-Einbau oder -Austausch.** Dokumentiert am 21. März 2026 nach dem ersten systematischen Qualitätsaudit aller B1.1-Banner.

### Warum visuelle Prüfung?

Pexels-Keywords sind unzuverlässig. Eine Suche nach „office meeting" kann ein Foto von einem leeren Schreibtisch liefern. Alt-Texte in den HTML-Dateien beschreiben das *gewünschte* Bild, nicht das *tatsächliche*. Nur die visuelle Prüfung im Browser stellt sicher, dass das Bild thematisch passt.

### Schritt-für-Schritt-Anleitung

**1. GitHub Pages URL öffnen:**
```javascript
// Im Chrome-MCP navigate tool:
url: "https://fabdaf.github.io/daf-b1-uebungen/DE_B1_1012G-konjunktiv-ii.html"
```

**2. Tab-ID beschaffen:**
```
tabs_context_mcp(createIfEmpty=True) → tabId
```

**3. Jeden Tab nacheinander anklicken und Banner zoomen:**
```javascript
// Tab N aktivieren (N = 0, 1, 2, ...):
document.querySelectorAll('.nav-btn')[N].click()
```

**4. Banner-Region zoomen:**
```
computer tool → action: "zoom", region: [270, 230, 1100, 410]
```
Diese Region zeigt das Tab-Banner in hoher Auflösung. Koordinaten können je nach Viewport leicht variieren — bei Bedarf erst einen Screenshot machen und die Banner-Position identifizieren.

**5. Bewertungskriterien pro Bild:**

| Kriterium | ✅ Gut | ❌ Schlecht |
|-----------|--------|------------|
| Thematische Passung | Bild zeigt das Tab-Thema | Bild zeigt etwas Fremdes |
| Alt-Text-Übereinstimmung | Alt-Text beschreibt, was zu sehen ist | Alt-Text und Bild passen nicht zusammen |
| Bildqualität | Scharf, gut belichtet, professionell | Unscharf, dunkel, amateurhaft |
| Format | Landscape, füllt den Banner-Bereich | Portrait, abgeschnitten, verzerrt |
| Wasserzeichen | Keines sichtbar | Wasserzeichen oder Overlay |
| Angemessenheit | Kulturell passend, kein anstößiger Inhalt | Stereotypen, unangemessen |

**6. Bei Fehler:**
- Pexels-ID notieren
- Neues Bild suchen (Chrome-MCP Pexels-Suche)
- Ersetzen nach §6a Workflow (Nachträgliche Einzel-Ersetzungen)

### Beispiel: Kompletter Audit-Durchlauf einer Datei

```
1. Navigate → https://fabdaf.github.io/daf-b1-uebungen/DE_B1_1012G-konjunktiv-ii.html
2. Warte 3 Sekunden (GitHub Pages laden)
3. Tab 0: document.querySelectorAll('.nav-btn')[0].click()
   → zoom [270, 230, 1100, 410]
   → Bewertung: „Lupe auf Buch — passt zu Entdecken ✅"
4. Tab 1: document.querySelectorAll('.nav-btn')[1].click()
   → zoom [270, 230, 1100, 410]
   → Bewertung: „Tafel mit Regeln — passt zu Regel ✅"
5. Tab 2: ...  (alle Tabs durchgehen)
6. Ergebnis dokumentieren: „1012G: 5/5 Banner OK" oder „1012G: Tab 1 ❌ — Python-Buch statt Grammatik"
```

### Batch-Audit aller Dateien

Für einen systematischen Durchlauf aller Dateien:
1. Liste aller HTML-Dateien erstellen
2. Pro Datei: URL öffnen → alle Tabs durchklicken → alle Banner zoomen
3. Ergebnisse in einer Tabelle festhalten
4. Alle ❌-Bilder am Ende gesammelt ersetzen (effizienter als einzeln)

---

## 6c. Zusätzliche Bildtypen neben Bannern — Verbindliche Regeln

⛔ **Banner allein sind nicht genug.** Jede HTML-Datei braucht zusätzliche Bilder je nach Datei-Typ. Diese Regeln stammen aus den Skills `daf-bilder-pflicht`, `daf-html-layout` und `textgestaltung-daf`.

### Grundregel: Minimum 8 Fotos pro HTML-Datei

Aus dem Skill `daf-html-layout`:
> Minimum 8 Fotos müssen pro HTML-Übungsdatei integriert werden.
> Nur echte Fotos, keine UI-Elemente. Kein Foto doppelt. Auf möglichst viele Tabs verteilen.

### Bildtypen nach Datei-Typ

| Datei-Typ | Banner | Zusätzliche Bilder |
|-----------|--------|--------------------|
| **V** (Vokabular) | 6 Banner (je Tab) | **Vokabelkarten mit Fotos** (10–12 Karten): Jede Karte zeigt ein Pexels-Foto des Vokabels |
| **R** (Lesetext) | 6 Banner (je Tab) | **Bilder im Lesetext** (2–4 Fotos zwischen Absätzen) + **Vorentlastung Fotokarten** |
| **X** (Extra) | 4–5 Banner | **Situative Bilder** (Szenenfotos passend zu Dialogen/Übungen) |
| **G** (Grammatik) | 5 Banner | Banner reichen in der Regel aus |
| **S** (Speaking) | nach Bedarf | **Dialogsituations-Fotos** |

### 1. Vokabelkarten mit Fotos (V-Dateien)

Jede Vokabelkarte im Wörter-Tab (Tab 0) zeigt ein thematisches Foto:

```html
<div class="vocab-card">
  <img src="data:image/jpeg;base64,..." alt="der Tisch"
       style="width:100%;height:140px;object-fit:cover;border-radius:8px 8px 0 0;">
  <div class="vocab-info">
    <strong>der Tisch</strong>, -e
    <span class="vocab-en">table</span>
    <em>Auf dem Tisch liegt ein Buch.</em>
  </div>
</div>
```

- **10–12 Karten** pro V-Datei
- Jedes Foto muss das Wort visuell darstellen
- Einbettung als Base64 (wie Banner, gleicher Workflow §6a)

### 2. Bilder im Lesetext (R-Dateien)

Zwischen Absätzen des Lesetexts stehen thematische Fotos als `<figure>`:

```html
<figure style="margin:18px 0;text-align:center;">
    <img src="data:image/jpeg;base64,..." alt="Beschreibung"
         style="width:100%;max-width:600px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,0.12);">
    <figcaption style="margin-top:6px;font-size:0.85em;color:#667eea;font-weight:600;">
        Bildunterschrift
    </figcaption>
</figure>
```

- **2–4 Bilder** pro Lesetext, gleichmäßig verteilt
- Bilder illustrieren die Szene, nicht dekorieren
- `<figcaption>` ist Pflicht — beschreibt die Szene kurz

### 3. Vorentlastung Fotokarten (R-Dateien, Tab 0)

Im Vorentlastungs-Tab werden Schlüsselwörter als Fotokarten mit englischer Übersetzung präsentiert:

**Großes Grid (4–6 Karten, 2 Spalten):**
```css
.pre-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}
.pre-card img {
  height: 220px;
  object-fit: cover;
}
```

**Kleines Grid (8–12 Karten, 4 Spalten):**
```css
.pre-grid-small {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
}
.pre-card-small img {
  max-height: 160px;
  object-fit: cover;
}
```

### 4. Situative Bilder (X-Dateien)

X-Dateien zeigen Szenenfotos, die zur Übungssituation passen:
- Dialogübung über ein Vorstellungsgespräch → Foto einer Gesprächssituation im Büro
- Übung zu Naturkatastrophen → Foto einer Überschwemmung oder eines Sturms
- Diese Bilder stehen **innerhalb der Übung**, nicht nur als Banner

### Einbettungs-Workflow

Alle zusätzlichen Bilder werden nach dem gleichen Workflow wie Banner eingebettet (→ §6a):
1. Pexels-IDs sammeln
2. Chrome-MCP fetch → JSON Download
3. Python ersetzt URLs durch Base64

### Selbst-Check (Zusätzliche Bilder)

- [ ] V-Datei: Hat Tab 0 (Wörter) mindestens 10 Foto-Vokabelkarten?
- [ ] R-Datei: Stehen 2–4 `<figure>`-Bilder im Lesetext?
- [ ] R-Datei: Hat Tab 0 (Vorentlastung) Fotokarten im Grid?
- [ ] X-Datei: Gibt es situative Bilder passend zu den Übungen?
- [ ] Insgesamt: Mindestens 8 verschiedene Fotos in der gesamten Datei?
- [ ] Kein Foto doppelt verwendet?
- [ ] Alle Bilder als Base64 eingebettet (keine externen URLs)?

---

## 7. Arbeitsreihenfolge beim Erstellen einer neuen Datei

1. **Diesen Masterplan lesen** (diese Datei)
2. **Lingoda-PDF lesen** (`pdftotext` → vollständigen Inhalt extrahieren)
3. **Passende Skills lesen** (siehe Tabelle oben, Abschnitt 0)
4. **Bilder suchen** — Batch-Suche via Chrome-MCP (siehe Abschnitt 6 oben)
5. **Datei aufbauen** — Tab für Tab, alle Skill-Muster einhalten
6. **Bilder einbauen** — echte Pexels-URLs, kein SVG-Platzhalter
7. **Selbst-Check vor Browser-Test:**
   - [ ] Emojis über Text in Nav-Buttons?
   - [ ] Klasse `active` (nicht `aktiv`) für Nav-Button?
   - [ ] Kein Prüfen-Button?
   - [ ] Kein `placeholder="___"`?
   - [ ] Live-Feedback korrekt (erst `===`, dann `startsWith`)?
   - [ ] Timer: `.timer-controls` mit `.tc-buttons` links + `.tc-times` rechts? (KEIN `timer-bar`/`btn-row`!)
   - [ ] Satzbau nach Skill (`satzbau-drag-drop`)?
   - [ ] ⛔ Keine Satznummern (`Satz 1`, `Satz 2`, `idx+1`)?
   - [ ] Copyright-Footer unverändert?
   - [ ] Karim-Geschichte: Gedanken als `.gedanke`?
   - [ ] Vokabeln als `.hl` im Lesetext markiert?
   - [ ] ⛔ SVG-Platzhalter entfernt, echte Pexels-Bilder eingebaut?
   - [ ] Jeder Tab hat ein thematisch passendes Banner-Bild?
   - [ ] Zusätzliche Bilder je Datei-Typ (§6c) vorhanden?
8. **Browser-Test** — `daf-browser-test` Skill ausführen
9. **Fehler beheben und erneut testen** — so oft wie nötig, bis 0 Fehler
10. **Visuelle Bildprüfung** — nach §6b im Browser jeden Tab zoomen und bewerten
11. **Git commit & push** — direkt im Anschluss, ohne Nachfrage

---

## 8. GitHub — Repositories

| Niveau | Repo | GitHub Pages |
|--------|------|--------------|
| B1.1 | `fabDaF/daf-b1-uebungen` | `fabdaf.github.io/daf-b1-uebungen/` |
| A2.1 | (eigenes Repo) | (eigene URL) |

**Push-Regel:** Nach jedem abgeschlossenen Arbeitspaket wird **sofort** gepusht — ohne Rückfrage, ohne Verzögerung.

### GitHub-Token — Wo er zu finden ist

Das GitHub-Token (PAT) steht in der git-config des Cowork-Repos:

```
/sessions/eager-great-dirac/mnt/Cowork/htmlS/B1.1/.git/config
```

Abrufen:
```bash
grep "ghp_" /sessions/eager-great-dirac/mnt/Cowork/htmlS/B1.1/.git/config
```

In der Remote-URL des Push-Verzeichnisses setzen:
```bash
cd /tmp/b1push
git remote set-url origin https://ghp_TOKEN@github.com/fabDaF/daf-b1-uebungen.git
git push origin main
```

⚠️ `/tmp/b1push/` ist das temporäre Push-Verzeichnis. Es wird bei Session-Start neu geklont falls nötig:
```bash
git clone https://ghp_TOKEN@github.com/fabDaF/daf-b1-uebungen.git /tmp/b1push
```

---

## 9. Bekannte Bugs und Lösungen

### Bug 1: Satzbau-Chip bewegt sich nicht (Event-Bubbling)

**Symptom:** Chip-Click in Bank → Chip wandert in Row, aber bubbelt sofort zurück.
**Ursache:** `bank.addEventListener('click', ...)` feuert nach dem `chip.addEventListener('click', ...)`.
**Fix:** `e.stopPropagation()` im Chip-Click-Handler:

```javascript
chip.addEventListener('click', function(e) {
  e.stopPropagation(); // ← PFLICHT
  var row = document.getElementById('sb-row-' + idx);
  row.appendChild(chip);
  updateSbCaps(idx);
  colorSbRow(idx);
  timerAutoStart(3);
});
```

### Bug 2: Header nicht zentriert

**Symptom:** `.header` linksbündig.
**Fix:** `text-align: center` in `.header {}` ergänzen.

### Bug 3: Nav-Buttons nicht über volle Breite

**Symptom:** Tabs clustern links, viel Leerraum rechts.
**Fix:** `flex: 1` in `.nav-btn {}` ergänzen.

### Bug 4: Vokabel-Hervorhebung fehlt

**Symptom:** `.vocab-hl`-Elemente = 0, obwohl Lesetext vorhanden.
**Ursache:** `highlightVocabInText()` nicht implementiert oder nicht aufgerufen.
**Fix:** Funktion + Aufruf aus `lesetext-hervorhebung` SKILL.md einbauen.
Bei `WORT_DATA` mit `.answer`-Feld (nicht `.wort`): Kernwort so extrahieren:
```javascript
var core = ans.replace(/^(der|die|das)\s+/i, '').split(',')[0].trim();
```

### Bug 5: Satzbau falsch implementiert (wiederkehrender Fehler — März 2026)

**Symptom:** Satzbau wurde neu gebaut, aber ohne Skill-Standard gelesen zu haben.
Erkennungszeichen der FALSCHEN Implementierung:
- Variable heißt `SB_DATA` statt `satzbauData`
- Container-ID ist `sb-container` statt `satzbauContainer`
- Chips haben `linear-gradient` statt weißem Hintergrund mit lila Rand
- Klassen heißen `chip-bank`/`drop-row` statt `chips-container`/`sentence-builder`
- Funktionen: `buildSatzbau`, `colorSbRow`, `updateSbCaps`, `allowDrop`, `dropToRow`

**Ursache:** Satzbau aus dem Kopf implementiert statt `satzbau-drag-drop` SKILL.md gelesen.

**Fix:** IMMER zuerst `/sessions/.../skills/satzbau-drag-drop/SKILL.md` lesen,
dann vollständig nach Standard implementieren. Niemals „schnell" patchen.

**Validierung:** Nach jeder Migration zwingend ausführen:
```bash
python3 "/sessions/eager-great-dirac/mnt/.skills/skills/satzbau-drag-drop/check-satzbau-migration.py" DATEI.html
```
Erst wenn `✓ ALLES OK` gemeldet wird, ist die Migration abgeschlossen.

### Bug 6: Header-Design entspricht nicht dem Standard

**Symptom:** Header zeigt kleine Schrift, `.badge`-Chips für B1.1/Lektion/Lesen, keine Georgia-Schrift.
**Ursache:** Header aus dem Kopf gebaut statt `daf-html-layout` SKILL.md gelesen.
**Korrektes Pattern:**
```html
<div class="header">
  <h1>Titel der Übung</h1>
  <p style="font-family: Georgia, serif;">B1.1 · Lektion XXXX · Typ</p>
  <div class="big-emoji">🌍</div>
</div>
```
```css
.header h1 { font-size: 2.2em; font-family: Georgia, 'Times New Roman', serif; }
.header p  { font-size: 1.1em; font-family: Georgia, 'Times New Roman', serif; }
.header .big-emoji { font-size: 2.6em; display: block; margin-top: 8px; }
```
**KEINE `.badge`-Spans, KEIN `font-size: 1.45rem`.**

---

## 10. Pre-Flight-Checklist — Nachhaltige Fehlervermeidung

**Antwort auf: „Wie können wir diese Fehler nachhaltig beseitigen?"**

Jeder Bug, der mehr als einmal aufgetreten ist, wurde durch das **Überspringen der Skill-Lektüre** verursacht. Die einzige nachhaltige Lösung ist eine verbindliche Pre-Flight-Routine:

### Vor dem Erstellen einer neuen Datei — PFLICHT

- [ ] `daf-html-layout` SKILL.md gelesen? → Korrekte Header-, Nav-, Container-CSS, Wortschatz-Pattern
- [ ] Nav-HTML: `<div class="nav">` und `<div class="nav-btn">` (KEIN `<nav>` oder `<button>`)
- [ ] Wortschatz: `WORTSCHATZ[]` mit `type`/`artikel`/`de`/`plural` + `vocabContainer` (kein `WORT_DATA`, kein `wort-item`)
- [ ] Wortschatz: `#vocabContainer { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }` — **ZWEISPALTIG PFLICHT**
- [ ] Wortschatz: Responsiver Breakpoint `@media (max-width: 700px)` gesetzt?
- [ ] `satzbau-drag-drop` SKILL.md gelesen? (wenn Satzbau-Tab) → satzbauData, sbMakeChip, white chips
- [ ] `lesetext-hervorhebung` SKILL.md gelesen? (wenn Lesetext) → highlightVocabInText()
- [ ] `daf-bilder-pflicht` gelesen? → Tab-Banner für jeden Tab
- [ ] `textgestaltung-daf` gelesen? (wenn Lesetext) → Georgia, max-width, Blocksatz

### Vor dem Bearbeiten einer bestehenden Datei — PFLICHT

- [ ] Datei komplett gelesen (alle Teile — CSS, HTML, JS)?
- [ ] Entsprechende Skill-SKILL.md gelesen?
- [ ] `check-satzbau-migration.py` ausgeführt nach jeder Satzbau-Änderung?

### Nach Fertigstellung — PFLICHT

- [ ] `daf-browser-test` Skill ausgeführt?
- [ ] Alle 5 Phasen des Tests bestanden?
- [ ] Visuelle Bildprüfung nach §6b durchgeführt?
- [ ] Git commit & push durchgeführt?
- [ ] Dashboard-Badge aktualisiert?

### Bug 7: `<nav>`-Tag statt `<div class="nav">` — schwarze Linien zwischen Tabs

**Symptom:** Sichtbare schwarze Trennlinien zwischen den Tab-Reitern.
**Ursache:** HTML5 `<nav>`-Tag hat Browser-Default-Styling (outline, border) das CSS-Resets manchmal nicht vollständig überschreiben.
**Fix:** IMMER `<div class="nav">` verwenden — niemals das semantische `<nav>`-Tag:
```html
<!-- ❌ FALSCH -->
<nav class="nav"> ... </nav>

<!-- ✅ RICHTIG -->
<div class="nav"> ... </div>
```
Gleiches gilt für Nav-Buttons: `<div class="nav-btn">` statt `<button class="nav-btn">`.
Buttons erhalten Browser-Default-Borders und Focus-Outlines, die unerwünschte Linien erzeugen.

**Auch in §10 Pre-Flight-Checklist ergänzt** — Nav-HTML wird jetzt beim Layout-Check geprüft.

---

### Bug 8: Wortschatz-Tab mit `wort-item`/`WORT_DATA` statt Skill-Standard

**Symptom:** Wortschatz-Tab zeigt nur ein einziges Eingabefeld pro Wort, kein Artikel/Plural.
**Ursache:** Wortschatz aus dem Kopf gebaut, ohne `daf-html-layout` SKILL.md (Abschnitt „Wortschatz-Tab") gelesen zu haben.

**Erkennungszeichen der FALSCHEN Implementierung:**
- Variable heißt `WORT_DATA` mit `.answer`-Feld statt `WORTSCHATZ` mit `.type`/`.de`/`.artikel`/`.plural`
- CSS-Klassen: `wort-item`, `wort-prompt`, `wort-en` statt `vocab-item`, `vocab-en`, `vocab-inputs`
- Nur ein `input.blank` pro Zeile statt getrennter `.art`/`.wort`/`.plural`-Inputs
- Container heißt `wort-container` statt `vocabContainer`
- Funktionen: `buildWort`, `liveCheckWort`, `showWortLoesung`, `resetWort` statt `initVocab`, `vocabLiveCheck`, `showVocabLoesung`, `resetVocab`

**Fix:** `daf-html-layout` SKILL.md → Abschnitt „Wortschatz-Tab — VERBINDLICHES KOMPLETT-PATTERN" vollständig lesen und umsetzen. Datenformat:
```javascript
var WORTSCHATZ = [
  { id:1, type:'n', en:'...', artikel:'der', de:'Wort', plural:'Wörter' },
  { id:2, type:'v', en:'...', de:'machen' }
];
```

---

### Bug 9: Wortschatz-Tab einspaltig statt zweispaltig

**Symptom:** Alle Vokabelkarten stehen untereinander in einer einzigen Spalte — wirkt unübersichtlich und platzverschwendend auf breiten Bildschirmen.
**Ursache:** `#vocabContainer` erhält kein CSS-Grid, nur `flex-direction: column` oder gar kein Layoutmodell.

**Pflicht-CSS (nicht verhandelbar):**
```css
#vocabContainer {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}
@media (max-width: 700px) {
  #vocabContainer { grid-template-columns: 1fr; }
  .vocab-item { flex-direction: column; align-items: flex-start; }
}
```

**Warum 700px (nicht 600px)?** Drei Input-Felder (Artikel 70px + Wort 120px + Plural 120px + gaps) passen bei halber Container-Breite erst ab ca. 700px Viewport.

**Erkennung:** Wenn nach dem Tippen eines Testwortes die zweite Spalte leer und weit rechts erscheint → Grid fehlt.

**Fix:** Immer `display: grid; grid-template-columns: repeat(2, 1fr);` auf `#vocabContainer` setzen. Responsiver Breakpoint bei 700px. Input-Breiten: `.art` 70px, `.wort` 120px, `.plural` 120px.

**Auch in §10 Pre-Flight-Checklist ergänzt** — Zweispaltig wird jetzt beim Wortschatz-Check geprüft.

---

### Goldene Regel

> **Kein Code ohne Skill-Lektüre.** Die Zeit für das Lesen des Skills ist immer kürzer
> als die Zeit für das Reparieren eines Bugs, der durch Nicht-Lesen entstand.
> Frank hat dies vielfach korrigiert. Die Skills existieren, weil diese Fehler
> bereits gemacht wurden. Nutze sie.
