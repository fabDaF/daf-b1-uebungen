#!/usr/bin/env python3
"""
Pre-Deployment-Validierung für DaF-HTML-Dateien.

Prüft eine fertige HTML-Datei gegen die verbindlichen Skill-Standards
BEVOR sie auf GitHub gepusht wird. Erkennt den Dateityp automatisch
und wendet die passenden Prüfregeln an.

Verwendung:
    python3 pre-deploy-check.py DATEI.html
    python3 pre-deploy-check.py --all /pfad/zum/ordner/

Quellen:
    - daf-kern/SKILL.md + shared-rules.md
    - daf-lesetext/SKILL.md
    - daf-satzbau/SKILL.md
    - daf-uebungsformen/SKILL.md
    - daf-kern/references/daf-registry.json (canonical_values)

Rückgabewert:
    0 = alle Prüfungen bestanden
    1 = Fehler gefunden (nicht deployment-bereit)
"""

import re
import sys
import os
from pathlib import Path

# ═══════════════════════════════════════════
# FARBEN
# ═══════════════════════════════════════════
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def ok(msg):   return f"  {GREEN}✅ {msg}{RESET}"
def fail(msg): return f"  {RED}❌ {msg}{RESET}"
def warn(msg): return f"  {YELLOW}⚠️  {msg}{RESET}"
def info(msg): return f"  {CYAN}ℹ  {msg}{RESET}"

# ═══════════════════════════════════════════
# DATEITYP & NIVEAU ERKENNEN
# ═══════════════════════════════════════════
def detect_type(filename):
    m = re.search(r'_(\d{4})([RGVXSCW])', filename)
    return (m.group(2), m.group(1)) if m else (None, None)

def detect_level(filename):
    m = re.search(r'DE_(A1|A2|B1|B2|C1)_', filename)
    return m.group(1) if m else None

# ═══════════════════════════════════════════
# CSS-HELFER
# ═══════════════════════════════════════════
def get_style_block(html):
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    return m.group(1) if m else ''

def find_css_value(css, selector, prop):
    """Sucht einen CSS-Wert für einen Selektor."""
    esc = re.escape(selector)
    for match in re.finditer(esc + r'\s*\{([^}]*)\}', css):
        block = match.group(1)
        val = re.search(re.escape(prop) + r'\s*:\s*([^;]+)', block)
        if val:
            return val.group(1).strip()
    # Einzeilige Deklarationen: .header h1 { ... }
    for match in re.finditer(esc + r'\s*\{([^}]*)\}', css, re.DOTALL):
        block = match.group(1)
        val = re.search(re.escape(prop) + r'\s*:\s*([^;]+)', block)
        if val:
            return val.group(1).strip()
    return None

def css_has_selector(css, selector):
    return selector in css

def js_contains(html, func_name):
    m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
    return func_name in m.group(1) if m else False

