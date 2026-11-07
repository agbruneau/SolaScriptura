# Planification d'exécution : mise en œuvre de l'évaluation académique

**Document source :** `Evaluation-academique-CoramDeo.md` (15 septembre 2026), recommandations P0 à P2.
**Point de départ :** commit `5d330f0`, dépôt public, 0 fork, 0 étoile, pas de GitHub Pages (vérifié le 15 septembre).
**Régime :** production. Chaque lot se termine par un critère d'acceptation vérifiable et par une entrée dans `gauntlet-log.md`.
**Cible :** faire passer le dépôt de D+ (56) à la zone B- à B (71 à 75) par les lots 1 à 8 ; le lot 9 est facultatif et ne relève que d'une version académique.

Les efforts sont des estimations. Une « séance » est une session de travail avec Claude Code d'une à trois heures. Les « agents » suivent l'unité de compte du journal d'audit existant. Les heures humaines désignent ce que seul l'auteur peut faire.

---

## 1. Décisions préalables

Six décisions conditionnent les lots. Elles se prennent au lot 0, avant toute exécution.

| # | Décision | Options | Recommandation | Lots touchés |
|---|---|---|---|---|
| D1 | Visibilité du dépôt pendant et après les travaux | (a) privé définitivement ; (b) privé pendant la purge, public après ; (c) rester public et purger à chaud | **(b)**. Passer en privé le jour 1 arrête la diffusion des sources protégées immédiatement, sans attendre la purge. Republier une fois l'historique nettoyé et la déclaration en place. | 1, 2 |
| D2 | Format canonique des recherches | (a) HTML canonique, `.md` et `.pdf` dérivés ; (b) Markdown canonique, `.html` et `.pdf` dérivés | **(a)**. Les corrections d'audit ont été faites sur le HTML ; le HTML contient du texte éditorial absent du `.md` (accroches de section, verset-clé, description) ; les identifiants de section des pages sont ceux du gabarit du skill. Choisir (b) obligerait à reporter à la main les corrections de 14 pages et à réécrire un générateur qui reproduit les accroches. | 3, 5, 6, 7 |
| D3 | Licences | Contenu : CC BY-NC-ND 4.0 ; code (`.py`, skills) : MIT | Recommandé tel quel. Réserve : une licence CC sur des condensés d'ouvrages protégés ne vaut que si la paraphrase reste dans les limites de l'utilisation équitable ; demander l'avis d'Éditions Impact et de la Société Biblique de Genève avant republication publique. | 2 |
| D4 | Devenir des 30 séries | (a) régénérer selon le skill actuel ; (b) retirer les trois sections interdites et ajouter les sections manquantes en place ; (c) amender le skill pour reconnaître le format existant | **(b)**, avec « Carte doctrinale » déclarée facultative dans le skill pour les séries antérieures à septembre 2026. C'est le compromis qui rend le corpus conforme à la méthode déclarée sans tout réécrire. | 8 |
| D5 | Formulation de la paternité | Texte de la déclaration d'usage de l'IA (annexe A) et remplacement de « Recherches et séries signées AGB » | Adopter l'annexe A ; « conçues, dirigées et vérifiées par AGB » plutôt que « signées ». | 2 |
| D6 | Plafond budgétaire de la vérification d'attribution (lot 7) | Un plafond global d'agents et un plafond par livre, fixés avant lancement, comme au volet 2 du journal | Plafond global 240 agents, par livre selon le nombre de péricopes (une tranche de 4 pages par agent), règle d'arrêt si un livre dépasse 130 % de son plafond. | 7 |

Deux décisions secondaires, à prendre au fil de l'eau : D7, statut des fichiers `Puritains/*.docx` et `*.pptx` (auteur inconnu ; à garder seulement si l'auteur en est propriétaire) ; D8, faire ou non le lot 9.

---

## 2. Vue d'ensemble des lots

