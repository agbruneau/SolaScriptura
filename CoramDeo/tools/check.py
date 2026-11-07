# -*- coding: utf-8 -*-
"""Contrôle du dépôt, en local et en intégration continue (stdlib seulement).

    python tools/check.py            erreurs -> code de retour 1
    python tools/check.py --strict   les avertissements comptent aussi comme erreurs
    python tools/check.py --fix      corrige les ligatures (seule règle corrigible sans jugement)

Chaque règle rapporte un compte et quelques exemples. Les règles de EN_COURS sont des
avertissements tant que le lot qui les satisfait n'est pas terminé.
"""
import glob
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages  # noqa: E402

ROOT = pages.ROOT
EN_COURS = set()
SECTIONS_MD = ['Contexte du passage', 'Arrière-plan historique et culturel', 'Étude des mots-clés',
               'Apports des commentateurs', 'Renvois et passages parallèles', 'Thèmes théologiques',
               'Pistes de réflexion']
IDS = ['contexte', 'arriere-plan', 'mots-cles', 'commentateurs', 'renvois', 'themes', 'reflexion']
# Liste fermée : « coexister », « goel », « Zoé », « coercition » ne doivent pas être touchés.
LIGATURES = re.compile(r'\b(?:contre|ran|é)?coeurs?\b|\bchoeurs?\b|\b(?:dés)?oeuvr\w*|\bmanoeuvr\w*|'
                       r'\boeil\b|\bvoeux?\b|\bsoeurs?\b|\bboeufs?\b|\bnoeuds?\b|\bmoeurs\b|\boecum\w*',
                       re.I)
SERIE_INTERDITS = ['Propositions de titre', 'Arc narratif', 'Recommandation pour le lancement']
GTY = re.compile(r'https?://(?:www\.)?gty\.org/(?:[^\s"\')<>]*/)?sermons(?:-library)?/([A-Za-z]*\d[\w-]*)')


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, '/')


def html_pages():
    return sorted(p for p in glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)
                  if os.sep + '.claude' + os.sep not in p)


def check_links(add):
    files = html_pages() + [os.path.join(ROOT, 'README.md')]
    for p in files:
        s = read(p)
        targets = re.findall(r'(?:href|src)="([^"#?]+)', s) if p.endswith('.html') else \
            re.findall(r'\]\(<([^>]+)>\)|\]\(([^)<\s]+)\)', s)
        for t in targets:
            t = t if isinstance(t, str) else (t[0] or t[1])
            if re.match(r'[a-z]+:', t) or not t:
                continue
            path = os.path.normpath(os.path.join(os.path.dirname(p), urllib.parse.unquote(t.split('#')[0])))
            if not os.path.exists(path):
                add('liens', f'{rel(p)} -> {t}')


def check_pages(add):
    for p in html_pages():
        s = read(p)
        for a in re.findall(r'<a\b([^>]*)>(.*?)</a>', s, re.S):
            name = re.sub(r'<[^>]+>', '', a[1]).strip() or 'aria-label=' in a[0] or \
                re.search(r'alt="[^"]+"', a[1])
            if not name:
                add('liens-sans-nom', rel(p))
        if 'class="footer__line footer__ia"' not in s:
            add('declaration-ia', rel(p))
        if '@media print' not in s:
            add('impression', rel(p))
        for m in LIGATURES.finditer(re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)):
            add('ligatures', f'{rel(p)} : {m.group(0)}')


def check_pericopes(add):
    index = set()
    idx_path = os.path.join(ROOT, 'tools', 'gty-index.json')
    if os.path.exists(idx_path):
        index = {e['code'] for e in json.loads(read(idx_path))}
    else:
        add('index-sermons', 'tools/gty-index.json absent')
    couverture = json.loads(read(os.path.join(ROOT, 'tools', 'couverture.json')))
    for d in pages.pericope_dirs():
        r = rel(d)
        s = read(os.path.join(d, 'index.html'))
        ids = re.findall(r'<article class="section[^"]*" id="([^"]+)"', s)
        if ids != IDS:
            add('sections-html', f'{r} : {ids}')
        try:
            md_path = pages.research_md(d)
        except ValueError as e:
            add('sections-md', str(e))
            continue
        md = read(md_path)
        heads = re.findall(r'^## (.+)$', md, re.M)
        if heads != SECTIONS_MD:
            add('sections-md', f'{r} : {heads}')
        # les titres de sermon gty.org sont cités tels quels : exclus de la règle
        if '—' in re.sub(r'<a href="https://www\.gty\.org[^>]*>.*?</a>', '', s.split('<main>')[-1]) or \
                '—' in re.sub(r'\[[^\]]*\]\(https://www\.gty\.org[^)]*\)', '', md):
            add('tiret-cadratin', r)
        for m in LIGATURES.finditer(md):
            add('ligatures', f'{rel(md_path)} : {m.group(0)}')
        try:
            h = pages.source_hash(pages.extract(s))
        except ValueError as e:
            add('extraction', f'{r} : {e}')
            continue
        if f'<!-- source_hash: {h} -->' not in md:
            add('md-perime', r)
        pdf = os.path.splitext(md_path)[0] + '.pdf'
        with open(pdf, 'rb') as f:
            if f'/Keywords ({h})'.encode() not in f.read():
                add('pdf-perime', r)
        if 'Niveau de source :</b>' not in s:
            add('niveau-source', r)
        for code in GTY.findall(s):
            if index and code not in index:
                add('code-hors-index', f'{r} : {code}')
        if r not in couverture:
            add('attribution-verifiee', r)


