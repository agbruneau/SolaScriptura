# Coram Deo : Vision, Mission, Pérégrination

> Ressource d'étude biblique, de doctrine et de préparation de prédication pour l'**Église Baptiste
> de Charlesbourg** (Québec ; pasteur Simon Ouellette). Le **Nouveau Testament est couvert en
> entier** (27 livres), complété par des **séries de l'Ancien Testament** (Genèse 1-11, Psaume 19,
> Psaume 119), le tout dans un cadre baptiste réformé conforme à la théologie de John MacArthur.

Le dépôt est organisé en **trois volets**, qui vont du fondement doctrinal à la vie de l'homme
racheté, puis à l'exposition suivie des Écritures :

| Volet | Contenu | Pages |
|---|---|---|
| [`1 - Vision/`](<1 - Vision>) | Ce que nous croyons : bibliologie, christologie, pneumatologie, ecclésiologie | 4 |
| [`2 - Mission/`](<2 - Mission>) | Ce que devient l'homme racheté : Dieu, autrui, travail, héritage | 4 |
| [`3 - Pérégrination/`](<3 - Pérégrination>) | Les expositions suivies, livre par livre, et leurs fondations | 916 |

Un **index de navigation** [`index.html`](index.html) à la racine fédère l'ensemble.

---

## Méthode de production et usage de l'intelligence artificielle

Les recherches exégétiques, les plans de série et les pages de ce dépôt ont été produits entre mai
et septembre 2026 avec **Claude Code (Anthropic)**, à partir de deux gabarits de génération
versionnés dans [`.claude/skills/`](<.claude/skills>), sous la direction d'**André-Guy Bruneau**, qui
a fixé le cadre théologique, les sources autorisées, la structure des livrables et les règles de
vérification. Le texte biblique de référence est la Nouvelle Édition de Genève 1979 ; les positions
attribuées à John MacArthur proviennent de ses sermons Grace to You et des notes de *La Bible
d'étude MacArthur*, consultées localement sous licence d'usage personnel et non redistribuées.

Le contrôle humain a porté sur la conception, la relecture par sondage et un audit doctrinal dont
la portée exacte est donnée ci-dessous et dans [`gauntlet-log.md`](gauntlet-log.md). Les audits ont
eux-mêmes été conduits avec des agents d'IA (bâtisseurs, critiques et juges distincts), sous la
direction de l'auteur. **Chaque page de péricope dit dans son pied si l'attribution à MacArthur a
été vérifiée**, et à quelle date. Toute erreur d'attribution qui subsiste est de la responsabilité
de l'auteur, non de MacArthur.

Couverture de l'audit :

| Volet | Pages | Conformité doctrinale | Attribution vérifiée |
|---|---|---|---|
| Vision et Mission | 8 | 7 (gauntlet, août 2026 ; Bibliologie non auditée) | sans objet (sources systématiques) |
| Pérégrination, Genèse 1-11 | 12 péricopes et 1 introduction | 13 (gauntlet, août 2026) | 12 péricopes (246 attributions, 10 corrigées) et 1 introduction (sept. 2026) |
| Pérégrination, autres livres | 874 péricopes et 29 introductions | triage par signature seulement | 874 péricopes et 29 introductions (gauntlet, sept. 2026 ; juge à l'aveugle par groupe d'environ 12 pages) |

---

## `1 - Vision/` : les fondements doctrinaux

Quatre traités de théologie systématique, présentés comme des pages web autonomes, qui gouvernent
la lecture de tout le reste du dépôt. Source : MacArthur et Mayhue, *Théologie systématique*.

- **[`1 - Bibliologie/`](<1 - Vision/1 - Bibliologie>)** : la Parole de Dieu (inspiration, autorité,
  inerrance, préservation, enseignement et prédication, obligations envers l'Écriture).
- **[`2 - Christologie/`](<1 - Vision/2 - Christologie>)** : Dieu le Fils, en trois temps, le Christ
  **préincarné**, **incarné** et **glorifié** (intercession céleste, enlèvement, tribunal de Christ,
  règne millénaire, grand trône blanc, éternité future).
- **[`3 - Pneumatologie/`](<1 - Vision/3 - Pneumatologie>)** : Dieu le Saint-Esprit (divinité,
  salut, sanctification, service, création, Écriture, ministère prophétique).
- **[`4 - Ecclésiologie/`](<1 - Vision/4 - Ecclésiologie>)** : l'Église (définition, but, autorité
  spirituelle, vie d'assemblée, moyens de grâce, unité et pureté, membres, dons spirituels,
  avant-goût du ciel).