| Lot | Objet | Recommandations couvertes | Dépend de | Effort estimé | Livrable de sortie |
|---|---|---|---|---|---|
| 0 | Décisions, gel, sauvegarde | préalable | rien | 1 séance, 1 h humaine | D1 à D6 consignées dans `gauntlet-log.md` ; `coramdeo.bundle` hors dépôt |
| 1 | Retrait des sources protégées et purge de l'historique | P0.1 | 0 | 2 séances | historique sans les 62 fichiers ; scripts pointant hors dépôt |
| 2 | Déclarations : IA, licence, README | P0.2, P0.3, P2.10 | 0 | 1 séance, 1 h humaine | `LICENSE`, section README, ligne de pied sur 925 pages |
| 3 | Outillage : extraction, régénération, contrôle, intégration continue, index des sermons | P1.6, P2.12, P2.13 (prépare P1.4) | 0 (D2) | 4 séances | `tools/` avec 5 scripts, workflow GitHub, `gty-index.json` |
| 4 | Corrections mécaniques : liens-logos, ligatures, feuille d'impression | P2.8, P2.9, P2.11 | 3 (contrôle) | 1 séance | 925 pages corrigées, contrôle vert |
| 5 | Synchronisation des corrections d'audit | P1.6 | 3 | 1 séance | 14 dossiers avec `.md` et `.pdf` régénérés |
| 6 | Niveaux de source et références sur 886 recherches et 4 pages Vision | P1.4 | 3 | 3 séances, 4 h humaines | 886 sections « Apports » avec niveau, table de sermons, notes ; Vision avec chapitres |
| 7 | Vérification d'attribution sur 903 pages | P1.5 | 3, 6 | ≈ 240 agents en 27 lots | tableau de couverture par livre dans le README ; corrections appliquées |
| 8 | Mise en conformité des 30 séries | P1.7 | 3 | 3 séances | 30 `Serie.md` conformes, régénérés |
| 9 | Distance critique sur les textes exigeants (facultatif) | P2.14 | 8 | selon D8 | notes de lectures concurrentes |
| 10 | Clôture et réévaluation | tous | 1 à 8 | 1 séance | grille C1 à C8 rejouée, journal clos |

Chemin critique : 0 → 1 → 3 → 6 → 7. Les lots 2, 4, 5, 8 s'insèrent en parallèle dès que le lot 3 livre le contrôle et le régénérateur.

---

## 3. Détail des lots

### Lot 0 : décisions, gel, sauvegarde

| Tâche | Contenu | Acceptation |
|---|---|---|
| 0.1 | Consigner D1 à D6 dans `gauntlet-log.md`, section « Volet 3 : mise en conformité », avec date | entrée présente |
| 0.2 | Sauvegarde complète hors OneDrive : `git bundle create ../coramdeo-avant-purge.bundle --all`, plus copie des quatre PDF et des 60 `.md` de référence dans un dossier local hors dépôt | bundle restaurable (`git clone coramdeo-avant-purge.bundle test`) |
| 0.3 | Passer le dépôt en privé (D1) : `gh repo edit agbruneau/CoramDeo --visibility private --accept-visibility-change-consequences` | `gh repo view --json visibility` renvoie PRIVATE |
| 0.4 | Geler les contributions : aucune modification de contenu tant que le lot 3 n'a pas livré le contrôle | règle écrite dans le journal |

**Point d'attention.** Le dépôt vit dans un dossier OneDrive. Les opérations Git massives (purge, régénération de 954 PDF) déclenchent des synchronisations et des conflits. Suspendre OneDrive pendant les lots 1, 3 et 5, ou travailler dans un clone hors OneDrive et pousser ensuite.

### Lot 1 : retrait des sources protégées et purge

Fichiers visés (62) : `NEG - MacArthur.pdf`, `Vallée de la Vision.pdf`, les 30 `NEG - <Livre>.md`, les 30 `JMA - <Livre>.md`. Selon D7, éventuellement les `.docx` et `.pptx` de `Puritains/`.