def check_series(add):
    for p in sorted(glob.glob(os.path.join(ROOT, '3 - Pérégrination', '*', '00 - Introduction', 'Serie.md'))):
        s = read(p)
        for t in SERIE_INTERDITS:
            if t in s:
                add('serie-sections-interdites', f'{rel(p)} : {t}')
        for m in LIGATURES.finditer(s):
            add('ligatures', f'{rel(p)} : {m.group(0)}')
        src = os.path.join(os.path.dirname(p), 'Serie.json')
        if not os.path.exists(src):
            add('serie-source', f'{rel(p)} : Serie.json absent')
            continue
        data = json.loads(read(src))
        h = pages.source_hash(data)
        if f'<!-- source_hash: {h} -->' not in s:
            add('serie-md-perime', rel(p))
        with open(os.path.splitext(p)[0] + '.pdf', 'rb') as f:
            if f'/Keywords ({h})'.encode() not in f.read():
                add('serie-pdf-perime', rel(p))
        units = data.get('pericope_division', [])
        if not units or any(not u.get('unit_basis') for u in units):
            add('serie-base-decoupage', rel(p))
        if not data.get('argument_structure'):
            add('serie-structure-argument', rel(p))
        texts = data.get('difficult_texts', [])
        if len(texts) < 3 or any(not all(t.get(k) for k in ('passage', 'issue', 'macarthur_reading', 'source_level'))
                                 for t in texts):
            add('serie-textes-exigeants', rel(p))


def check_readme(add):
    s = read(os.path.join(ROOT, 'README.md'))
    n_pages = len(html_pages())
    n_peri = len(pages.pericope_dirs())
    for needle in (f'{n_pages} pages `index.html`', f'{n_peri} péricopes'):
        if needle not in s:
            add('readme-comptes', f'README ne contient pas « {needle} »')
    dirs = glob.glob(os.path.join(ROOT, '[1-4] - *' + os.sep)) + \
        glob.glob(os.path.join(ROOT, '[12] - *', '*' + os.sep)) + \
        glob.glob(os.path.join(ROOT, '3 - *', '00 - *' + os.sep))
    for d in sorted(dirs):
        if os.path.basename(os.path.dirname(d)) not in s:
            add('readme-dossiers', f'dossier non documenté : {rel(d)}')


def ligature(m):
    w = m.group(0)
    i = w.lower().index('oe')
    return w[:i] + ('Œ' if w[i] == 'O' else 'œ') + w[i + 2:]


def fix_ligatures():
    files = html_pages() + glob.glob(os.path.join(ROOT, '[1-4] - *', '**', '*.md'), recursive=True) + \
        glob.glob(os.path.join(ROOT, '3 - *', '*', '00 - Introduction', 'Serie.json'))
    changed = 0
    for p in files:
        s = read(p)
        new = LIGATURES.sub(ligature, s)
        if new != s:
            with open(p, 'w', encoding='utf-8', newline='') as f:
                f.write(new)
            changed += 1
    print(f'ligatures corrigées dans {changed} fichiers')


def main(argv):
    sys.stdout.reconfigure(encoding='utf-8')
    if '--fix' in argv:
        fix_ligatures()
        return 0
    strict = '--strict' in argv
    found = {}

    def add(rule, detail):
        found.setdefault(rule, []).append(detail)

    for check in (check_links, check_pages, check_pericopes, check_series, check_readme):
        check(add)
    errors = 0
    for rule, details in sorted(found.items()):
        level = 'AVERT' if rule in EN_COURS and not strict else 'ERREUR'
        errors += level == 'ERREUR'
        print(f'{level:6} {rule:28} {len(details):5}   ex. {details[0]}')
    print('OK' if not errors else f'{errors} règle(s) en erreur')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
