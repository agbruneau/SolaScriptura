# -*- coding: utf-8 -*-
"""Dossier de vérification d'attribution d'une péricope (lot 7).

    python tools/attributions.py <dossier> [...]

Imprime, pour chaque péricope : les phrases qui nomment MacArthur (avec leur section), les
transcriptions locales des sermons retenus et le texte des notes de la Bible d'étude qui couvrent
le passage. Les sources vivent hors dépôt (CORAMDEO_SOURCES) : ce dossier ne s'écrit pas dans le dépôt.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages  # noqa: E402
import sources  # noqa: E402

SECTIONS = [('passage_context', 'contexte'), ('historical_background', 'arriere-plan'),
            ('word_studies', 'mots-cles'), ('commentary_insights', 'commentateurs'),
            ('cross_references', 'renvois'), ('theological_themes', 'themes'), ('thinking_prompts', 'reflexion')]


def flatten(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [t for v in value.values() for t in flatten(v)]
    return [t for v in value for t in flatten(v)]


def sentences_naming(data):
    out = []
    for key, sid in SECTIONS:
        for block in flatten(data.get(key, [])):
            for s in re.split(r'(?<=[.!?»])\s+(?=[A-ZÀ-ÖÉÈ«])', block):
                if re.search(r'MacArthur', s):
                    out.append((sid, s.strip()))
    return out


def note_texts(d, passage):
    folder = os.path.basename(os.path.dirname(d))
    path = os.path.join(sources.SOURCES, folder, f'JMA - {folder.split(" - ", 1)[1]}.md')
    with open(path, encoding='utf-8') as f:
        notes = f.read().partition('## Notes verset par verset')[2]
    wanted = set(sources.jma_notes(d, passage))
    kept, keep = [], False
    for para in notes.split('\n\n'):
        m = re.match(r'\*\*(\d+(?:\.\d+)?(?:[-–](?:\d+\.)?\d+)?)', para.strip())
        if m:
            head = m.group(1).replace('–', '-')
            single = '.' not in head.split('-')[0]
            label = f'1.{head}' if single and sources.book_of(d)[1] in sources.SINGLE else head
            keep = label in wanted or head in wanted
        # sous-note (« **lemme.** ») ou suite : rattachée à la dernière note numérotée
        if keep and para.strip():
            kept.append(para.strip())
    return path, kept


def dossier(d):
    data = pages.load(d)
    passage = data['passage']
    lines = [f'# {passage}', '', f'Page : {os.path.join(d, "index.html")}', '']
    lines += ['## Phrases qui nomment MacArthur', '']
    for i, (sid, s) in enumerate(sentences_naming(data), 1):
        lines.append(f'{i}. [#{sid}] {s}')
    lines += ['', '## Sermons Grace to You retenus (transcriptions locales)', '']
    for link in data.get('sermon_links', []):
        code = link['url'].rsplit('/', 1)[-1]
        path = os.path.join(sources.SOURCES, 'gty', f'{code}.txt')
        state = path if os.path.exists(path) else 'TRANSCRIPTION ABSENTE'
        lines.append(f'- {code} « {link["title"]} » ({link["passage"]}) : {state}')
    path, notes = note_texts(d, passage)
    lines += ['', f'## Notes de la Bible d\'étude couvrant le passage ({path})', ''] + notes
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    for arg in sys.argv[1:]:
        print(dossier(os.path.abspath(arg)))