# ═══════════════════════════════════════════
# A. SHARED RULES (alle Dateitypen)
# ═══════════════════════════════════════════
def check_shared_rules(html):
    results = []
    errors = 0
    results.append(f"\n{BOLD}═══ A. Shared Rules ═══{RESET}")

    # 1. Anführungszeichen: „...ASCII" oder „...englisch"
    bad = re.findall(r'„[^"\u201C]*[\u0022\u201D]', html)
    if bad:
        results.append(fail(f"Falsche Anführungszeichen: {len(bad)} Stellen"))
        errors += 1
    else:
        results.append(ok("Deutsche Anführungszeichen korrekt (U+201E / U+201C)"))

    # 2. Footer
    if 'author-footer' not in html:
        results.append(fail("Author-Footer fehlt komplett"))
        errors += 1
    elif 'fabdaf.onmicrosoft.com' in html:
        results.append(ok("Footer mit korrekter E-Mail (onmicrosoft.com)"))
    elif 'gmx.net' in html:
        results.append(fail("Footer enthält private GMX-Adresse statt onmicrosoft.com"))
        errors += 1
    else:
        results.append(warn("Footer vorhanden — E-Mail manuell prüfen"))

    # 3. Kein Prüfen-Button
    pruefen = re.findall(r'(?i)>\s*(?:Prüfen|Check|Auswerten)\s*<', html)
    if pruefen:
        results.append(fail(f"Verbotener Prüfen-Button: {pruefen}"))
        errors += 1
    else:
        results.append(ok("Kein Prüfen-Button"))

    # 4. Keine Satznummerierung (Satz 1, Satz 2, ... im UI)
    if re.search(r"'Satz\s*'\s*\+|'Satz\s*'\s*\+\s*\(|Satz.*idx\s*\+\s*1|textContent\s*=.*Satz.*\+.*idx", html):
        results.append(fail("Satznummerierung gefunden"))
        errors += 1
    else:
        results.append(ok("Keine Satznummerierung"))

    # 5. Tab-Namen ohne Codes
    codes = re.findall(r'>[GVRXCSW]\d\s*[·:\-]', html)
    if codes:
        results.append(fail(f"Interne Tab-Codes in Nav: {codes}"))
        errors += 1
    else:
        results.append(ok("Tab-Namen ohne interne Codes"))

    # 6. Direct-Feedback / Timer (startTimer = Aufwärts-Timer, timerAutoStart = Legacy)
    if js_contains(html, 'startTimer') or js_contains(html, 'timerAutoStart'):
        results.append(ok("Timer-System vorhanden (startTimer/timerAutoStart)"))
    else:
        results.append(fail("Timer-System fehlt (weder startTimer noch timerAutoStart)"))
        errors += 1

    return results, errors

# ═══════════════════════════════════════════
# B. DAF-KERN LAYOUT (alle Dateitypen)
# ═══════════════════════════════════════════
def check_kern_layout(html, css):
    results = []
    errors = 0
    results.append(f"\n{BOLD}═══ B. daf-kern Layout ═══{RESET}")

    checks = [
        ('.container', 'max-width',     '1000px'),
        ('.container', 'border-radius', '12px'),
        ('.header h1', 'font-size',     '2.2em'),
    ]
    for sel, prop, expected in checks:
        val = find_css_value(css, sel, prop)
        if val == expected:
            results.append(ok(f"{sel} {prop}: {expected}"))
        else:
            results.append(fail(f"{sel} {prop}: {val} (soll: {expected})"))
            errors += 1

    # Header font-family muss Georgia enthalten
    h1_ff = find_css_value(css, '.header h1', 'font-family')
    if h1_ff and 'Georgia' in h1_ff:
        results.append(ok("Header h1: Georgia serif"))
    else:
        results.append(fail(f"Header h1 font-family: {h1_ff} (soll: Georgia)"))
        errors += 1

    # Big-Emoji
    if 'big-emoji' in html:
        if re.search(r'<h1[^>]*>[^<]*[\U0001F300-\U0001FAFF]', html):
            results.append(fail("Emoji im <h1> statt in eigenem .big-emoji div"))
            errors += 1
        else:
            results.append(ok("Big-Emoji als eigenes div"))
    else:
        results.append(fail("Kein .big-emoji gefunden"))
        errors += 1

    # Tab-Banner
    sections = len(re.findall(r'class="section(?:\s+active)?"', html))
    banners  = len(re.findall(r'tab-banner', html))
    if banners >= sections and banners > 0:
        results.append(ok(f"Tab-Banner: {banners}/{sections} Sections"))
    elif banners > 0:
        results.append(warn(f"Tab-Banner: nur {banners} von {sections} Sections"))
    else:
        results.append(fail("Keine Tab-Banner gefunden"))
        errors += 1

    return results, errors

