# -*- coding: utf-8 -*-
"""Sources MacArthur d'une péricope : sermons Grace to You (index) et notes de la Bible d'étude.

    python tools/sources.py index <capture.json>      reconstruit tools/gty-index.json
    python tools/sources.py match [dossier ...]       sermons et notes retenus, par péricope
    python tools/sources.py inject [dossier ...]      pose le niveau de source dans le HTML
    python tools/sources.py --selftest

La capture vient de l'archive gty.org par Écriture (https://www.gty.org/sermons/archive?tab=scripture),
dont la page interroge /api/website/sermons-by-field?book=<livre> ; un objet par sermon
(code, date, scripture, title, series). Aucun code de sermon ne s'écrit ailleurs que depuis cet index.

Règle d'appariement : un sermon est retenu si l'un de ses passages chevauche la péricope ; les
sermons au niveau du verset priment, ceux qui portent sur un chapitre entier ou plus ne sont retenus
qu'à défaut ; un sermon sans chapitre (« Matthew ») n'est jamais retenu.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages  # noqa: E402

INDEX = os.path.join(pages.ROOT, 'tools', 'gty-index.json')
SOURCES = os.environ.get('CORAMDEO_SOURCES') or os.path.join(os.path.expanduser('~'), 'CoramDeo-sources')
END = 999  # « fin du chapitre »

# dossier du corpus -> (nom français dans les passages, nom anglais gty.org, abréviation des notes)
BOOKS = {
    '01 - Genèse': ('Genèse', 'Genesis', 'Gn'), '19 - Psaume 19': ('Psaume', 'Psalm', 'Ps'),
    '19 - Psaume 119': ('Psaume', 'Psalm', 'Ps'), '40 - Matthieu': ('Matthieu', 'Matthew', 'Mt'),
    '41 - Marc': ('Marc', 'Mark', 'Mc'), '42 - Luc': ('Luc', 'Luke', 'Lc'), '43 - Jean': ('Jean', 'John', 'Jn'),
    '44 - Actes': ('Actes', 'Acts', 'Ac'), '45 - Romains': ('Romains', 'Romans', 'Rm'),
    '46 - 1 Corinthiens': ('1 Corinthiens', '1 Corinthians', '1 Co'),
    '47 - 2 Corinthiens': ('2 Corinthiens', '2 Corinthians', '2 Co'), '48 - Galates': ('Galates', 'Galatians', 'Ga'),
    '49 - Éphésiens': ('Éphésiens', 'Ephesians', 'Ep'), '50 - Philippiens': ('Philippiens', 'Philippians', 'Ph'),
    '51 - Colossiens': ('Colossiens', 'Colossians', 'Col'),
    '52 - 1 Thessaloniciens': ('1 Thessaloniciens', '1 Thessalonians', '1 Th'),
    '53 - 2 Thessaloniciens': ('2 Thessaloniciens', '2 Thessalonians', '2 Th'),
    '54 - 1 Timothée': ('1 Timothée', '1 Timothy', '1 Tm'), '55 - 2 Timothée': ('2 Timothée', '2 Timothy', '2 Tm'),
    '56 - Tite': ('Tite', 'Titus', 'Tt'), '57 - Philémon': ('Philémon', 'Philemon', 'Phm'),
    '58 - Hébreux': ('Hébreux', 'Hebrews', 'Hé'), '59 - Jacques': ('Jacques', 'James', 'Jc'),
    '60 - 1 Pierre': ('1 Pierre', '1 Peter', '1 P'), '61 - 2 Pierre': ('2 Pierre', '2 Peter', '2 P'),
    '62 - 1 Jean': ('1 Jean', '1 John', '1 Jn'), '63 - 2 Jean': ('2 Jean', '2 John', '2 Jn'),
    '64 - 3 Jean': ('3 Jean', '3 John', '3 Jn'), '65 - Jude': ('Jude', 'Jude', 'Jude'),
    '66 - Apocalypse': ('Apocalypse', 'Revelation', 'Ap'),
}
EN_FR = {en: fr for fr, en, _ in BOOKS.values()}
SINGLE = {'Philemon', '2 John', '3 John', 'Jude', 'Obadiah'}
PSALM_TITLE_SHIFT = {19: 1}  # psaumes du corpus dont la suscription est le verset 1 en NEG


def parse_scripture(s):
    """« Matthew 26:57, 59–61; 1 Corinthians 7:1–7 » -> [(livre, (c, v), (c, v)) ...] ; (livre, None, None) si sans chapitre."""
    refs, book = [], None
    s = s.replace('\xad', '').replace('–', '-').replace('—', '-')
    s = re.sub(r'\s*:\s*', ':', s)
    s = re.sub(r'\s*-\s*', '-', s)
    s = re.sub(r'(\d)[a-d]-[a-d]\b', r'\1', s).replace(' and ', ', ')  # « 2:13a-b » : un seul verset
    for seg in s.split(';'):
        seg = seg.strip()
        m = re.match(r'^((?:[123] )?[A-Z][a-z]+(?: of [A-Z][a-z]+)?)\s*(.*)$', seg)
        if m:
            book, seg = m.group(1), m.group(2)
        if book is None:
            continue
        if not seg:
            refs.append((book, None, None))
            continue
        ch = 1 if book in SINGLE else None
        for part in seg.split(','):
            part = re.sub(r'(\d)[a-d]\b', r'\1', part.strip())
            part = re.sub(r'^(\d+:\d+) (\d+)$', r'\1-\2', part)
            if m := re.fullmatch(r'(\d+):(\d+)-(\d+):(\d+)', part):
                c, v, c2, v2 = map(int, m.groups())
                refs.append((book, (c, v), (c2, v2)))
                ch = c2
            elif m := re.fullmatch(r'(\d+):(\d+)(?:-(\d+))?', part):
                c, v = int(m.group(1)), int(m.group(2))
                refs.append((book, (c, v), (c, int(m.group(3) or v))))
                ch = c
            elif m := re.fullmatch(r'(\d+)(?:-(\d+))?', part):
                a, b = int(m.group(1)), int(m.group(2) or m.group(1))
                if ch is not None:
                    refs.append((book, (ch, a), (ch, b)))
                else:
                    refs.append((book, (a, 1), (b, END)))
    return refs


def parse_passage(passage):
    """« Genèse 1.3-2.3 » -> ('Genèse', (1, 3), (2, 3))."""
    # « 9.1-19a » : le demi-verset compte comme le verset entier ; « 21.37 à 22.21 » : plage
    m = re.fullmatch(r'((?:[123] )?\D+?) (\d+)\.(\d+)[ab]?(?:(?:-| à )(?:(\d+)\.)?(\d+)[ab]?)?', passage.strip())
    if not m:
        raise ValueError(f'passage illisible : {passage!r}')
    c, v = int(m.group(2)), int(m.group(3))
    c2 = int(m.group(4) or c)
    v2 = int(m.group(5) or v)
    return m.group(1), (c, v), (c2, v2)


def overlaps(a1, a2, b1, b2):
    return a1 <= b2 and b1 <= a2


def fr_ref(book, start, end):
    fr = EN_FR.get(book, book)
    if start[0] == end[0]:
        if start[1] == 1 and end[1] == END:
            return f'{fr} {start[0]}'
        return f'{fr} {start[0]}.{start[1]}' + (f'-{end[1]}' if end[1] != start[1] else '')
    if start[1] == 1 and end[1] == END:
        return f'{fr} {start[0]}-{end[0]}'
    return f'{fr} {start[0]}.{start[1]}-{end[0]}.{end[1] if end[1] != END else "fin"}'


def build_index(capture):
    out = []
    for e in capture:
        refs = parse_scripture(e['scripture'])
        out.append({'code': e['code'], 'title': e['title'], 'date': e['date'], 'scripture': e['scripture'],
                    'series': e.get('series', ''),
                    'refs': [[b, *(s or (None, None)), *(t or (None, None))] for b, s, t in refs]})
    return sorted(out, key=lambda x: x['code'])


# Références corrigées à la main là où les métadonnées gty sont plus étroites que le sermon (vérifié à la transcription).
REF_OVERRIDES = {'63-1': [['2 John', 1, 1, 1, 4]], '63-2': [['2 John', 1, 1, 1, 4]]}


def load_index():
    with open(INDEX, encoding='utf-8') as f:
        index = json.load(f)
    for e in index:
        e['refs'] = REF_OVERRIDES.get(e['code'], e['refs'])
    return index


def book_of(d):
    return BOOKS[os.path.basename(os.path.dirname(d))]


def to_english(en, start, end):
    """La NEG numérote la suscription d'un psaume comme verset 1 ; la numérotation anglaise, non."""
    shift = PSALM_TITLE_SHIFT.get(start[0], 0) if en == 'Psalm' else 0
    return (start[0], max(1, start[1] - shift)), (end[0], max(1, end[1] - shift))