| Tâche | Contenu | Acceptation |
|---|---|---|
| 1.1 | Créer un dossier local hors dépôt, par exemple `%USERPROFILE%\CoramDeo-sources\`, y déplacer les 62 fichiers en conservant la structure `<NN - Livre>/`. Définir la variable d'environnement `CORAMDEO_SOURCES` | fichiers présents et lisibles hors dépôt |
| 1.2 | Adapter `extract_nt.py` et `extract_at.py` : chemin du PDF et dossier de sortie lus dans `CORAMDEO_SOURCES` (repli sur le dossier du script) | `python extract_nt.py` régénère un livre dans le dossier externe |
| 1.3 | Ajouter au `.gitignore` : `NEG - *.md`, `JMA - *.md`, `NEG - MacArthur.pdf`, `Vallée de la Vision.pdf` | `git status` propre après remise des fichiers en place localement |
| 1.4 | Retirer les fichiers de l'index (`git rm --cached`), commit « Sources protégées retirées du dépôt » | `git ls-files` ne les liste plus |
| 1.5 | Purge de l'historique dans un clone frais hors OneDrive : `pip install git-filter-repo`, puis `git filter-repo --invert-paths` avec un `--path` par fichier (ou `--path-glob "*/JMA - *.md"` et `--path-glob "*/NEG - *.md"`). Vérifier : `git log --all --oneline -- "<chemin>"` vide pour chaque fichier ; `git count-objects -vH` en baisse (attendu : environ 35 Mo de moins sur 206 Mio, les PDF de recherche restant) | 0 trace dans `--all` |
| 1.6 | **Point d'arrêt : poussée forcée.** Elle réécrit `main`. À faire seulement après validation de 1.5 par l'auteur : `git push --force --all` puis `git push --force --tags`. Reclonage local ensuite ; le bundle de 0.2 reste la copie de sûreté | dépôt distant réécrit, clone local aligné |
| 1.7 | Demander à GitHub la suppression des vues en cache des commits purgés (formulaire de support, motif : contenu protégé). Sans fork ni étoile, le risque résiduel est faible ; la demande reste la seule façon de fermer les URL de commits directs | demande envoyée, numéro noté au journal |
| 1.8 | Mettre à jour les 8 passages du README qui décrivent ou lient ces fichiers : les décrire comme sources locales de l'auteur, non versionnées, obtenues sous licence personnelle | aucun lien du README ne pointe vers un fichier retiré |

**Ce que le lot ne change pas.** La méthode de vérification (confronter chaque attribution aux notes locales) reste entière : les fichiers existent toujours sur la machine de l'auteur, sous la licence d'usage personnel qu'il a acquise. Seule leur redistribution cesse.

### Lot 2 : déclarations

| Tâche | Contenu | Acceptation |
|---|---|---|
| 2.1 | `LICENSE` selon D3 : texte CC BY-NC-ND 4.0 pour `1 - Vision`, `2 - Mission`, `3 - Pérégrination`, `4 - Sermon` ; MIT pour `.claude/`, `tools/`, `*.py`. Une section « Licences » dans le README qui énonce la partition et la réserve sur les sources | fichier présent, README cohérent |
| 2.2 | Section README « Méthode de production et usage de l'intelligence artificielle » (annexe A) : outil, rôle de l'auteur, dates, périmètre du contrôle humain, tableau de couverture de l'audit (initialisé avec Vision, Mission et Genèse 1-11 ; alimenté par le lot 7) | section présente, tableau à 3 lignes au départ |
| 2.3 | Remplacer la ligne « Recherches et séries signées AGB · EBC » (D5) | ligne remplacée |
| 2.4 | Ligne de pied sur les 925 pages, après « Citations bibliques : … » : « Texte produit avec l'assistance de l'IA générative sous la direction d'André-Guy Bruneau ; voir la méthode dans le dépôt. » Insertion par substitution unique sur le motif `Citations bibliques : Nouvelle Édition de Genève 1979 (NEG)` | 925 pages contiennent la ligne (contrôle du lot 3) |
| 2.5 | Étiquette de pied des PDF : passer `label=` à `make_page_footer` dans les deux `generate-pdf.py` pour inclure la mention « produit avec l'assistance de l'IA » ; effectif à la régénération (lot 3) | étiquette visible sur un PDF régénéré |
| 2.6 | Corriger les autres écarts du README (annexe A de l'évaluation) : 4 pages Vision, `4 - Héritage`, `00 - Avant-propos`, `4 - Sermon` documenté, `HistoireBible` retiré, compte des pages tiré du contrôle | contrôle du lot 3 compare les comptes du README au dépôt |

### Lot 3 : outillage

C'est le lot qui rend les autres possibles et qui répond au critère C7. Tout est en Python standard plus `reportlab` déjà requis ; aucune dépendance nouvelle.

| Tâche | Contenu | Acceptation |
|---|---|---|
| 3.1 | `tools/extract_page.py` : lit un `index.html` de péricope et produit le JSON du skill `sermon-research` (`passage`, `date`, `pastor_name`, `passage_context`, `historical_background`, `word_studies`, `commentary_insights`, `cross_references`, `theological_themes`, `thinking_prompts`, plus `source_level` et `sermon_links` s'ils sont présents). Règle : accroche de section (`.lead`) et corps (`.body p`) concaténés ; verset-clé du hero conservé dans un champ `key_verse` ignoré par le générateur | sur Matthieu 3.1-12, le JSON réinjecté dans `generate-pdf.py` produit un `.md` dont le corps ne diffère de l'actuel que par la typographie et l'accroche |
| 3.2 | `tools/regen.py` : pour un dossier, une liste ou tout le corpus, enchaîne 3.1 puis `generate_pdf()` importé du skill, avec le nom de fichier du corpus. Option `--only-md` pour éviter de régénérer 954 PDF à chaque passe | régénération de `59 - Jacques` (12 péricopes) sans erreur ; diff `.md` avant/après lisible |
| 3.3 | `tools/check.py`, exécutable en local et en intégration continue : liens internes résolus ; 7 sections dans chaque `.md` et 7 `id` dans chaque page ; présence de « Niveau de source » (avertissement tant que le lot 6 n'est pas fini, erreur après) ; aucun `alt=""` sur un logo dans un lien ; aucun tiret cadratin dans les recherches ; aucune séquence `oe` d'une liste de mots à ligature ; `.md` et `.pdf` non antérieurs au `.html` du même dossier ; comptes du README (pages, péricopes) égaux à ceux du dépôt ; ligne de déclaration présente sur chaque page. Sortie : tableau et code de retour | passe sur le dépôt après les lots 2, 4, 5 |
| 3.4 | `.github/workflows/check.yml` : `python tools/check.py` à chaque poussée. Aucune génération de PDF en intégration continue | workflow vert |
| 3.5 | `tools/gty-index.json` : extraction de l'archive Grace to You par Écriture. L'archive (`gty.org/sermons/archive?tab=scripture`) rend la liste complète d'un livre dans la page après sélection du livre, sans pagination : titre, date, passage, code (vérifié le 15 septembre sur Genèse et Matthieu). Procédure : 27 sélections dans le navigateur, texte de page capturé, analysé en entrées `{code, title, date, book, chapter, verses}`. Livrer aussi les 17 livres de l'AT couverts par l'archive | 27 livres NT présents ; nombre d'entrées par livre consigné ; sondage de 20 codes ouverts sur gty.org sans erreur |
| 3.6 | `tools/match_sermons.py` : pour chaque péricope, candidats de `gty-index.json` dont le passage chevauche la plage de versets ; sortie par livre en Markdown pour relecture, avec un champ « retenu » à cocher | 848 péricopes NT avec au moins un candidat ou la mention « aucun sermon » ; 38 péricopes AT idem |
| 3.7 | `tools/jma_notes.py` : pour une péricope, liste des amorces de notes du fichier `JMA - <Livre>.md` externe couvrant la plage (`**3.7 de pharisiens…**` donne « Mt 3.7 ») | liste correcte sur Matthieu 3.1-12 (attendu : 3.1, 3.2, 3.3, 3.4, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12) |

**Ordre interne :** 3.3 d'abord (il sert à mesurer tout le reste), puis 3.1 et 3.2 validés sur Jacques, puis 3.5 à 3.7.

### Lot 4 : corrections mécaniques

| Tâche | Contenu | Acceptation |
|---|---|---|
| 4.1 | Liens-logos : 5 variantes de balise, toutes avec `alt=""` (3 variantes × 925 pages, 2 × 9 pages). Substitution : `LogoEBC.avif` → `alt="Église Baptiste de Charlesbourg"`, `LogoScriptura.webp` → `alt="Faculté de Théologie Scriptura"` | contrôle : 0 lien sans nom |
| 4.2 | Ligatures, liste fermée pour ne pas toucher « coexister », « goel », « Phoebé », « Zoé », « coercition » : cœur(s), contrecœur, œuvre(s), œuvrer, manœuvre, œil, vœu(x), sœur(s), bœuf(s), nœud(s), chœur, mœurs, œcuménisme. Appliquer sur les 925 pages ; les `.md` suivent par régénération (D2) | contrôle : 0 occurrence des formes sans ligature dans la liste |
| 4.3 | Feuille d'impression : bloc `@media print` commun (fond blanc, texte noir, navigation et couches décoratives masquées, liens en clair) inséré avant `</style>` dans les 925 pages. Le thème clair à l'écran reste facultatif ; la feuille d'impression répond au besoin réel (lecteurs aînés, chaire) | impression PDF d'une page depuis le navigateur lisible en noir sur blanc |
| 4.4 | Régénérer `.md` et `.pdf` de tout le corpus après 4.1 à 4.3 (`tools/regen.py`), pour que les trois formats soient à jour et datés après le HTML | contrôle : dates cohérentes sur 886 dossiers |

### Lot 5 : synchronisation des corrections d'audit

Avec D2 (a), le lot se réduit à régénérer `.md` et `.pdf` pour les 13 pages de Genèse et pour `46 - 1 Corinthiens/16` depuis leur HTML corrigé. Le lot 4.4 le fait déjà pour tout le corpus ; la tâche propre du lot 5 est la vérification ciblée.

| Tâche | Contenu | Acceptation |
|---|---|---|
| 5.1 | Sur les 14 dossiers, vérifier que les corrections nommées au journal sont dans le `.md` régénéré : absence de « nuage de vapeur » attribué à MacArthur, absence de « nouvel Israël spirituel », présence de la lecture chaire sur les sept points du tableau du journal | 14 dossiers vérifiés, consignés |
| 5.2 | Règle écrite dans le README et dans le skill : toute correction se fait dans le HTML puis passe par `tools/regen.py` ; un `.md` ou un `.pdf` modifié à la main est une erreur que le contrôle signale par la date | règle présente, contrôle actif |

Si D2 (b) était retenue malgré la recommandation : reporter à la main le diff du commit `2cf6eba` (13 fichiers, 161 insertions, 90 suppressions) et de la correction 1 Corinthiens dans les `.md`, puis régénérer HTML et PDF ; compter 2 séances de plus.

### Lot 6 : niveaux de source et références

| Tâche | Contenu | Acceptation |
|---|---|---|
| 6.1 | Relecture des appariements de 3.6, livre par livre : retenir les sermons dont le passage couvre la péricope, écarter les sermons thématiques (« Matthew » sans chapitre). Effort humain concentré ici : environ 4 heures pour 27 livres, par sondage de 10 % et validation en bloc des appariements univoques | fichier d'appariement validé, 848 péricopes |
| 6.2 | Injection dans le HTML de chaque péricope, section `#commentateurs`, sous le titre : bloc « Niveau de source » et tableau Code / Sermon / Passage selon le gabarit du skill (ids et classes existants, aucun CSS nouveau). NT : « Niveau 1 — sermons Grace to You <codes> ». AT sans sermon : « Niveau 3 — notes de La Bible d'étude MacArthur sur <références de 3.7> ». Jamais de code absent de `gty-index.json` | 886 pages avec niveau ; contrôle vert sur la règle « code présent dans l'index » |
| 6.3 | Ajout, sous le niveau, de la ligne « Notes de la Bible d'étude consultées : Mt 3.1, 3.2, … » produite par 3.7. C'est la référence localisable minimale pour chaque attribution de niveau 3 | 886 pages avec la ligne |
| 6.4 | Régénération `.md` et `.pdf` (le générateur rend déjà `source_level` et `sermon_links`) | dates cohérentes, PDF affichant le tableau |
| 6.5 | Pages Vision : ajouter à chaque `h2` la référence au chapitre de *Théologie systématique* (MacArthur et Mayhue, 2018) et, si l'auteur a l'ouvrage sous la main, les pages. Pages Mission : chapitre de *The Redeemed Man* déjà nommé ; ajouter les références de la Bible d'étude citées | 8 pages avec références de chapitre ; pages là où disponibles |
| 6.6 | Skill `sermon-research` : ajouter à la section « Sorties » que `gty-index.json` est la seule source autorisée de codes | skill mis à jour |