---

## `2 - Mission/` : l'homme racheté

Quatre pages qui suivent le plan de *The Redeemed Man* (Richard D. Phillips, dir.) : les intitulés
de chapitres sont ceux de l'ouvrage ; **l'exposition, elle, est rédigée sous la seule lentille de
John MacArthur**, conformément au cadre du dépôt (là où l'ouvrage source relèverait d'une autre
tradition, paedobaptisme ou amillénarisme, c'est la lecture de MacArthur qui tranche).

| Dossier | Page | Chapitres traités |
|---|---|---|
| [`1 - Trinité/`](<2 - Mission/1 - Trinité>) | Trinité | Se repentir et croire · Connaître son Dieu · S'attacher à la Parole · Croître en grâce |
| [`2 - Autrui/`](<2 - Mission/2 - Autrui>) | Autrui | Parents · Célibat · Épouse · Direction de la famille · Enfants · Culte familial · Amitiés · Témoignage |
| [`3 - Travail/`](<2 - Mission/3 - Travail>) | Travail | Regard sur le travail · Ardeur · Service dans l'Église · Ressources · Loisirs · Citoyenneté |
| [`4 - Héritage/`](<2 - Mission/4 - Héritage>) | Héritage | Santé · Persévérance · Retraite · Préparation à la mort |

Chaque page comporte un sommaire en cartes, un article détaillé par chapitre (ancres, tableaux de
synthèse, encadrés de mise en garde), une conclusion et un pied de page qui nomme la source.

*(Les tables des matières Markdown `Partie 1.md` à `Partie 4.md` et `Homme Racheté.md`, qui ont servi
de plan de travail, ont été retirées le 22 août 2026, commit `415e211`, une fois les pages
rédigées.)*

---

## `3 - Pérégrination/` : les expositions suivies

Le cœur du dépôt : le matériel produit pour des **expositions suivies** (*lectio continua*), livre
par livre. Pour chaque livre traité : un **plan de série de prédications**, une **recherche
exégétique** par péricope, une **recherche globale** d'introduction et une **page de présentation
web**.

Les livres sont rangés dans des dossiers numérotés selon l'ordre canonique des **66 livres de la
Bible protestante** : `01 - Genèse` à `66 - Apocalypse`. Le dossier `00 - Avant-propos/` réunit les
pièces fondatrices.

### `00 - Avant-propos/` : les fondations

#### Référence d'autorité doctrinale

*La Sainte Bible avec commentaires de John MacArthur* (Société Biblique de Genève), sur le texte
NEG 1979, est la **source qui tranche la conformité doctrinale** de tout le matériel produit. Elle
est sous droit d'auteur et n'est **pas versionnée** : l'auteur la consulte localement, sous licence
d'usage personnel, avec les fichiers de référence par livre qui en sont extraits (`NEG - <Livre>.md`
pour le texte biblique, `JMA - <Livre>.md` pour les notes d'étude). Ces fichiers vivent hors dépôt,
dans le dossier désigné par la variable d'environnement `CORAMDEO_SOURCES` (par défaut
`%USERPROFILE%\CoramDeo-sources`), sous la même arborescence de livres ; ils ont été retirés de
l'historique du dépôt le 15 septembre 2026.

#### Standards doctrinaux de l'Église

- **[`Confession de foi-EBC.pdf`](<3 - Pérégrination/00 - Avant-propos/Confession de foi-EBC.pdf>)** :
  la confession de foi de l'Église Baptiste de Charlesbourg (révisée en 2016) : autorité et
  inerrance des Écritures (66 livres), Trinité, création littérale en six jours, prémillénarisme
  prétribulationniste, retour imminent et corporel du Christ.

#### Ressources de discipulat et de piété

- **[`PrecisDicipulat.md`](<3 - Pérégrination/00 - Avant-propos/PrecisDicipulat.md>)** (et son
  `.pdf`) : un *Précis du discipulat chrétien*. Il pose que le discipulat **est** la vie chrétienne
  elle-même : fruit nécessaire de la régénération, suivre Christ comme Seigneur (*Lordship
  Salvation*), nourri par la Parole suffisante, vécu dans l'Église locale et transmis par le
  mentorat, en vue de la conformité à Christ.
