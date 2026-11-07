# Sola Scriptura

Ressources d'étude biblique et de préparation de prédication expositive d'André-Guy Bruneau, dans
un cadre baptiste réformé conforme à la théologie de John MacArthur, sur le texte de la Nouvelle
Édition de Genève 1979 (NEG79).

| Projet | Contenu | Point d'entrée |
|---|---|---|
| [`CoramDeo/`](CoramDeo) | Ressource de l'Église Baptiste de Charlesbourg (Québec) en trois volets : **Vision** (4 traités de doctrine), **Mission** (4 pages sur la vie de l'homme racheté) et **Pérégrination** (886 péricopes en exposition suivie : le Nouveau Testament au complet, 27 livres et 848 péricopes, et 38 péricopes de l'Ancien Testament en trois séries : Genèse 1-11, Psaume 19, Psaume 119). | [`CoramDeo/index.html`](CoramDeo/index.html) |
| [`Paulus/`](Paulus) | Les épîtres de Paul, et Hébreux, dans l'ordre chronologique de rédaction selon MacArthur (14 livres, de Galates à Hébreux) : pour chaque livre, une recherche globale, une recherche par chapitre (100 au total), un plan de série à raison d'un sermon par chapitre et un portail HTML. S'y ajoutent deux synthèses sur la vie de l'apôtre. | [`Paulus/README.md`](Paulus/README.md), puis `index.html` de chaque livre |

Le détail de chaque projet (méthode, sources, conventions, couverture, audits) se trouve dans son
propre README : [`CoramDeo/README.md`](CoramDeo/README.md) et [`Paulus/README.md`](Paulus/README.md).
Les conventions de production de Paulus sont dans [`Paulus/AGENTS.md`](Paulus/AGENTS.md).

## Structure

```
SolaScriptura/
├── README.md
├── .gitattributes            PDF et images traités en binaire
├── CoramDeo/
│   ├── index.html            index de navigation
│   ├── 1 - Vision/           bibliologie, christologie, pneumatologie, ecclésiologie
│   ├── 2 - Mission/          Trinité, autrui, travail, héritage
│   ├── 3 - Pérégrination/    avant-propos, puis un dossier par livre (01 - Genèse … 66 - Apocalypse)
│   ├── tools/                génération et contrôle (Python)
│   ├── .claude/skills/       skills sermon-research et sermon-series
│   └── LICENSE
└── Paulus/
    ├── 01 - Galates/ … 14 - Hébreux/
    │   ├── index.html        portail de l'étude
    │   ├── Plan-Serie-*.md   plan de série (et PDF)
    │   ├── Sommaire/         recherche sur le livre entier
    │   └── NN-<Livre>-N/     une recherche par chapitre (MD, HTML, PDF, JSON)
    ├── Apôtre Paul - Histoire.pdf
    ├── Apôtre Paul - Présentation.pdf
    └── .agents/skills/etude-livre/
```

## Consultation

Les pages sont des fichiers HTML autonomes : il suffit d'ouvrir un `index.html` dans un navigateur,
sans serveur ni installation. Les recherches existent aussi en Markdown, lisible directement sur
GitHub, et en PDF pour l'impression.

## Production et contrôle

Les recherches et les pages ont été produites avec Claude Code (Anthropic) à partir de skills
versionnés (`CoramDeo/.claude/skills/`, `Paulus/.agents/skills/etude-livre/`), sous la direction
de l'auteur, qui en a fixé le cadre théologique, les sources autorisées et les règles de
vérification. La portée des relectures et des audits est documentée dans chaque projet.

Le dépôt n'a pas d'intégration continue. Les contrôles de CoramDeo se lancent localement, depuis
`CoramDeo/`, avec Python 3 (et `reportlab` pour régénérer les PDF) :

```bash
python tools/pages.py --selftest
python tools/check.py
```

## Origine

Les deux dossiers ont été intégrés en entier le 7 novembre 2026, à partir des dépôts
[agbruneau/CoramDeo](https://github.com/agbruneau/CoramDeo) et
[agbruneau/Paulus](https://github.com/agbruneau/Paulus), où leur historique antérieur est conservé.
Ils sont désormais maintenus ici.

Les `.gitignore` de chaque dossier continuent de s'appliquer. Les sources protégées de CoramDeo
(textes sous licence d'usage personnel) restent hors dépôt.

## Licences

- **CoramDeo** : contenu sous CC BY-NC-ND 4.0, code (`tools/`, `.claude/`, `*.py`) sous MIT. La
  confession de foi de l'Église, les logos et les citations bibliques en sont exclus. Voir
  [`CoramDeo/LICENSE`](CoramDeo/LICENSE).
- **Paulus** : aucun fichier de licence.
