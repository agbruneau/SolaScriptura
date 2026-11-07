# -*- coding: utf-8 -*-
"""Régénère les dérivés d'une péricope depuis son index.html (décision D2 : HTML canonique).

    python tools/regen.py [--only-md] [--footers] [dossier ...]

Sans dossier : tout le corpus. Chaque péricope reçoit son .md et son .pdf,
produits par le générateur du skill sermon-research avec le `source_hash` du HTML.
--only-md  : saute le PDF (passe rapide ; check.py signalera les PDF périmés).
--footers  : réécrit seulement la ligne de déclaration dans le pied des 925 pages.
--intros   : recherches globales (00 - Introduction/Recherche.md, source) vers leur .pdf.

Le pied de chaque page porte la déclaration d'usage de l'IA et, pour une péricope,
l'état de la vérification d'attribution lu dans tools/couverture.json. Corriger le
contenu dans le HTML, jamais dans le .md ni le .pdf.
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

GEN = os.path.join(pages.ROOT, '.claude', 'skills', 'sermon-research', 'assets', 'generate-pdf.py')
COUVERTURE = os.path.join(pages.ROOT, 'tools', 'couverture.json')
IA = ("Texte produit avec l'assistance de l'IA générative (Claude, Anthropic) "
      "sous la direction d'André-Guy Bruneau · méthode : README du dépôt")


def generator():
    from reportlab import rl_config
    rl_config.invariant = 1  # PDF identique octet pour octet si le contenu ne change pas : pas de churn Git
    spec = importlib.util.spec_from_file_location('generate_pdf', GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rel(path):
    return os.path.relpath(path, pages.ROOT).replace(os.sep, '/')


def couverture():
    with open(COUVERTURE, encoding='utf-8') as f:
        return json.load(f)


def footer_line(page_dir, cov, pericopes):
    """Texte de la ligne de déclaration pour la page du dossier donné (chemin relatif)."""
    if page_dir not in pericopes:
        return IA
    date = cov.get(page_dir)
    return IA + (f' · Attribution à John MacArthur vérifiée le {date}' if date
                 else ' · Attribution à John MacArthur non vérifiée')


def stamp_footer(page_html, line):
    """Pose (ou remplace) la ligne de déclaration juste avant les boutons de retour du pied."""
    tag = f'  <p class="footer__line footer__ia">{line}</p>\n'
    s = re.sub(r'  <p class="footer__line footer__ia">.*?</p>\n', '', page_html)
    anchor = re.search(r'  <p class="footer__(?:retour|sdg)"', s)
    if not anchor:
        raise ValueError('pied sans footer__retour ni footer__sdg')
    return s[:anchor.start()] + tag + s[anchor.start():]


def stamp_all(cov, targets=()):
    pericopes = {rel(d) for d in pages.pericope_dirs()}
    changed = 0
    for p in sorted(glob.glob(os.path.join(pages.ROOT, '**', 'index.html'), recursive=True)):
        if os.sep + '.claude' + os.sep in p:
            continue
        if targets and not any(p.startswith(t + os.sep) for t in targets):
            continue
        with open(p, encoding='utf-8') as f:  # fins de ligne normalisées en LF (core.autocrlf s'en charge)
            s = f.read()
        new = stamp_footer(s, footer_line(rel(os.path.dirname(p)), cov, pericopes))
        if new != s:
            with open(p, 'w', encoding='utf-8', newline='') as f:
                f.write(new)
            changed += 1
    return changed


def regen(d, gen, only_md=False):
    data = pages.load(d)
    data['source_hash'] = pages.source_hash(data)
    md = pages.research_md(d)
    if only_md:
        gen.generate_markdown(data, md)
        return
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as tmp:
        json.dump(data, tmp, ensure_ascii=False)
    try:
        gen.generate_pdf(tmp.name, os.path.splitext(md)[0] + '.pdf')
    finally:
        os.unlink(tmp.name)


def regen_intro(book_dir, gen, index):
    """Recherche globale d'un livre : le .md est la source ; niveau de source posé s'il manque."""
    import sources
    md = os.path.join(book_dir, '00 - Introduction', 'Recherche.md')
    with open(md, encoding='utf-8') as f:
        data = pages.parse_md(f.read())
    if not data.get('source_level'):
        fr, en, _ = sources.BOOKS[os.path.basename(book_dir)]
        n = sum(1 for e in index if any(r[0] == en for r in e['refs']))
        data['source_level'] = (
            f"Niveau 1, sermons Grace to You sur {data['passage']} ({n} sermons dans l'archive par Écriture, "
            "voir la page de chaque péricope) ; introduction et notes de La Bible d'étude MacArthur." if n and en != 'Psalm'
            else "Niveau 3, introduction et notes de La Bible d'étude MacArthur.")
    data['source_hash'] = pages.source_hash(data)
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as tmp:
        json.dump(data, tmp, ensure_ascii=False)
    try:
        gen.generate_pdf(tmp.name, os.path.splitext(md)[0] + '.pdf')
    finally:
        os.unlink(tmp.name)


def main(argv):
    sys.stdout.reconfigure(encoding='utf-8')
    unknown = [a for a in argv if a.startswith('-') and a not in ('--only-md', '--footers', '--intros')]
    if unknown:
        sys.exit(f'option inconnue : {" ".join(unknown)}\n{__doc__}')
    only_md = '--only-md' in argv
    if '--footers' in argv:
        targets = [os.path.abspath(a) for a in argv if not a.startswith('--')]
        print(f'{stamp_all(couverture(), targets)} pages : ligne de déclaration posée ou mise à jour')
        return 0
    if '--intros' in argv:
        import sources
        targets = [os.path.abspath(a) for a in argv if not a.startswith('--')]
        books = sorted(d for d in glob.glob(os.path.join(pages.CORPUS, '[0-9][0-9] - *'))
                       if os.path.isfile(os.path.join(d, '00 - Introduction', 'Recherche.md'))
                       and (not targets or d in targets))
        gen, index = generator(), sources.load_index()
        for d in books:
            regen_intro(d, gen, index)
        print(f'{len(books)} recherches globales régénérées')
        return 0
    targets = [os.path.abspath(a) for a in argv if not a.startswith('--')]
    dirs = [d for d in pages.pericope_dirs() if not targets or any(
        d == t or d.startswith(t + os.sep) for t in targets)]
    if not dirs:
        sys.exit('aucun dossier de péricope ne correspond')
    gen = generator()
    failures = []
    for i, d in enumerate(dirs, 1):
        try:
            regen(d, gen, only_md)
        except Exception as e:  # une page cassée ne doit pas arrêter le lot : on la rapporte
            failures.append((rel(d), repr(e)))
        if i % 50 == 0:
            print(f'{i}/{len(dirs)}', flush=True)
    print(f'{len(dirs) - len(failures)}/{len(dirs)} péricopes régénérées' + (' (.md seulement)' if only_md else ''))
    for f in failures:
        print('ÉCHEC', *f)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