def sermons_for(d, index, passage=None):
    fr, en, _ = book_of(d)
    _, p1, p2 = parse_passage(passage or pages.load(d)['passage'])
    p1, p2 = to_english(en, p1, p2)
    verse_level, chapter_level = [], []
    for e in index:
        hits = [(tuple(r[1:3]), tuple(r[3:5])) for r in e['refs']
                if r[0] == en and r[1] is not None and overlaps(tuple(r[1:3]), tuple(r[3:5]), p1, p2)]
        if not hits:
            continue
        start, end = min(hits)[0], max(h[1] for h in hits)
        broad = all(s[1] == 1 and t[1] == END for s, t in hits)
        shift = PSALM_TITLE_SHIFT.get(start[0], 0) if en == 'Psalm' and not broad else 0
        start, end = (start[0], start[1] + shift), (end[0], end[1] + shift if end[1] != END else END)
        (chapter_level if broad else verse_level).append((start, e['code'], e, fr_ref(en, start, end)))
    chosen = verse_level or chapter_level
    return [{'code': c, 'title': e['title'], 'passage': p, 'url': f'https://www.gty.org/sermons/{c}'}
            for _, c, e, p in sorted(chosen, key=lambda x: (x[0], x[1]))]


def jma_notes(d, passage=None):
    """Amorces des notes de la Bible d'étude qui couvrent la péricope : ['1.1', '1.2', '1.9-10', ...]."""
    folder = os.path.basename(os.path.dirname(d))
    fr, en, abbr = BOOKS[folder]
    path = os.path.join(SOURCES, folder, f'JMA - {folder.split(" - ", 1)[1]}.md')
    with open(path, encoding='utf-8') as f:
        notes = f.read().partition('## Notes verset par verset')[2]
    _, p1, p2 = parse_passage(passage or pages.load(d)['passage'])
    single = en in SINGLE
    found = []
    for m in re.finditer(r'^\*\*(\d+)(?:\.(\d+))?(?:[-–](?:(\d+)\.)?(\d+))?', notes, re.M):
        a, b, c, e = m.groups()
        if single and b is None:
            s, t = (1, int(a)), (1, int(e or a))
        elif b is None:
            continue
        else:
            s = (int(a), int(b))
            t = (int(c or a), int(e or b))
        if overlaps(s, t, p1, p2):
            label = f'{s[0]}.{s[1]}' + ('' if t == s else (f'-{t[1]}' if t[0] == s[0] else f'-{t[0]}.{t[1]}'))
            if label not in found:
                found.append(label)
    return found