- **[`PlanEvangélisation.md`](<3 - Pérégrination/00 - Avant-propos/PlanEvangélisation.md>)** (et son
  `.pdf`) : un essai sur *The Master Plan of Evangelism* de Robert E. Coleman (1963, rév. 1993) :
  les **huit principes** de la stratégie du Maître : sélection, association, consécration,
  impartation, démonstration, délégation, supervision, reproduction.
  ⚠ *Coleman écrit depuis la tradition wesleyenne de sainteté ; l'essai comporte une section
  « limites et points de vigilance » qui redresse notamment son vocabulaire pneumatologique (second
  baptême de l'Esprit) au regard du cadre du dépôt.*
- **[`Puritains/Guide Étude Biblique.md`](<3 - Pérégrination/00 - Avant-propos/Puritains/Guide Étude Biblique.md>)** :
  une méthode d'étude personnelle (lecture quotidienne, notes manuscrites en Bible à marges larges,
  archivage en Bible intercalaire, langues originales).
  ⚠ *Ce guide décrit une méthode de travail ; il ne fait autorité sur aucun point doctrinal.*

Le recueil *La Vallée de la Vision* (Publications Chrétiennes, 2023), son étude PowerPoint et les
documents puritains d'auteur non établi (essai, synthèse, présentation) ont été retirés du dépôt et
de son historique ; ils restent parmi les sources locales de l'auteur.

#### Outillage d'extraction

- **`extract_nt.py`** et **`extract_at.py`** : régénèrent les fichiers de référence
  `NEG - <Livre>.md` / `JMA - <Livre>.md` depuis le PDF de la Bible d'étude, dans
  `CORAMDEO_SOURCES` (séparation des flux texte biblique / notes d'étude par police et taille ;
  exigent PyMuPDF).
- **`md-to-pdf.py`** : rend un `.md` en PDF au style maison, noir et orange (exige reportlab).
  Usage : `python md-to-pdf.py <fichier.md> [sortie.pdf]`. Ce n'est **pas un parseur Markdown
  général** : il ne couvre que les constructions présentes dans `PrecisDicipulat.md` (`#`, `##`,
  `###`, citations `>`, listes `-`, tableaux `|`, `**`, `*`, plus `<!-- pagebreak -->` pour forcer
  un saut de page ; les filets `---` sont ignorés) et insère une signature datée sous le sous-titre,
  surchargeable par la variable d'environnement `MD2PDF_BYLINE`.

### Couverture biblique : 886 péricopes

#### Nouveau Testament : 27/27 livres complets (848 péricopes)

Pour chaque livre : une série figée, une recherche globale, une page d'accueil et **toutes les
péricopes** (page `index.html`, recherche `.md`, export `.pdf`), la réunion des péricopes
recomposant le livre de son premier à son dernier verset.

| # | Livre | Péricopes | # | Livre | Péricopes |
|---|---|---|---|---|---|
| 40 | Matthieu | 89 | 54 | 1 Timothée | 18 |
| 41 | Marc | 82 | 55 | 2 Timothée | 13 |
| 42 | Luc | 129 | 56 | Tite | 8 |
| 43 | Jean | 53 | 57 | Philémon | 4 |
| 44 | Actes | 77 | 58 | Hébreux | 39 |
| 45 | Romains | 47 | 59 | Jacques | 12 |
| 46 | 1 Corinthiens | 55 | 60 | 1 Pierre | 17 |
| 47 | 2 Corinthiens | 42 | 61 | 2 Pierre | 10 |
| 48 | Galates | 23 | 62 | 1 Jean | 16 |
| 49 | Éphésiens | 24 | 63 | 2 Jean | 4 |
| 50 | Philippiens | 15 | 64 | 3 Jean | 4 |
| 51 | Colossiens | 14 | 65 | Jude | 7 |
| 52 | 1 Thessaloniciens | 11 | 66 | Apocalypse | 28 |
| 53 | 2 Thessaloniciens | 7 | | | |

L'épître de **Jacques** (12 péricopes plus site de présentation) est le **gabarit de référence**
(structure et système visuel) sur lequel les autres livres ont été modelés.