# ═══════════════════════════════════════════
# C. DAF-LESETEXT (R-Dateien)
# ═══════════════════════════════════════════
def check_lesetext(html, css, level):
    results = []
    errors = 0
    results.append(f"\n{BOLD}═══ C. daf-lesetext (R-Datei) ═══{RESET}")

    # .story-text CSS-Werte lt. Skill
    story_checks = [
        ('max-width',   '600px'),
        ('line-height', '1.8'),
        ('text-align',  'justify'),
        ('color',       '#1a1a1a'),
    ]
    for prop, expected in story_checks:
        val = find_css_value(css, '.story-text', prop)
        if val == expected:
            results.append(ok(f".story-text {prop}: {expected}"))
        elif val:
            results.append(fail(f".story-text {prop}: {val} (soll: {expected})"))
            errors += 1
        else:
            results.append(fail(f".story-text {prop}: nicht gefunden (soll: {expected})"))
            errors += 1

    # Font-family (enthält Georgia)
    ff = find_css_value(css, '.story-text', 'font-family')
    if ff and 'Georgia' in ff:
        results.append(ok(".story-text: Georgia serif"))
    else:
        results.append(fail(f".story-text font-family: {ff} (soll: Georgia)"))
        errors += 1

    # font-size
    fs = find_css_value(css, '.story-text', 'font-size')
    if fs == '1.05em':
        results.append(ok(".story-text font-size: 1.05em"))
    elif fs:
        results.append(fail(f".story-text font-size: {fs} (soll: 1.05em)"))
        errors += 1

    # text-indent
    ti = find_css_value(css, '.story-text p', 'text-indent')
    if ti == '1.4em':
        results.append(ok(".story-text p text-indent: 1.4em"))
    elif ti:
        results.append(fail(f".story-text p text-indent: {ti} (soll: 1.4em)"))
        errors += 1

    # R/F-Layout
    results.append(f"\n  {CYAN}── Richtig/Falsch ──{RESET}")
    rf_mw = find_css_value(css, '.rf-list', 'max-width')
    if rf_mw == '650px':
        results.append(ok(".rf-list max-width: 650px"))
    elif css_has_selector(css, '.rf-list'):
        results.append(fail(f".rf-list max-width: {rf_mw} (soll: 650px)"))
        errors += 1

    rf_br = find_css_value(css, '.rf-btn', 'border-radius')
    if rf_br and '14px' in rf_br:
        results.append(ok(".rf-btn: Pill-Form (14px)"))
    elif rf_br:
        results.append(fail(f".rf-btn border-radius: {rf_br} (soll: 14px)"))
        errors += 1

    rf_border = find_css_value(css, '.rf-btn', 'border')
    if rf_border and '#9b59b6' in rf_border:
        results.append(ok(".rf-btn: lila Rand (#9b59b6)"))
    elif rf_border:
        results.append(fail(f".rf-btn border: {rf_border} (soll: #9b59b6)"))
        errors += 1

    # Vokabel-Hervorhebung
    results.append(f"\n  {CYAN}── Vokabel-Hervorhebung ──{RESET}")
    if css_has_selector(css, '.vocab-hl'):
        results.append(ok(".vocab-hl CSS vorhanden"))
    else:
        results.append(fail(".vocab-hl CSS fehlt"))
        errors += 1

    if js_contains(html, 'highlightVocabInText'):
        results.append(ok("highlightVocabInText() vorhanden"))
    else:
        results.append(fail("highlightVocabInText() fehlt"))
        errors += 1

    # Bilder im Text
    figures = len(re.findall(r'<figure', html))
    if figures >= 2:
        results.append(ok(f"{figures} <figure>-Bilder im Text"))
    elif figures == 1:
        results.append(warn("Nur 1 Bild (2–3 empfohlen)"))
    else:
        results.append(fail("Keine <figure>-Bilder im Lesetext"))
        errors += 1

    # Voice Lock
    results.append(f"\n  {CYAN}── Voice Lock ──{RESET}")
    if level == 'B1':
        if re.search(r'Karim', html):
            results.append(ok("B1: Karim Benali erkannt"))
        else:
            results.append(fail("B1: Kein 'Karim' — soll Karim-Benali-Geschichte sein"))
            errors += 1
    elif level == 'B2':
        results.append(info("B2: Wissenschaftsjournalist — manuell prüfen"))
    else:
        results.append(info(f"{level}: Kein Voice Lock definiert"))

    # Dialog-CSS
    if css_has_selector(css, '.dialog'):
        results.append(ok(".dialog CSS definiert"))
    else:
        results.append(warn(".dialog CSS nicht definiert (ok falls keine Dialoge)"))

    return results, errors