def level_html(d, sermons, notes):
    fr, en, abbr = book_of(d)
    passage = pages.load(d)['passage']
    note_txt = (f'notes de <i>La Bible d\'étude MacArthur</i> sur {abbr} {", ".join(notes)}' if notes
                else 'aucune note de <i>La Bible d\'étude MacArthur</i> sur ce passage')
    if sermons:
        lead = f'Niveau 1, sermons Grace to You sur {passage} (tableau ci-dessous) ; {note_txt}.'
    elif notes:
        lead = f'Niveau 3, {note_txt}. Aucun sermon Grace to You n\'expose {passage}.'
    else:
        lead = f'Niveau ∅, aucune exposition de John MacArthur trouvée sur {passage}.'
    out = [f'    <p class="lead"><b>Niveau de source :</b> {lead}</p>']
    if sermons:
        out += ['    <div class="table-wrap">', '      <table class="mots">', '        <thead>',
                '          <tr><th scope="col">Code</th><th scope="col">Sermon</th><th scope="col">Passage</th></tr>',
                '        </thead>', '        <tbody>']
        for s in sermons:
            title = s['title'].replace('&', '&amp;').replace('<', '&lt;')
            out += ['          <tr>', f'            <th scope="row"><span class="mot-fr">{s["code"]}</span></th>',
                    f'            <td><a href="{s["url"]}" target="_blank" rel="noopener">{title}</a></td>',
                    f'            <td>{s["passage"]}</td>', '          </tr>']
        out += ['        </tbody>', '      </table>', '    </div>']
    return '\n'.join(out) + '\n'


def inject(page_html, block):
    """Remplace (ou pose) le bloc de niveau de source en tête de #commentateurs."""
    m = re.search(r'(<article class="section[^"]*" id="commentateurs">.*?</header>\n)', page_html, re.S)
    if not m:
        raise ValueError('#commentateurs introuvable')
    rest = page_html[m.end():]
    rest = re.sub(r'^    <p class="lead"><b>Niveau de source :</b>.*?</p>\n'
                  r'(?:    <div class="table-wrap">.*?\n    </div>\n)?', '', rest, count=1, flags=re.S)
    return page_html[:m.end()] + block + rest


