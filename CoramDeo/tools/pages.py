# -*- coding: utf-8 -*-
"""Lecture des pages de péricope : le HTML est la source canonique (décision D2).

    python tools/pages.py <dossier de péricope>     affiche le JSON extrait
    python tools/pages.py --selftest

Le JSON produit suit la structure du skill sermon-research ; `generate-pdf.py`
en tire le .md et le .pdf. `source_hash` résume ce JSON : il est écrit dans le .md
et dans les métadonnées du .pdf, et check.py le compare pour détecter un dérivé périmé.
"""
import glob
import hashlib
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, '3 - Pérégrination')
MOIS = {m: i for i, m in enumerate(
    'janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split(), 1)}


def pericope_dirs():
    """Les 886 dossiers de péricope, triés."""
    return sorted(d for d in glob.glob(os.path.join(CORPUS, '[0-9][0-9] - *', '[0-9]*'))
                  if os.path.isdir(d) and not os.path.basename(d).startswith('00 - '))


def research_md(d):
    found = glob.glob(os.path.join(d, 'Recherche-*.md'))
    if len(found) != 1:
        raise ValueError(f'{d}: {len(found)} fichiers Recherche-*.md')
    return found[0]


def text(fragment):
    """HTML en ligne vers texte brut (espaces insécables conservés)."""
    t = re.sub(r'<br\s*/?>', ' ', fragment)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'[ \t\r\n]+', ' ', html.unescape(t)).strip()


def _one(pattern, s, what):
    m = re.search(pattern, s, re.S)
    if not m:
        raise ValueError(f'élément introuvable : {what}')
    return m.group(1)


def _section(s, sid):
    body = _one(r'<article class="section[^"]*" id="%s">(.*?)\n  </article>' % sid, s, '#' + sid)
    return re.sub(r'<header class="sec-head">.*?</header>', '', body, count=1, flags=re.S)


def _prose(body):
    """Paragraphes d'une section de prose, dans l'ordre : lead, body, p, points.

    Les versets affichés (div.verses) sont une illustration de mise en page : exclus.
    Le bloc « Niveau de source » et son tableau de sermons sont lus à part.
    """
    body = re.sub(r'<div class="verses">.*?\n    </div>', '', body, flags=re.S)
    body = re.sub(r'<p class="lead"><b>Niveau de source :</b>.*?</p>', '', body, flags=re.S)
    body = re.sub(r'<div class="table-wrap">.*?</div>', '', body, flags=re.S)
    paras = []
    for m in re.finditer(r'<p(?: class="lead")?>(.*?)</p>|<li>(.*?)</li>', body, re.S):
        t = text(m.group(1) if m.group(1) is not None else m.group(2))
        if t:
            paras.append(t)
    return '\n\n'.join(paras)


def _date(meta):
    m = re.search(r'(\d{4}-\d{2}-\d{2})', meta)
    if m:
        return m.group(1)
    m = re.search(r'(\d{1,2}) (\w+) (\d{4})', meta)
    if m and m.group(2) in MOIS:
        return f'{m.group(3)}-{MOIS[m.group(2)]:02d}-{int(m.group(1)):02d}'
    raise ValueError(f'date illisible : {meta!r}')


def extract(page_html):
    s = page_html
    meta = text(_one(r'<p class="hero__meta">(.*?)</p>', s, 'hero__meta'))
    parts = [p.strip() for p in meta.split('·')]
    data = {
        'passage': text(_one(r'<p class="hero__kicker">Recherche · (.*?)</p>', s, 'hero__kicker')),
        'date': _date(meta),
        'pastor_name': parts[-2],
        'church_name': parts[-1],
    }
    comm = _section(s, 'commentateurs')
    m = re.search(r'<p class="lead"><b>Niveau de source :</b>(.*?)</p>', comm, re.S)
    if m:
        data['source_level'] = text(m.group(1))
    links = []
    table = re.search(r'<div class="table-wrap">.*?</div>', comm, re.S)
    for row in re.findall(r'<tr>\s*<th scope="row"><span class="mot-fr">[^<]*</span></th>(.*?)</tr>',
                          table.group(0) if table else '', re.S):
        cells = re.findall(r'<td>(.*?)</td>', row, re.S)
        url = re.search(r'href="([^"]+)"', cells[0])
        links.append({'title': text(cells[0]), 'passage': text(cells[1]), 'url': url.group(1) if url else ''})
    if links:
        data['sermon_links'] = links
    data['passage_context'] = _prose(_section(s, 'contexte'))
    data['historical_background'] = _prose(_section(s, 'arriere-plan'))
    words = []
    for row in re.findall(r'<tr>\s*(<th scope="row"><span class="mot-fr">.*?)</tr>', _section(s, 'mots-cles'), re.S):
        tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
        words.append({
            'english': text(_one(r'<span class="mot-fr">(.*?)</span>', row, 'mot-fr')),
            'transliteration': text(_one(r'<span class="mot-gr">(.*?)</span>', row, 'mot-gr')),
            'literal_meaning': text(tds[0]),
            'range_of_meaning': text(tds[1]),
            'translations': {text(k): text(v) for k, v in
                             re.findall(r'<span><b>(.*?)</b>(.*?)</span>', tds[2], re.S)},
        })
    data['word_studies'] = words
    data['commentary_insights'] = _prose(comm)
    data['cross_references'] = [
        {'reference': text(r), 'connection': text(c), 'type': text(t)}
        for r, t, c in re.findall(
            r'<span class="renvoi__ref">(.*?)</span><span class="renvoi__tag">(.*?)</span>.*?'
            r'<p class="renvoi__desc">(.*?)</p>', _section(s, 'renvois'), re.S)]
    themes = []
    for t in re.findall(r'<section class="theme"[^>]*>(.*?)</section>', _section(s, 'themes'), re.S):
        ps = re.findall(r'<p>(.*?)</p>', t, re.S)
        themes.append({'name': text(_one(r'<h3 class="theme__title">(.*?)</h3>', t, 'theme__title')),
                       'in_text': text(ps[0]), 'implication': text(ps[1])})
    data['theological_themes'] = themes
    data['thinking_prompts'] = [text(q) for q in re.findall(
        r'<li>(.*?)</li>', _one(r'<ol class="questions">(.*?)</ol>', _section(s, 'reflexion'), 'questions'), re.S)]
    data['key_verse'] = text(_one(r'<p class="hero__verse">(.*?)</p>', s, 'hero__verse'))
    return data


def _md_sections(md):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r'^## (.+?)\n(.*?)(?=^## |\Z)', md, re.M | re.S)}