# ═══════════════════════════════════════════
# D. SATZBAU (alle mit Satzbau-Tab)
# ═══════════════════════════════════════════
def check_satzbau(html):
    if not js_contains(html, 'satzbauData') and not js_contains(html, 'SATZBAU'):
        return [], 0

    results = []
    errors = 0
    results.append(f"\n{BOLD}═══ D. daf-satzbau ═══{RESET}")

    if js_contains(html, 'getSbCursor') and js_contains(html, 'sbDragged'):
        results.append(ok("Moderne Architektur (getSbCursor + sbDragged)"))
    elif js_contains(html, "getData"):
        results.append(fail("Veraltete Architektur (getData)"))
        errors += 1
    else:
        results.append(warn("Satzbau-Architektur nicht eindeutig erkannt"))

    # Prüfe ob Sätze multiple valid orders haben
    script = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
    if script:
        js = script.group(1)
        valid_blocks = re.findall(r'valid\s*:\s*\[(\[.*?\])\s*\]', js, re.DOTALL)
        single = sum(1 for v in valid_blocks if v.count('[') <= 1)
        multi  = len(valid_blocks) - single
        if single > 0:
            results.append(warn(f"{single}/{len(valid_blocks)} Sätze mit nur 1 gültiger Reihenfolge"))
        if multi > 0:
            results.append(ok(f"{multi}/{len(valid_blocks)} Sätze mit mehreren gültigen Reihenfolgen"))

    # Prüfe Großschreibung: Nicht-Nomen dürfen in parts NICHT großgeschrieben sein
    # (sbUpdateCapitalization() kapitalisiert das erste Wort automatisch)
    if script:
        js = script.group(1)
        NON_NOUNS = {
            # Artikel
            'der', 'die', 'das', 'ein', 'eine', 'einer', 'eines', 'einem', 'einen',
            'dem', 'den', 'des',
            # Pronomen
            'er', 'sie', 'es', 'wir', 'ihr', 'ich', 'du', 'man', 'sich',
            'mein', 'dein', 'sein', 'unser', 'euer',
            'meine', 'deine', 'seine', 'unsere', 'eure', 'ihre',
            'dieser', 'diese', 'dieses', 'diesem', 'diesen',
            'jeder', 'jede', 'jedes', 'jedem', 'jeden',
            'alle', 'viele', 'einige', 'manche', 'welche',
            # Präpositionen
            'in', 'an', 'auf', 'mit', 'bei', 'zu', 'von', 'aus', 'nach',
            'über', 'unter', 'für', 'durch', 'gegen', 'ohne', 'um',
            'vor', 'hinter', 'neben', 'zwischen', 'seit', 'bis', 'während',
            'wegen', 'trotz', 'statt', 'außer', 'ab', 'zum', 'zur', 'vom', 'im', 'am',
            # Konjunktionen
            'und', 'oder', 'aber', 'weil', 'dass', 'wenn', 'ob', 'obwohl',
            'damit', 'nachdem', 'bevor', 'als', 'während', 'sondern', 'denn',
            'sodass', 'falls', 'sobald', 'solange', 'indem', 'seitdem',
            # Adverbien (häufige)
            'nicht', 'auch', 'nur', 'noch', 'schon', 'sehr', 'immer',
            'oft', 'dann', 'dort', 'hier', 'heute', 'deshalb', 'trotzdem',
            'außerdem', 'dabei', 'daher', 'deswegen', 'dennoch',
            # Verben (häufige, die am Satzanfang stehen können bei Inversion)
            'kann', 'muss', 'soll', 'will', 'darf', 'mag',
            'hat', 'ist', 'sind', 'war', 'wird', 'werden', 'wurde',
            'haben', 'sein', 'können', 'müssen', 'sollen', 'wollen', 'dürfen',
            # Relativpronomen etc.
            'was', 'wer', 'wo', 'wie', 'warum', 'wann',
        }
        parts_blocks = re.findall(r"parts\s*:\s*\[(.*?)\]", js, re.DOTALL)
        cap_errors = 0
        for i, block in enumerate(parts_blocks, 1):
            words = re.findall(r"'([^']+)'", block)
            for word in words:
                if word[0].isupper() and word.lower() in NON_NOUNS:
                    results.append(fail(
                        f"Satz {i}: '{word}' ist großgeschrieben, aber kein Nomen → '{word.lower()}'"
                    ))
                    cap_errors += 1
                    errors += 1
        if cap_errors == 0 and parts_blocks:
            results.append(ok("Alle Nicht-Nomen in parts korrekt kleingeschrieben"))

    return results, errors