#### Ancien Testament : séries complètes (38 péricopes)

| # | Livre / portée | Série | Péricopes | État |
|---|---|---|---|---|
| 01 | Genèse 1 à 11 (« De Babel à Abraham ») | ✓ | 12 | Complet |
| 19 | Psaume 19 (« Dieu a parlé ») | ✓ | 4 | Complet |
| 19 | Psaume 119 (« Une lampe à mes pieds ») | ✓ | 22 (par strophes) | Complet |

### Anatomie d'un livre traité

Chaque dossier de livre (`NN - <Livre>/`) contient :

- **`00 - Introduction/`** : le **plan de série** (`Serie.md` / `.pdf`), la **recherche globale**
  (`Recherche.md` / `.pdf`), la **page d'accueil** (`index.html`) et les logos (`LogoEBC.avif`,
  `LogoScriptura.webp`).
- **`NN - <titre> (Réf c.v-v)/`** : un dossier par semaine de prédication (péricope), contenant la
  page web `index.html` et la recherche exégétique (`Recherche-MacArthur-<Livre>-<c>-<v>-<v>.md` plus
  son `.pdf` : dans le nom de fichier, la référence s'écrit tout en traits d'union,
  `Recherche-MacArthur-Jacques-2-14-26.md` pour le dossier `05 - La foi qui agit (Jacques 2.14-26)`).
  Le numéro de semaine `NN` est sur deux chiffres (trois pour Luc et Actes).

**Gabarit d'une recherche exégétique** : Contexte du passage ; Arrière-plan historique et culturel ;
Étude des mots-clés (tableau de traductions comparées S21 / NEG79 / Darby / LSG / KJF) ; Apports des
commentateurs (niveau de source, puis prose MacArthur) ; Renvois et passages parallèles ; Thèmes
théologiques (« Dans le texte » plus « Pour votre assemblée ») ; Pistes de réflexion.

**Format canonique.** Pour une péricope, **la page `index.html` est la source** : le `.md` et le
`.pdf` en sont dérivés par `tools/regen.py`, qui les marque de l'empreinte du HTML. Toute correction
se fait dans le HTML, puis passe par la régénération ; un `.md` ou un `.pdf` modifié à la main est
une erreur que `tools/check.py` signale.

---

## Cadre théologique