def _md_cell(c):
    return c.strip().replace('\\|', '|').replace('\\\\', '\\')


def parse_md(md):
    """Recherche au format du générateur (.md) vers JSON : pour les recherches globales, dont le .md est la source."""
    md = re.sub(r'\n<!-- source_hash: \w+ -->\s*$', '\n', md)
    head, _, _ = md.partition('\n---\n')
    lines = head.strip().splitlines()
    meta = re.findall(r'\*\*(.+?)\*\*', lines[2]) if len(lines) > 2 else []
    data = {'passage': lines[0].split(' : ', 1)[1].strip(),
            'date': meta[0] if meta else '', 'pastor_name': meta[1] if len(meta) > 1 else '',
            'church_name': meta[2] if len(meta) > 2 else ''}
    sec = _md_sections(md)
    data['passage_context'] = sec.get('Contexte du passage', '')
    data['historical_background'] = sec.get('Arrière-plan historique et culturel', '')
    words = []
    for row in sec.get('Étude des mots-clés', '').splitlines()[2:]:
        c = [_md_cell(x) for x in re.split(r'(?<!\\)\|', row.strip()[1:-1])]
        words.append({'english': c[0].strip('*'), 'transliteration': c[1].strip('_'), 'literal_meaning': c[2],
                      'range_of_meaning': c[3],
                      'translations': dict(re.findall(r'_(.+?)_ (.*?)(?= · _|$)', c[4]))})
    data['word_studies'] = words
    comm = sec.get('Apports des commentateurs', '')
    m = re.match(r'\*\*Niveau de source\*\*\n\n(.*?)(?:\n\n|$)', comm, re.S)
    if m:
        level = m.group(1).strip()
        if not level.startswith('Non déclaré.'):
            data['source_level'] = level
        comm = comm[m.end():]
    m = re.match(r'\*\*Sermons Grace to You\*\*\n\n((?:\|.*\n?)+)', comm)
    if m:
        links = []
        for row in m.group(1).strip().splitlines()[2:]:
            c = [_md_cell(x) for x in re.split(r'(?<!\\)\|', row.strip()[1:-1])]
            t = re.fullmatch(r'\[(.*)\]\((.*)\)', c[1])
            links.append({'title': t.group(1) if t else c[1], 'passage': c[2], 'url': t.group(2) if t else ''})
        data['sermon_links'] = links
        comm = comm[m.end():]
    data['commentary_insights'] = comm.strip()
    refs = []
    for m in re.finditer(r'^\*\*(.+?)\*\*(?: · _(.+?)_)?\n(?:\n(?!\*\*)(.+?))?(?=\n\n\*\*|\Z)',
                         sec.get('Renvois et passages parallèles', ''), re.M | re.S):
        refs.append({'reference': m.group(1), 'connection': (m.group(3) or '').strip(), 'type': m.group(2) or ''})
    data['cross_references'] = refs
    themes = []
    for m in re.finditer(r'^### (.+?)\n(.*?)(?=^### |\Z)', sec.get('Thèmes théologiques', ''), re.M | re.S):
        body = m.group(2)
        it = re.search(r'\*\*Dans le texte\*\*\n\n(.*?)(?=\n\n\*\*Pour votre assemblée\*\*|\Z)', body, re.S)
        im = re.search(r'\*\*Pour votre assemblée\*\*\n\n(.*)', body, re.S)
        themes.append({'name': m.group(1).strip(), 'in_text': it.group(1).strip() if it else '',
                       'implication': im.group(1).strip() if im else ''})
    data['theological_themes'] = themes
    data['thinking_prompts'] = re.findall(r'^\d+\. (.+)$', sec.get('Pistes de réflexion', ''), re.M)
    return data