# ═══════════════════════════════════════════
# E. WORTSCHATZ-PATTERN (G/V + alle mit Wortschatz)
# ═══════════════════════════════════════════
def check_wortschatz_pattern(html):
    if not js_contains(html, 'ortschatz') and not js_contains(html, 'WORTSCHATZ'):
        return [], 0

    results = []
    errors = 0
    results.append(f"\n{BOLD}═══ E. Wortschatz-Pattern ═══{RESET}")

    has_wortschatz = js_contains(html, 'initWortschatz') or js_contains(html, 'wortschatzCheck')
    has_vocab = js_contains(html, 'initVocab') or js_contains(html, 'vocabLiveCheck')
    if has_wortschatz or has_vocab:
        results.append(ok("Wortschatz-Pattern vorhanden (initWortschatz/initVocab)"))
    else:
        results.append(fail("Wortschatz-Pattern fehlt"))
        errors += 1

    return results, errors

# ═══════════════════════════════════════════
# HAUPTFUNKTION
# ═══════════════════════════════════════════
def validate_file(filepath):
    filename = os.path.basename(filepath)
    typ, nr  = detect_type(filename)
    level    = detect_level(filename)

    print(f"\n{BOLD}{'═' * 60}")
    print(f"  PRE-DEPLOYMENT CHECK: {filename}")
    print(f"  Typ: {typ or '?'}  |  Nr: {nr or '?'}  |  Niveau: {level or '?'}")
    print(f"{'═' * 60}{RESET}")

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    css = get_style_block(html)
    all_results = []
    total_errors = 0

    # Immer: Shared Rules + Kern Layout
    for check in [
        lambda: check_shared_rules(html),
        lambda: check_kern_layout(html, css),
    ]:
        r, e = check()
        all_results.extend(r)
        total_errors += e

    # Typ-spezifisch: Lesetext für R-Dateien
    if typ == 'R':
        r, e = check_lesetext(html, css, level)
        all_results.extend(r)
        total_errors += e

    # Allgemein: Satzbau + Wortschatz
    for check in [
        lambda: check_satzbau(html),
        lambda: check_wortschatz_pattern(html),
    ]:
        r, e = check()
        all_results.extend(r)
        total_errors += e

    # Ausgabe
    for line in all_results:
        print(line)

    print(f"\n{BOLD}{'─' * 60}")
    if total_errors == 0:
        print(f"  {GREEN}✅ DEPLOYMENT-BEREIT — 0 Fehler{RESET}")
    else:
        print(f"  {RED}❌ NICHT DEPLOYMENT-BEREIT — {total_errors} Fehler{RESET}")
    print(f"{'─' * 60}{RESET}\n")

    return total_errors

# ═══════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Verwendung: python3 {sys.argv[0]} DATEI.html [DATEI2.html ...]")
        print(f"            python3 {sys.argv[0]} --all /pfad/zum/ordner/")
        sys.exit(1)

    files = []
    if sys.argv[1] == '--all' and len(sys.argv) > 2:
        folder = sys.argv[2]
        files = sorted(Path(folder).glob('DE_*.html'))
    else:
        files = [Path(f) for f in sys.argv[1:]]

    total = 0
    failed_count = 0
    for f in files:
        if not f.exists():
            print(f"{RED}Datei nicht gefunden: {f}{RESET}")
            continue
        errs = validate_file(str(f))
        total += 1
        if errs > 0:
            failed_count += 1

    if total > 1:
        print(f"\n{BOLD}{'═' * 60}")
        print(f"  GESAMTERGEBNIS: {total - failed_count}/{total} bestanden")
        print(f"{'═' * 60}{RESET}")

    sys.exit(1 if failed_count > 0 else 0)