def _selftest():
    assert parse_scripture('Matthew 26:57, 59–61; 1 Corinthians 7:1–7') == [
        ('Matthew', (26, 57), (26, 57)), ('Matthew', (26, 59), (26, 61)), ('1 Corinthians', (7, 1), (7, 7))]
    assert parse_scripture('Jude 14–16') == [('Jude', (1, 14), (1, 16))]
    assert parse_scripture('Romans 9–11') == [('Romans', (9, 1), (11, END))]
    assert parse_scripture('Matthew') == [('Matthew', None, None)]
    assert parse_scripture('Romans 3: 21–31') == [('Romans', (3, 21), (3, 31))]
    assert parse_scripture('1 John 3:11 – 18') == [('1 John', (3, 11), (3, 18))]
    assert parse_scripture('1 Peter 2:13a–b') == [('1 Peter', (2, 13), (2, 13))]
    assert parse_scripture('1 Corinthians 13:4d–5c') == [('1 Corinthians', (13, 4), (13, 5))]
    assert parse_scripture('1 Corinthians 10 and 11') == [('1 Corinthians', (10, 1), (10, END)),
                                                          ('1 Corinthians', (11, 1), (11, END))]
    assert parse_scripture('1 Corinthians 13:4d–5c') == [('1 Corinthians', (13, 4), (13, 5))]
    assert parse_scripture('1 Corinthians 10 and 11') == [('1 Corinthians', (10, 1), (10, END)), ('1 Corinthians', (11, 1), (11, END))]
    assert parse_scripture('Genesis 1:26–2:3') == [('Genesis', (1, 26), (2, 3))]
    assert parse_scripture('Matthew 13:3a, 10–17') == [('Matthew', (13, 3), (13, 3)), ('Matthew', (13, 10), (13, 17))]
    assert parse_passage('Genèse 1.3-2.3') == ('Genèse', (1, 3), (2, 3))
    assert parse_passage('Jacques 1.12') == ('Jacques', (1, 12), (1, 12))
    assert parse_passage('Actes 21.37 à 22.21') == ('Actes', (21, 37), (22, 21))
    assert parse_passage('1 Corinthiens 6.1-8') == ('1 Corinthiens', (6, 1), (6, 8))
    assert to_english('Psalm', (19, 8), (19, 15)) == ((19, 7), (19, 14))
    assert to_english('Psalm', (119, 1), (119, 8)) == ((119, 1), (119, 8))
    assert overlaps((1, 1), (1, 12), (1, 12), (1, 20)) and not overlaps((1, 1), (1, 11), (1, 12), (1, 20))
    assert fr_ref('James', (1, 1), (1, END)) == 'Jacques 1'
    html = '<article class="section reveal" id="commentateurs">\n    <header>h</header>\n    <p class="lead">x</p>'
    b = '    <p class="lead"><b>Niveau de source :</b> Niveau 3, a.</p>\n'
    once = inject(html, b)
    assert inject(once, b) == once and once.count('Niveau de source') == 1
    print('selftest OK')


def main(argv):
    sys.stdout.reconfigure(encoding='utf-8')
    if argv[:1] == ['--selftest']:
        return _selftest()
    cmd, args = argv[0], argv[1:]
    if cmd == 'index':
        with open(args[0], encoding='utf-8') as f:
            idx = build_index(json.load(f))
        with open(INDEX, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(idx, f, ensure_ascii=False, indent=0)
        print(len(idx), 'sermons indexés')
        return
    targets = [os.path.abspath(a) for a in args]
    dirs = [d for d in pages.pericope_dirs()
            if not targets or any(d == t or d.startswith(t + os.sep) for t in targets)]
    index = load_index()
    for d in dirs:
        sermons, notes = sermons_for(d, index), jma_notes(d)
        if cmd == 'match':
            print(f'{pages.load(d)["passage"]} | {len(sermons)} sermon(s) : '
                  + ', '.join(f'{s["code"]} ({s["passage"]})' for s in sermons) + f' | notes : {", ".join(notes)}')
        elif cmd == 'inject':
            p = os.path.join(d, 'index.html')
            with open(p, encoding='utf-8') as f:
                s = f.read()
            new = inject(s, level_html(d, sermons, notes))
            if new != s:
                with open(p, 'w', encoding='utf-8', newline='') as f:
                    f.write(new)


if __name__ == '__main__':
    main(sys.argv[1:])