def source_hash(data):
    payload = json.dumps({k: v for k, v in data.items() if k != 'source_hash'},
                         ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(payload.encode('utf-8')).hexdigest()[:16]


def load(d):
    with open(os.path.join(d, 'index.html'), encoding='utf-8') as f:
        return extract(f.read())


def _selftest():
    jac = next(d for d in pericope_dirs() if 'Jacques 1.1-12' in d)
    data = load(jac)
    assert data['passage'] == 'Jacques 1.1-12', data['passage']
    assert data['date'] == '2026-06-06' and data['pastor_name'] == 'AGB'
    assert len(data['word_studies']) == 5 and data['word_studies'][0]['translations']['Darby'] == 'tentations'
    assert len(data['cross_references']) == 8 and data['cross_references'][0]['type'] == 'Parallèle direct'
    assert len(data['theological_themes']) == 5 and len(data['thinking_prompts']) == 7
    assert data['passage_context'].count('\n\n') == 3, 'lead + 3 paragraphes'
    assert 'Heureux l' not in data['passage_context'], 'versets affichés exclus'
    assert "L'épreuve de l'or." in data['historical_background'], 'points conservés'
    assert data['source_level'].startswith('Niveau 1, sermons Grace to You'), data.get('source_level')
    assert data['sermon_links'][0]['url'] == 'https://www.gty.org/sermons/59-1'
    assert 'Niveau de source' not in data['commentary_insights'] and 'Purpose of Trials' not in data['commentary_insights']
    assert data['commentary_insights'].startswith('La question interprétative centrale')
    assert source_hash(data) == source_hash(dict(data, source_hash='x'))
    print('selftest OK')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:] == ['--selftest']:
        _selftest()
    elif len(sys.argv) == 2:
        print(json.dumps(load(sys.argv[1]), ensure_ascii=False, indent=2))
    else:
        sys.exit(__doc__)
