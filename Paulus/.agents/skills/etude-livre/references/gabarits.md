# Gabarits du plan de série et du portail HTML

Ce document précise la structure du fichier `Plan-Serie-<Livre>-1-<N>.md` et le schéma JSON attendu par la sous-commande `portal` de `scripts/etude_livre.py`.

---

## 1. Structure de `Plan-Serie-<Livre>-1-<N>.md`

Pour un livre à chapitre unique (Abdias, Philémon, 2 Jean, 3 Jean, Jude), remplacer `1-<N>` par `1` dans les noms de fichiers. Aucun tiret cadratin (`\u2014`) ne doit figurer dans le fichier; utiliser `:`, `;`, `,` ou `-`.

```markdown
# Plan de série : <Nom du livre> 1 à <N>

**<Sous-titre thématique du livre>**
*Série de <N> prédications expositives (un chapitre par sermon) selon la perspective de John MacArthur*

- **Texte biblique :** Nouvelle Édition de Genève 1979 (NEG79)
- **Recherche d'ensemble sur le livre :** [`Sommaire/Recherche-MacArthur-<Slug>-1-<N>.pdf`](Sommaire/Recherche-MacArthur-<Slug>-1-<N>.pdf) ([version HTML](Sommaire/Recherche-MacArthur-<Slug>-1-<N>.html) · [Markdown](Sommaire/Recherche-MacArthur-<Slug>-1-<N>.md))

---

## Vue d'ensemble de la série

- **Idée centrale de la série :** <1 paragraphe résumant la thèse théologique du livre selon MacArthur>
- **Phrase de la série :** *« <Formule mémorisable en une phrase> »*
- **Progression homilétique :**
  1. **<Titre du bloc I> (ch. <x> à <y>)** : <synthèse du bloc>
  2. **<Titre du bloc II> (ch. <y+1> à <z>)** : <synthèse du bloc>

### Tableau récapitulatif des <N> sermons

| # | Chapitre | Bloc structurel | Titre du sermon | Verset clé | Recherche du chapitre |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | <Livre> 1 | I. <Nom court du bloc> | *<Titre du sermon 1>* | <Abrév.> 1.<v> | [`01-<Slug>-1`](01-<Slug>-1/Recherche-MacArthur-<Slug>-1.pdf) |
```

Pour chaque bloc structurel, insérer un titre de niveau 2 (`## PREMIÈRE PARTIE : ... (CHAPITRES <x> À <y>)`), suivi d'une section par chapitre :

```markdown
### Sermon <n> : <Titre du sermon> (<Livre> <n>.1-<dernier_verset>)

- **Dossier de recherche :** [`0<n>-<Slug>-<n>/Recherche-MacArthur-<Slug>-<n>.pdf`](0<n>-<Slug>-<n>/Recherche-MacArthur-<Slug>-<n>.pdf) ([HTML](0<n>-<Slug>-<n>/Recherche-MacArthur-<Slug>-<n>.html) · [Markdown](0<n>-<Slug>-<n>/Recherche-MacArthur-<Slug>-<n>.md))
- **Sermons de référence de John MacArthur (Grace to You) :**
  - *<Titre anglais>* (`<code GTY>`, `<plage>`) - <Titre français traduit>
- **Textes d'appui (Ancien et Nouveau Testament) :** <liste de renvois commentés>
- **Verset clé :**
  > « <Citation exacte mot pour mot dans la NEG79> » (<Livre> <n>.<v>, NEG79)

#### Orientation homilétique

- **Idée centrale :** <1 phrase énonçant le thème exégétique du chapitre>
- **Phrase à faire retenir :** *« <1 phrase percutante destinée à l'auditoire> »*
- **But du sermon :** <objectif pastoral et doctrinal>

#### Étapes du sermon

1. **<Titre du point 1> (<n>.<a>-<b>)** : <résumé>
   - *Sous-points :* <détail des versets>
2. **<Titre du point 2> (<n>.<c>-<d>)** : <résumé>
   - *Sous-points :* <détail des versets>

#### Développement exégétique et homilétique

##### Introduction
<Mise en contexte historique, lien avec le chapitre précédent et prise en compte explicite de toute charnière inter-chapitres>

##### 1. <Titre du point 1> (<n>.<a>-<b>)
<Exposition verset par verset intégrant la syntaxe grecque ou hébraïque, les termes clés translittérés, l'exégèse de MacArthur et les citations exactes de la NEG79>

##### Application et pistes de réflexion pastorale
- **<Axe 1> :** <question et interpellation concrète>
- **<Axe 2> :** <question et interpellation concrète>

##### Transition vers le Sermon <n+1> (ou Conclusion de la série pour le dernier chapitre)
<Pont homilétique vers le chapitre suivant>
```

Pour un livre de l'Ancien Testament où Grace to You ne compte aucun sermon séquentiel de niveau 1 sur le chapitre, remplacer la ligne **Sermons de référence** par les sources de niveaux 2 à 5 effectivement vérifiées (*MacArthur Study Bible*, *MacArthur Bible Commentary*, sermons thématiques GTY avec leur code, ou ouvrages de MacArthur).

---

## 2. Spécification JSON pour `etude_livre.py portal`

La sous-commande `portal` lit une spécification JSON (`--spec`) et écrit `<Livre>/index.html` : un portail autonome sombre et orange (`#0a0a0a` / `#e8843c`), avec CSS et JS en ligne. Le gabarit règle seul la mise en page qui dépend du livre :