Ce que le lot ne fait pas : citer le *MacArthur New Testament Commentary* par volume et page. L'ouvrage n'est pas dans les sources locales ; le déclarer sans l'avoir consulté serait une référence fabriquée. Le niveau 2 reste vide tant que l'auteur ne dispose pas des volumes.

### Lot 7 : vérification d'attribution

Protocole : celui que l'auteur a défini au volet 2 du journal, appliqué aux 903 pages restantes (886 recherches moins 13 Genèse, plus 30 recherches globales).

| Tâche | Contenu | Acceptation |
|---|---|---|
| 7.1 | `tools/attributions.py` : pour une page, extraire chaque phrase qui nomme MacArthur (attendu : environ 15 par page, 13 800 au total) avec sa section, et joindre les notes JMA de la plage (3.7) et, pour le NT, les codes de sermons retenus (6.1) | fichier de travail par livre |
| 7.2 | Par livre, en tranches de 4 pages : un vérificateur confronte chaque phrase d'abord à la note locale, puis à la transcription du sermon sur gty.org (les pages de sermon sont accessibles ; l'archive donne le code). Verdict par phrase : conforme, extrapolation à reformuler sans le nom, mésattribution à corriger, contradiction note/chaire à trancher côté chaire (règle de l'auteur) | tableau par livre : phrases vérifiées, reformulées, corrigées |
| 7.3 | Correction dans le HTML, régénération, entrée au journal par livre avec les chiffres, mise à jour du tableau de couverture du README (2.2) | par livre : contrôle vert, journal à jour |
| 7.4 | Ordre des livres : celui que la prédication de l'Église utilisera en premier, décidé par l'auteur ; à défaut, ordre canonique. Plafonds selon D6. Règle d'arrêt : si un livre dépasse 130 % de son plafond, suspendre et réviser le protocole avant de continuer | plafonds et ordre consignés avant le premier lot |

**Estimation.** Au ratio du journal (un agent par 4 pages), 903 pages donnent environ 226 agents, arrondis à 240 avec les arbitrages. Ce lot est parallélisable par livre ; c'est le seul du plan où le gain serait net, et la décision de lancer des agents en parallèle appartient à l'auteur.

**Sortie attendue au niveau du site.** Chaque page porte, dans le pied, l'état « Attribution vérifiée le <date> » ou « Attribution non vérifiée » ; la mention est produite par `tools/regen.py` à partir du tableau de couverture, jamais écrite à la main.

### Lot 8 : séries

Selon D4 (b), pour chacun des 30 `Serie.md` et de leur page `00 - Introduction/index.html` :

| Tâche | Contenu | Acceptation |
|---|---|---|
| 8.1 | Retirer « Propositions de titre », « Arc narratif de la série », « Recommandation pour le lancement » | 0 occurrence des trois titres (contrôle) |
| 8.2 | Ajouter « Niveau de source » en tête, tiré de `gty-index.json` pour le livre (série de sermons existante ou non) | 30 séries avec niveau |
| 8.3 | Ajouter « Textes exigeants » : par livre, les péricopes qui demandent une décision doctrinale explicite, avec la difficulté, la lecture retenue et le niveau qui l'appuie. Base de travail : les sections « Thèmes théologiques » des recherches du livre, où ces textes sont déjà identifiés | 30 séries avec la section, au moins 3 entrées par livre |
| 8.4 | Ajouter, dans le tableau semaine par semaine, une colonne « Base du découpage » (charnière, changement d'interlocuteur, inclusion, formule de transition). Pour le NT, la base est le découpage de MacArthur lui-même, vérifiable dans l'index des sermons | colonne remplie sur 30 séries |
| 8.5 | Amender le skill `sermon-series` : « Carte doctrinale » facultative pour les séries antérieures à septembre 2026 ; sinon, l'écrire pour les 30 livres (ajouter 2 séances) | skill et séries cohérents |
| 8.6 | Régénérer PDF et HTML des 30 introductions | contrôle vert |

### Lot 9 : distance critique (facultatif, D8)

Pour chaque « texte exigeant » du lot 8, une note de deux à quatre phrases qui nomme les lectures concurrentes avant de retenir celle de MacArthur, avec une référence par lecture. Ce lot contredit la règle « aucun cadre concurrent » des skills ; il ne se fait que si l'auteur veut une version académique distincte de la version d'église, auquel cas la note vit dans un bloc `<details>` replié, absent des PDF d'église. Effort : dépend du nombre de textes retenus (attendu : 90 à 150 pour 30 livres).

### Lot 10 : clôture

| Tâche | Contenu | Acceptation |
|---|---|---|
| 10.1 | Rejouer toutes les vérifications de l'annexe B de l'évaluation avec `tools/check.py` et consigner les résultats | tableau avant/après dans le journal |
| 10.2 | Rejouer la grille C1 à C8 et écrire le delta justifié par critère | note révisée dans `Evaluation-academique-CoramDeo.md`, section « Réévaluation » |
| 10.3 | Décider de la republication publique (D1) : conditions cumulatives : lot 1 terminé, lot 2 terminé, réserve de D3 levée ou assumée par écrit | décision consignée |

---

## 4. Calendrier indicatif

| Semaine | Lots | Jalon de fin de semaine |
|---|---|---|
| 1 | 0, 1, 2 | Dépôt privé, historique purgé, déclarations et licence en place |
| 2 | 3 | Contrôle, régénérateur validé sur Jacques, index des sermons livré |
| 3 | 4, 5, 6.1 | 925 pages corrigées, trois formats resynchronisés, appariements relus |
| 4 | 6.2 à 6.6, 7.4 | 886 pages avec niveau de source ; plafonds du lot 7 fixés |
| 5 à 9 | 7 (par livre), 8 en parallèle | couverture d'attribution qui progresse livre par livre ; 30 séries conformes à la semaine 7 |
| 10 | 10, puis 9 si D8 | réévaluation, décision de republication |

Le calendrier suppose une à deux séances par jour ouvrable. La durée réelle dépend surtout du lot 7, dont le rythme est celui de la vérification, pas de la génération.

---

## 5. Suivi

Indicateurs, tous produits par `tools/check.py` et reportés dans le README à chaque lot :

| Indicateur | Valeur de départ | Cible |
|---|---|---|
| Fichiers protégés dans l'historique | 62 | 0 |
| Liens internes brisés | 0 | 0 |
| Pages avec ligne de déclaration | 0 / 925 | 925 |
| Liens-logos sans nom | 2 793 | 0 |
| Recherches avec niveau de source | 0 / 886 | 886 |
| Codes de sermon hors index | non mesuré | 0 |
| Dossiers dont `.md` ou `.pdf` est antérieur au `.html` | 14 connus | 0 |
| Pages dont l'attribution est vérifiée | 20 / 923 | 923 |
| Séries contenant une section interdite | 30 / 30 | 0 |
| Écarts README / dépôt | 8 | 0 |

Journal : une entrée par lot dans `gauntlet-log.md`, avec les chiffres, le coût consommé et les arbitrages, dans la forme déjà en usage.

---

## 6. Risques et parades

| Risque | Effet | Parade |
|---|---|---|
| Purge ou poussée forcée qui détruit l'historique utile | perte du travail de juin à septembre | bundle du lot 0 ; purge dans un clone frais ; poussée forcée seulement après vérification de 1.5 par l'auteur |
| Synchronisation OneDrive pendant la purge ou la régénération | dépôt corrompu, fichiers en conflit | suspendre OneDrive ou travailler hors OneDrive pendant les lots 1, 3, 4 |
| Régénération qui altère le contenu des `.md` | perte silencieuse de texte | diff obligatoire sur Jacques avant tout passage global ; contrôle des 7 sections après régénération |
| Codes de sermon inventés | citation fabriquée | seule source : `gty-index.json` ; contrôle bloquant |
| Lot 7 qui dépasse le budget | travail inachevé sans le savoir | plafonds par livre, règle d'arrêt, couverture affichée page par page pour que l'inachèvement soit visible |
| Nouveaux écarts README / dépôt | retour de la dérive documentaire | comptes du README vérifiés par le contrôle en intégration continue |
| Réserve de droit d'auteur sur les condensés de *Théologie systématique* | republication contestable | demander l'avis de l'éditeur avant D1 (b) ; à défaut, rester privé |
| Contradictions note / chaire découvertes pendant le lot 7 | arbitrages qui s'accumulent | appliquer la règle écrite (le sermon prime) et consigner chaque cas au journal, comme pour Genèse |

---

## Annexe A : déclaration d'usage de l'IA générative (texte proposé)

> **Méthode de production et usage de l'intelligence artificielle.** Les recherches exégétiques, les plans de série et les pages de ce dépôt ont été produits entre mai et septembre 2026 avec Claude Code (Anthropic), à partir de deux gabarits de génération versionnés dans `.claude/skills/`, sous la direction d'André-Guy Bruneau, qui a fixé le cadre théologique, les sources autorisées, la structure des livrables et les règles de vérification. Le texte biblique de référence est la Nouvelle Édition de Genève 1979 ; les positions attribuées à John MacArthur proviennent de ses sermons Grace to You et des notes de *La Bible d'étude MacArthur*, consultés localement sous licence d'usage personnel et non redistribués. Le contrôle humain a porté sur la conception, la relecture par sondage et un audit doctrinal dont la portée exacte est donnée dans le tableau ci-dessous et dans `gauntlet-log.md`. Une page dont l'attribution n'a pas été vérifiée le dit dans son pied. Toute erreur d'attribution qui subsiste est de la responsabilité de l'auteur, non de MacArthur.

Tableau de couverture (initial) :

| Volet | Pages | Conformité doctrinale | Attribution vérifiée |
|---|---|---|---|
| Vision et Mission | 8 | 7 (gauntlet, août 2026) | sans objet (sources systématiques) |
| Pérégrination, Genèse 1-11 | 13 | 13 (gauntlet, août 2026) | 13 (246 attributions, 10 corrigées) |
| Pérégrination, autres livres | 903 | triage par signature seulement | 0 |

## Annexe B : fichiers à retirer au lot 1

- `3 - Pérégrination/00 - Avant-propos/NEG - MacArthur.pdf` (2 216 pages, 32 Mo)
- `3 - Pérégrination/00 - Avant-propos/Vallée de la Vision/Vallée de la Vision.pdf` (434 pages)
- `3 - Pérégrination/<NN - Livre>/NEG - <Livre>.md` (30 fichiers, 197 218 mots)
- `3 - Pérégrination/<NN - Livre>/JMA - <Livre>.md` (30 fichiers, 527 538 mots)
- selon D7 : `3 - Pérégrination/00 - Avant-propos/Puritains/*.docx`, `*.pptx`, `Vallée de la Vision/*.pptx`

Restent dans le dépôt : `Confession de foi-EBC.pdf` (document de l'Église), `Coram Deo.pdf`, les essais `.md` de l'auteur et leurs PDF, les scripts.

## Annexe C : commandes clés

```bash
git bundle create ../coramdeo-avant-purge.bundle --all
```

```bash
gh repo edit agbruneau/CoramDeo --visibility private --accept-visibility-change-consequences
```

```bash
pip install git-filter-repo
```

```bash
git filter-repo --invert-paths --path "3 - Pérégrination/00 - Avant-propos/NEG - MacArthur.pdf" --path "3 - Pérégrination/00 - Avant-propos/Vallée de la Vision/Vallée de la Vision.pdf" --path-glob "3 - Pérégrination/*/NEG - *.md" --path-glob "3 - Pérégrination/*/JMA - *.md"
```

```bash
python tools/check.py
```

```bash
python tools/regen.py "3 - Pérégrination/59 - Jacques" --only-md
```