Tout le contenu est élaboré dans un cadre **baptiste réformé, conforme à la théologie de John
MacArthur** (Master's Seminary), en accord avec la
[confession de foi de l'Église](<3 - Pérégrination/00 - Avant-propos/Confession de foi-EBC.pdf>). La
lecture est volontairement faite à travers la **seule lentille de MacArthur** ; en cas de divergence
d'interprétation, c'est sa lecture qui tranche. Quand ses notes d'étude et sa chaire divergent,
**le sermon prime**.

- herméneutique grammatico-historique, sens littéral, exposition suivie du texte ;
- **bibliologie** : inspiration verbale et plénière, infaillibilité, suffisance et clôture du canon ;
- **christologie** : pleine divinité éternelle et vraie humanité du Dieu-homme, naissance
  virginale ;
- **sotériologie** : élection, appel efficace et régénération monergiques (TULIP), justification
  forensique par la grâce seule au moyen de la foi seule (la foi étant elle-même un don), avec
  double imputation ; *Lordship salvation* (foi et repentance indissociables) ; persévérance des
  saints ; les œuvres **démontrent** la foi sans jamais mériter ni produire le salut (« la foi
  seule sauve, mais la foi qui sauve n'est jamais seule ») ;
- **ecclésiologie** : l'Église, mystère révélé dans le NT, distincte d'Israël ; sacerdoce de tous
  les croyants ; baptême des croyants par immersion et table du Seigneur comme ordonnances ;
  sacrifice unique de Christ (ni répétition sacrificielle ni régénération baptismale) ;
- **pneumatologie** : cessationnisme strict (les dons miraculeux et révélatoires ont cessé) ; le
  baptême de l'Esprit intervient à la conversion ;
- **eschatologie** : dispensationaliste et prémillénariste prétribulationniste ; distinction
  Israël / Église, promesses faites à Israël non spiritualisées, retour du Seigneur futur,
  littéral et imminent, suivi d'un règne millénaire terrestre.

Sources effectivement consultées, dans l'ordre de l'échelle du skill `sermon-research` : les sermons
Grace to You (gty.org, niveau 1), les notes de *La Bible d'étude MacArthur* (niveau 3) et, pour les
pages de Vision, *Théologie systématique* (MacArthur et Mayhue). Le *MacArthur New Testament
Commentary* (niveau 2) n'a pas été consulté : aucune page ne s'en réclame.

---

## Le site web

Le dépôt compte **925 pages `index.html`** : l'index racine, les 4 pages de Vision, les 4 pages de
Mission, et pour Pérégrination une page de présentation par livre (30) plus une page par péricope
(886).

Ce sont des **pages web autonomes** (HTML, CSS et JavaScript, sans dépendance de build) reprenant un
même système visuel : thème sombre à accents ambrés, polices serif *Cormorant Garamond* et
*EB Garamond*, barre de progression de lecture, barre de navigation escamotable, révélation au
défilement. Une **feuille d'impression** rend chaque page en noir sur blanc, sans décor ni
navigation. Le modèle de référence pour les livres est
[`59 - Jacques/00 - Introduction/index.html`](<3 - Pérégrination/59 - Jacques/00 - Introduction/index.html>).

L'**index racine** [`index.html`](index.html) fédère l'ensemble par sections : **Vision**,
**Mission**, puis le corpus (Ancien Testament, Évangiles, Histoire, épîtres pauliniennes, épîtres
générales, Apocalypse), et pointe vers la ressource [`Coram Deo.pdf`](<Coram Deo.pdf>). La navigation
est **aller-retour** : chaque page de présentation renvoie à cet index (« Études bibliques ») et
chaque péricope renvoie à la présentation de son livre.

Les logos affichés en tête et en pied de page, [`LogoEBC.avif`](LogoEBC.avif) et
[`LogoScriptura.webp`](LogoScriptura.webp), renvoient respectivement au site de l'Église et à celui
de la Faculté de Théologie Scriptura ; chaque lien porte un nom accessible (`aria-label`). Ce sont
les **seuls liens externes** des pages, avec les liens vers les sermons Grace to You.

**Pour consulter une page :** l'ouvrir dans un navigateur. Aucune page n'appelle de ressource
externe (ni feuille de style, ni script, ni fonte distante) : *Cormorant Garamond* et *EB Garamond*
sont simplement déclarées en CSS avec repli sur Georgia et Times New Roman. Tout fonctionne hors
ligne.

---

## Outillage et contrôle

Python standard, plus `reportlab` pour les PDF.

- **[`tools/pages.py`](tools/pages.py)** : lit une page de péricope et en tire le JSON du skill
  `sermon-research` (`python tools/pages.py <dossier>` l'affiche ; `--selftest`).
- **[`tools/regen.py`](tools/regen.py)** : régénère `.md` et `.pdf` depuis le HTML
  (`python tools/regen.py [--only-md] [dossier ...]`) et pose la ligne de déclaration du pied
  (`--footers`), avec l'état de vérification lu dans [`tools/couverture.json`](tools/couverture.json).
- **[`tools/check.py`](tools/check.py)** : liens internes, structure des pages et des recherches,
  noms accessibles, ligatures, empreinte des dérivés, déclaration, niveau de source, codes de sermon,
  sections interdites des séries, comptes du README. Exécuté à chaque poussée par
  [`.github/workflows/check.yml`](.github/workflows/check.yml).

---

## Structure du dépôt

```
.
├── README.md, LICENSE
├── index.html                                Index de navigation racine (Vision, Mission, corpus)
├── LogoEBC.avif, LogoScriptura.webp          Logos de l'Église et de la Faculté de Théologie Scriptura
├── Coram Deo.pdf                             Ressource d'accompagnement pastoral (affiche, 1 p.)
├── gauntlet-log.md                           Journal des audits et de la mise en conformité
├── Evaluation-academique-CoramDeo.md         Évaluation académique (15 septembre 2026)
├── Planification-execution-CoramDeo.md       Plan de mise en œuvre de l'évaluation
├── tools/                                    Extraction, régénération, contrôle
├── .claude/skills/                           Gabarits sermon-research et sermon-series
│
├── 1 - Vision/                               Doctrine : ce que nous croyons
│   ├── 1 - Bibliologie/index.html            La Parole de Dieu
│   ├── 2 - Christologie/index.html           Dieu le Fils : préincarné, incarné, glorifié
│   ├── 3 - Pneumatologie/index.html          Dieu le Saint-Esprit
│   └── 4 - Ecclésiologie/index.html          L'Église : but, autorité, vie, ordonnances
│
├── 2 - Mission/                              L'homme racheté (d'après The Redeemed Man)
│   ├── 1 - Trinité/index.html                Devant son Dieu
│   ├── 2 - Autrui/index.html                 Devant les siens
│   ├── 3 - Travail/index.html                Dans son ouvrage
│   └── 4 - Héritage/index.html               Jusqu'à la fin de sa course
│
└── 3 - Pérégrination/                        Expositions suivies, livre par livre
    ├── 00 - Avant-propos/                    Doctrine, piété, outillage d'extraction
    │   ├── Confession de foi-EBC.pdf         Confession de foi de l'Église (rév. 2016)
    │   ├── PrecisDicipulat.md / .pdf         Précis du discipulat chrétien
    │   ├── PlanEvangélisation.md / .pdf      Essai sur The Master Plan of Evangelism (Coleman)
    │   ├── Puritains/Guide Étude Biblique.md Méthode d'étude personnelle
    │   └── extract_nt.py, extract_at.py, md-to-pdf.py
    │
    ├── 01 - Genèse/                          AT : Genèse 1 à 11 (série complète)
    ├── 19 - Psaume 19/  19 - Psaume 119/     AT : séries de Psaumes
    └── 40 - Matthieu/ … 66 - Apocalypse/     NT : les 27 livres (complets)
        ├── 00 - Introduction/                Série, recherche globale, page d'accueil, logos
        └── NN - <titre> (Réf c.v-v)/         Un dossier par péricope (index.html + .md + .pdf)
```

Les artefacts d'outillage local (p. ex. `ruvector.db`), le cache Python, la configuration locale
`.claude/`, les sources protégées et les fichiers temporaires sont exclus du dépôt via
`.gitignore` ; `.gitattributes` force le traitement binaire des `.pdf`, que Git corromprait sinon en
injectant des CRLF.

---

## Licences

- **Contenu** (`1 - Vision/`, `2 - Mission/`, `3 - Pérégrination/`, `index.html`) :
  [Creative Commons Attribution, Pas d'utilisation commerciale, Pas de modification 4.0 International
  (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr), © 2026 André-Guy
  Bruneau.
- **Code** (`tools/`, `.claude/`, fichiers `*.py`) : licence MIT, texte dans [`LICENSE`](LICENSE).
- **Exclus** : la confession de foi et les logos appartiennent à leurs titulaires (Église Baptiste
  de Charlesbourg, Faculté de Théologie Scriptura) ; les citations bibliques (NEG 1979) restent
  sous le droit de leur éditeur.

**Réserve.** Les pages condensent et paraphrasent des ouvrages protégés (*La Bible d'étude
MacArthur*, *Théologie systématique*). La licence CC ne vaut que pour l'apport propre de l'auteur
et dans les limites de l'utilisation équitable ; l'avis d'Éditions Impact et de la Société Biblique
de Genève est à obtenir avant toute republication publique du dépôt.

---

## Crédits

- **Église Baptiste de Charlesbourg**, Charlesbourg (Québec) ; pasteur Simon Ouellette,
  [ebcharlesbourg.com](https://www.ebcharlesbourg.com/).
- **Faculté de Théologie Scriptura**, [ftscriptura.com](https://ftscriptura.com/).
- Recherches et séries **conçues et dirigées par André-Guy Bruneau** (AGB · EBC), produites avec
  Claude Code (voir la méthode ci-dessus).
- Textes bibliques : Nouvelle Édition de Genève 1979 (NEG) ; textes originaux NA28 / BHS.
- Notes d'étude : *La Sainte Bible avec commentaires de John MacArthur* (Société Biblique de
  Genève).
- Théologie systématique : MacArthur, John et Richard Mayhue, *Théologie systématique*, trad.
  Antoine Doriath, Trois-Rivières, Éditions Impact, 2018.
- Plan des chapitres de Mission : *The Redeemed Man*, Richard D. Phillips (dir.).

*Soli Deo Gloria.*
