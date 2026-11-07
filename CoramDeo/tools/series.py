# -*- coding: utf-8 -*-
"""Plans de série : Serie.json est la source, Serie.md et Serie.pdf en sont dérivés (lot 8).

    python tools/series.py convert [dossier de livre ...]   ancien Serie.md -> Serie.json (une fois)
    python tools/series.py [dossier de livre ...]           Serie.json -> Serie.md + Serie.pdf

La conversion reprend le texte existant tel quel, retire les sections que le skill sermon-series
interdit (propositions de titre et slogans, arc narratif, fil conducteur, recommandation de
lancement) et calcule depuis tools/gty-index.json le niveau de source et la colonne Source.
La base du découpage et les textes exigeants sont à rédiger dans Serie.json, puis à régénérer.
"""
import glob
import importlib.util
import json
import os
import re
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages  # noqa: E402
import sources  # noqa: E402

GEN = os.path.join(pages.ROOT, '.claude', 'skills', 'sermon-series', 'assets', 'generate-pdf.py')


def book_dirs():
    return sorted(d for d in glob.glob(os.path.join(pages.CORPUS, '[0-9][0-9] - *'))
                  if os.path.isfile(os.path.join(d, '00 - Introduction', 'Serie.md')))


def _section(md, title):
    m = re.search(r'^## ' + re.escape(title) + r'\n(.*?)(?=^## |\Z)', md, re.M | re.S)
    return m.group(1).strip() if m else ''


def _bold_block(text, label):
    m = re.search(r'^\*\*' + re.escape(label) + r'\*\*\n\n(.*?)(?=^\*\*[^*\n]+\*\*$|\Z)', text, re.M | re.S)
    return m.group(1).strip() if m else ''


def _cells(row):
    return [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', row.strip().strip('|'))]


def convert_md(md, book_dir, index):
    head = md.splitlines()[0]
    title = head.split(' : ', 1)[1] if ' : ' in head else head
    folder = os.path.basename(book_dir)
    fr_book = sources.BOOKS[folder][0]
    parts = title.split(' : ')
    if parts[0] == folder.split(' - ', 1)[1]:  # « Luc : venu sauver les perdus : slogan »
        parts = parts[1:]
    meta = [m.strip('* ') for m in md.splitlines()[2].split('·')]
    units = []
    for row in _section(md, 'Plan semaine par semaine').splitlines()[2:]:
        c = _cells(row)
        if len(c) >= 4 and c[0].isdigit():
            units.append({'unit': c[0], 'passage': c[2], 'unit_basis': '', 'exposition_title': c[1],
                          'main_point': c[3], 'macarthur_source': ''})
    notes = _section(md, 'Notes pratiques')
    data = {
        'book': folder.split(' - ', 1)[1],
        'series_title': parts[0].strip(),
        'date': meta[0],
        'pastor_name': meta[1] if len(meta) > 1 else '',
        'source_level': '',
        'book_survey': _section(md, 'Évaluation de la portée'),
        'pericope_division': units,
        'difficult_texts': [],
        'preaching_notes': {'cadence': _bold_block(notes, 'Vérification de la durée'),
                            'unit_sizing': _bold_block(notes, 'Semaines à traiter avec soin'),
                            'gaps': ''},
    }
    enrich(data, book_dir, index, fr_book)
    return data


def enrich(data, book_dir, index, fr_book=None):
    """Colonne Source, niveau de source et lacunes, recalculés depuis l'index (jamais écrits à la main)."""
    fr_book = fr_book or sources.BOOKS[os.path.basename(book_dir)][0]
    probe = os.path.join(book_dir, 'x')
    missing = []
    for u in data['pericope_division']:
        passage = u['passage'] if u['passage'].startswith(fr_book) else f'{fr_book} {u["passage"]}'
        codes = [s['code'] for s in sources.sermons_for(probe, index, passage)]
        u['macarthur_source'] = ('GTY ' + ', '.join(codes)) if codes else 'Notes de la Bible d\'étude'
        if u.get('source_override'):  # jugement documenté (sermon thématique, index incomplet) : prime sur le calcul
            u['macarthur_source'] = u['source_override']
            codes = [] if u['source_override'].startswith('Aucune') else codes or ['override']
        if not codes:
            missing.append(u['passage'])
    n, total = len(data['pericope_division']) - len(missing), len(data['pericope_division'])
    if n:
        data['source_level'] = (f'Niveau 1 pour {n} unités sur {total}, sermons Grace to You (codes dans la colonne '
                                f'Source, tirés de l\'archive par Écriture)'
                                + (' ; notes de La Bible d\'étude MacArthur pour les autres.' if missing else '.'))
    else:
        data['source_level'] = ('Niveau 3, notes de La Bible d\'étude MacArthur ; aucune exposition de ce texte '
                                'dans l\'archive Grace to You.')
    data['preaching_notes']['gaps'] = (
        'Unités sans sermon Grace to You : ' + ', '.join(missing) + '. Leur exposition repose sur les notes de '
        'la Bible d\'étude, position condensée : suffisante pour trancher, insuffisante pour nuancer.'
        if missing and n else '')


def write_json(path, data):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def generate(book_dir, gen, index):
    intro = os.path.join(book_dir, '00 - Introduction')
    path = os.path.join(intro, 'Serie.json')
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    enrich(data, book_dir, index)
    data.pop('source_hash', None)
    write_json(path, data)
    data['source_hash'] = pages.source_hash(data)
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as tmp:
        json.dump(data, tmp, ensure_ascii=False)
    try:
        gen.generate_pdf(tmp.name, os.path.join(intro, 'Serie.pdf'))
    finally:
        os.unlink(tmp.name)


def main(argv):
    sys.stdout.reconfigure(encoding='utf-8')
    convert = argv[:1] == ['convert']
    targets = [os.path.abspath(a) for a in (argv[1:] if convert else argv)]
    dirs = [d for d in book_dirs() if not targets or d in targets]
    if convert:
        index = sources.load_index()
        for d in dirs:
            intro = os.path.join(d, '00 - Introduction')
            with open(os.path.join(intro, 'Serie.md'), encoding='utf-8') as f:
                data = convert_md(f.read(), d, index)
            write_json(os.path.join(intro, 'Serie.json'), data)
            print(os.path.basename(d), len(data['pericope_division']), 'unités')
        return
    from reportlab import rl_config
    rl_config.invariant = 1
    spec = importlib.util.spec_from_file_location('series_gen', GEN)
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    index = sources.load_index()
    for d in dirs:
        generate(d, gen, index)
    print(len(dirs), 'plans de série régénérés')


if __name__ == '__main__':
    main(sys.argv[1:])