- **Barre collante.** Une pastille de 44 px par sermon, sur une seule rangée. Quand les pastilles ne tiennent pas (13 ou 16 chapitres sur téléphone), la rangée défile horizontalement. Le bord qui cache des pastilles s'estompe, la molette fait défiler la rangée, et la pastille du sermon en cours reste visible.
- **Sommaire de la série.** Au plus trois colonnes, en rangées équilibrées (6 blocs : 3 + 3; 5 : 3 + 2; 4 : 2 + 2). Trois colonnes à partir de 69 rem, une ou deux à partir de 60 rem.
- **Lien de retour.** Lien vers l'accueil de la collection, en tête et en pied : `--accueil` (défaut `../index.html`; chaîne vide pour l'omettre) et `--accueil-libelle` (défaut `Paulus`).

**Exemple complet et exécutable :** [`portal_spec.exemple.json`](portal_spec.exemple.json). C'est la spécification de `12 - Tite/index.html` (trois blocs d'un sermon chacun, avec transitions et sermons GTY). La régénérer reproduit ce portail à l'identique, ce qui vérifie que le schéma décrit ici et le générateur concordent :

```powershell
uv run python .agents/skills/etude-livre/scripts/etude_livre.py portal `
  --spec .agents/skills/etude-livre/references/portal_spec.exemple.json `
  --output "$env:TEMP\portail-tite\index.html"
# puis comparer à "12 - Tite/index.html" (fins de ligne mises à part)
```

### Champs de premier niveau

Les champs « HTML » acceptent du balisage en ligne (`<strong>`, `<em>`, `<abbr>`, `<span class="nw">`), inséré tel quel. Les autres sont du texte.

| Champ | Contenu | Emplacement dans le portail |
|---|---|---|
| `book` | nom du livre, résolu par la table canonique (`"Tite"`, `"1 Timothée"`) | titres, liens et noms de fichiers |
| `date_fr` | date du plan de série (`"11 avril 2026"`) | carte du plan et pied de page |
| `meta_description` | *facultatif*; texte | `<meta name="description">` (sinon, phrase générique) |
| `series_title` | HTML | `<h1>` |
| `series_phrase` | HTML | phrase de la série, en tête et en conclusion |
| `header_verse` | `{"text", "ref"}` : verset NEG79 sans guillemets, référence | verset de l'en-tête |
| `book_card` | `{"summary_html", "question_html"}` : HTML | carte « Recherche sur tout le livre » |
| `plan_card` | `{"heading", "summary_html"}` : texte, HTML | carte « Plan de série » |
| `movements_heading` | texte | titre de l'encadré des mouvements |
| `movements` | liste de `{"ref", "label"}` : référence, HTML | mouvements numérotés de la lettre |
| `sermons_section` | `{"heading", "lead_html", "question_html"}` : texte, HTML, HTML | en-tête de la section des sermons |
| `blocks` | liste des blocs structurels (tableau suivant) | sommaire et sections par bloc |
| `conclusion` | `{"heading", "benediction": {"text", "ref"}}` | conclusion et bénédiction finale |

### Blocs et sermons

| Champ | Contenu |
|---|---|
| `blocks[].ch_label` | étiquette du bloc (`"Chapitre\u00a01"`, `"Chapitres 1 et 2"`) |
| `blocks[].short_title` | titre court, dans le sommaire de la série |
| `blocks[].full_title` | titre complet, en tête de la section du bloc |
| `blocks[].sermons[]` | sermons du bloc, dans l'ordre (champs ci-dessous) |
| `num` | numéro du sermon, égal au numéro du chapitre (entier) |
| `title` | titre du sermon (HTML) |
| `gty_range` | ligne des sermons GTY (HTML), p. ex. `"11 sermons GTY (56-1 à 56-11) · Tite 1.1-16 (16 versets)"` |
| `phrase` | phrase à faire retenir, sans guillemets |
| `key_verse` | `{"text", "ref"}` : verset clé NEG79 sans guillemets, référence |
| `central_idea` | idée centrale (HTML) |
| `steps[]` | `{"num", "name", "ref"}` : étiquette (`"I."`, `"Intro."`, `"Concl."`), intitulé (HTML), référence (`"(1.1-4)"`) |
| `gty_sermons[]` | *facultatif* : `{"code", "title", "ref"}`, soit le code GTY, le titre anglais et le passage |
| `transition` | `null` (ou absent) pour le dernier sermon, sinon `{"text", "next_num", "next_title"}` |
| `rappel_short` | titre court repris dans le rappel de la conclusion |

### Règles de formatage
- Le nombre de sermons, tous blocs confondus, est égal au nombre de chapitres, numérotés de `1` à `N` dans l'ordre. Le générateur ne le contrôle pas : `etude_livre.py verify` signale ensuite tout fichier de chapitre manquant.
- Le gabarit ajoute lui-même les guillemets « » autour des versets et de la phrase à faire retenir : ne pas les mettre dans le JSON.
- Les références à ne pas couper prennent `\u00a0` (espace insécable) ou `<span class="nw">...</span>`. Sur téléphone étroit (moins de 26 rem), le gabarit laisse toutefois passer à la ligne les références longues des mouvements, des questions, des légendes et des sermons GTY.
- Aucun tiret cadratin (`\u2014`) : `verify` le refuse dans les `.json`, `.md` et `.html`.
