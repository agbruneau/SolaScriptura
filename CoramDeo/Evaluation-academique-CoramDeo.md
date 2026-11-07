# Évaluation académique du dépôt CoramDeo

**Objet évalué :** dépôt `agbruneau/CoramDeo`, branche `main`, commit `5d330f0` (8 septembre 2026), public sur GitHub.
**Auteur du travail :** André-Guy Bruneau (AGB), pour l'Église Baptiste de Charlesbourg (EBC).
**Date de l'évaluation :** 15 septembre 2026.
**Régime :** évaluation universitaire, selon le gabarit décrit en partie I. La note mesure la recevabilité académique du travail, non son utilité pastorale, qui est traitée à part (critère 5).

---

## Partie I : gabarit d'évaluation retenu

### 1. Nature de l'objet

Le dépôt n'est ni un mémoire ni un logiciel. C'est un **corpus de ressources de théologie pratique** (homilétique et exégèse pastorale), publié sous forme de site statique, avec trois composantes :

| Composante | Contenu | Volume vérifié |
|---|---|---|
| Doctrinale (`1 - Vision`, `2 - Mission`) | 4 traités de théologie systématique, 4 expositions sur la vie du racheté | 8 pages, 30 850 mots de corps de texte |
| Exégétique (`3 - Pérégrination`) | 30 livres bibliques : plan de série, recherche globale, une recherche par péricope | 886 recherches (.md, .pdf, .html), 30 séries, 30 introductions ; recherches ≈ 2,78 M mots |
| Infrastructure | site statique, scripts d'extraction et de PDF, deux skills Claude Code, journal d'audit doctrinal | 925 pages `index.html`, 6 scripts Python, 2 `SKILL.md`, `gauntlet-log.md` |

### 2. Choix du gabarit

Trois gabarits ont été considérés :

- **Grille de mémoire de recherche** (problématique, hypothèse, état de la question, démonstration). Rejetée : le travail ne pose pas de question de recherche et ne vise pas une démonstration.
- **Grille d'évaluation logicielle** (architecture, tests, maintenabilité). Rejetée : le code est instrumental, le contenu est l'objet.
- **Grille de projet d'intégration ou travail dirigé de 2e cycle en théologie pratique, volet humanités numériques.** Retenue. Elle évalue un livrable appliqué (ici un corpus homilétique) sur sa cohérence, son cadre, sa méthode, ses sources, sa contribution et sa forme, et y ajoute les critères propres aux corpus numériques : documentation, reproductibilité, accessibilité, licences. Elle est complétée par les exigences d'intégrité intellectuelle applicables à tout travail universitaire : attribution vérifiable, respect du droit d'auteur, déclaration de l'usage de l'IA générative.

### 3. Grille

| # | Critère | Points | Question évaluée |
|---|---|---|---|
| C1 | Objet, objectifs, cohérence d'ensemble | 10 | Le projet sait-il ce qu'il est, pour qui, et son architecture le sert-elle ? |
| C2 | Cadre théologique et herméneutique | 10 | Le cadre est-il explicite, cohérent, et sa portée est-elle assumée avec distance critique ? |
| C3 | Méthode exégétique et rigueur | 20 | La méthode déclarée est-elle appliquée ? Le texte gouverne-t-il l'analyse ou le gabarit ? |
| C4 | Sources, citation, attribution, intégrité | 20 | Les affirmations sont-elles traçables ? Le droit d'auteur et la paternité sont-ils respectés ? |
| C5 | Contribution et pertinence | 10 | Qu'apporte le travail qui n'existait pas, et à qui ? |
| C6 | Forme : langue, structure, ergonomie, accessibilité | 10 | Le livrable est-il lisible, correct, cohérent, accessible ? |
| C7 | Réalisation technique, documentation, reproductibilité | 10 | Un tiers peut-il comprendre, vérifier, régénérer ? |
| C8 | Réflexivité, limites, éthique | 10 | L'auteur nomme-t-il ses limites, ses risques, ses choix ? |

Descripteurs de niveau, par critère : Excellent (≥ 90 % des points), Très bien (80 à 89), Bien (70 à 79), Passable (60 à 69), Insuffisant (< 60).

Échelle lettrée indicative, d'usage courant dans les universités québécoises : A+ ≥ 90 ; A 85-89 ; A- 80-84 ; B+ 76-79 ; B 73-75 ; B- 70-72 ; C+ 66-69 ; C 63-65 ; C- 60-62 ; D+ 55-59 ; D 50-54 ; E < 50.

### 4. Méthode d'examen

**Ce qui a été lu intégralement :** `README.md`, `gauntlet-log.md`, les deux `SKILL.md` et `commentary-sources.md`, `pdf_utils.py`, l'en-tête des scripts d'extraction, l'index racine, la structure et le pied des 8 pages Vision et Mission, la mémoire de projet de l'auteur.

**Échantillon qualitatif lu en entier ou en grande partie :** recherche Matthieu 3.1-12 ; recherche Genèse 3.1-13 (exposition) ; recherche Jacques 2.14-26 (thèmes, pistes) ; recherche Romains 9.1-5 (exposition, mots) ; recherche Apocalypse 14 (exposition) ; recherche globale et série Genèse 1-11 ; série Psaume 119 (version `4 - Sermon`).

**Vérifications automatisées sur l'ensemble :** structure des 886 recherches ; résolution des 5 578 liens internes des 925 pages ; attributs d'accessibilité ; dates des livrables ; présence d'un appareil de références ; chronologie Git ; en-têtes et mentions légales des PDF de référence.

**Vérifications ponctuelles :** une citation biblique (Mt 3.9) contre `NEG - Matthieu.md` ; les attributions de Matthieu 3.1-12 contre `JMA - Matthieu.md` ; la divergence source/export sur Genèse.

**Non fait, et donc hors de portée des jugements ci-dessous :** lecture des 4,2 M de mots ; vérification contre les sermons gty.org ; contrôle lexicographique du grec et de l'hébreu au-delà d'un sondage ; rendu des pages dans un navigateur ; lecture des `.docx` et `.pptx` du dossier `Puritains`.

Les chiffres donnés sont exacts sur l'ensemble du corpus quand ils viennent d'une vérification automatisée. Les jugements de qualité rédactionnelle et exégétique reposent sur l'échantillon nommé ci-dessus (7 documents sur 946), et sont présentés comme tels.

---

## Partie II : fiche signalétique

| Élément | Valeur |
|---|---|
| Dépôt | github.com/agbruneau/CoramDeo, **public**, sans fichier `LICENSE` |
| Période de production | 30 mai au 8 septembre 2026 ; 177 commits (8 en mai, 80 en juin, 28 en juillet, 50 en août, 11 en septembre) |
| Fichiers suivis | 2 980 : 1 016 `.md`, 954 `.pdf`, 929 `.html`, 62 images, 6 `.py`, 4 polices, 2 `.docx`, 2 `.pptx` |
| Corpus exégétique | 886 péricopes (848 NT sur 27 livres, 38 AT sur Genèse 1-11, Psaumes 19 et 119) ; par recherche : min 1 891, médiane 3 149, max 4 119 mots |
| Sources de référence embarquées | `NEG - MacArthur.pdf` (2 216 pages, 32 Mo) ; 30 fichiers `NEG - <Livre>.md` (197 218 mots) ; 30 fichiers `JMA - <Livre>.md` (527 538 mots) ; `Vallée de la Vision.pdf` (434 pages) |
| Audit doctrinal déclaré | Vision et Mission : complet (7 pages). Pérégrination : Genèse 1-11 complet, triage par signature sur le reste ; **903 pages non auditées** selon l'auteur |
| Cadre confessionnel | Confession de foi EBC (rév. 2016), théologie de John MacArthur ; lentille unique déclarée |

---

## Partie III : évaluation par critère

### C1. Objet, objectifs, cohérence d'ensemble : 8 / 10 (Très bien)

**Constats.** L'objet est défini sans ambiguïté dès la première ligne du README : une ressource d'étude biblique, de doctrine et de préparation de prédication pour une église locale nommée, dans un cadre confessionnel nommé. L'architecture en trois volets (ce que nous croyons, ce que devient le racheté, l'exposition suivie du texte) est logique, et l'index racine la reflète : Vision, Mission, puis le corpus par sections canoniques. La couverture du Nouveau Testament est réellement complète : 27 livres, chaque livre recomposé de son premier à son dernier verset, ce que la structure des dossiers permet de constater (`40 - Matthieu` : 89 péricopes de 1.1 à 28.20).

Le périmètre est maîtrisé : l'Ancien Testament n'est pas prétendu couvert ; trois séries seulement, présentées comme telles.

**Forces.** Clarté du destinataire ; cohérence des trois volets ; navigation aller-retour effective (5 578 liens internes, 0 brisé).

**Faiblesses.** Le volet `4 - Sermon` existe dans le dépôt (6 fichiers, dernier commit du 1er septembre) mais n'est nulle part décrit : il contredit la table des trois volets. Le README annonce 2 pages Vision ; il y en a 4 (Bibliologie et Pneumatologie ajoutées sans mise à jour). Ces écarts sont documentaires, non structurels, et sont repris en C7.

### C2. Cadre théologique et herméneutique : 6 / 10 (Passable)

**Constats.** Le cadre est exposé de façon exemplaire dans sa clarté : la section « Cadre théologique » du README et la « Posture théologique » de `sermon-research/SKILL.md` déclarent positivement chaque locus (bibliologie, sotériologie, pneumatologie, ecclésiologie, eschatologie) et nomment l'arbitre en cas de divergence. L'herméneutique est grammatico-historique littérale, l'exposition suivie est le modèle normatif. La cohérence entre la confession de l'Église (prémillénarisme prétribulationniste, six jours littéraux) et le cadre MacArthur est réelle, vérifiée sur le texte de la confession.

La hiérarchie des sources (six niveaux, du sermon Grace to You à la lacune déclarée) est une contribution méthodologique sérieuse : elle reconnaît que le corpus MacArthur est clos, inégal et parfois contradictoire avec lui-même, ce que le journal d'audit documente sur sept points de Genèse.

**Faiblesses.** Du point de vue universitaire, le cadre est une **contrainte confessionnelle, non un cadre théorique**. Il est explicite, mais il exclut par conception toute position concurrente : « aucun cadre concurrent n'est présenté, pondéré, ni cité pour être réfuté ». Ce choix est légitime pour une ressource d'église ; il prive le travail de la distance critique qu'exige une évaluation académique. Trois conséquences concrètes :

1. Les lectures contestées (Genèse 6.1-4, la cessation des dons, l'enlèvement prétribulationniste, les 144 000 d'Apocalypse 7 et 14) sont exposées comme « le sens du texte » sans que le lecteur sache qu'elles sont minoritaires dans l'exégèse contemporaine, y compris évangélique.
2. La lentille unique fait dépendre la validité de tout le corpus de la fiabilité de l'attribution à MacArthur, ce qui reporte tout le poids sur C4, où le travail est le plus faible.
3. Le cadre ne justifie pas ses propres fondements : pourquoi MacArthur plutôt que la confession elle-même comme arbitre, alors que la confession est le standard ecclésial ? Le README dit que MacArthur « tranche » ; une confession de foi révisée en 2016 devrait logiquement primer sur un auteur.

### C3. Méthode exégétique et rigueur : 12 / 20 (Passable)

**Constats vérifiés sur les 886 recherches.**

| Élément du gabarit | Résultat |
|---|---|
| Sept sections dans l'ordre (contexte, arrière-plan, mots-clés, apports, renvois, thèmes, pistes) | 886 / 886 |
| Lignes du tableau de mots-clés | min 4, médiane 5, max 6 |
| Renvois | min 7, médiane 8, max 9 |
| Thèmes théologiques | min 4, médiane 5, max 5 |
| Traductions comparées (S21, NEG79, Darby, LSG, KJF) | présentes dans le tableau de chaque échantillon lu |

**Ce qui tient.** La méthode déclarée dans le README (« Gabarit d'une recherche exégétique ») est appliquée uniformément. Les échantillons lus sont d'une qualité rédactionnelle et exégétique honnête : Matthieu 3.1-12 situe correctement la péricope, distingue les trois baptêmes du v. 11, articule repentance et foi ; Genèse 3.1-13 reconstruit la stratégie du tentateur en quatre temps et distingue la tromperie d'Ève de la transgression d'Adam avec renvoi à 1 Tm 2.14 et Rm 5 ; Romains 9.1-5 pose le contrepoids pastoral à l'élection avant de l'exposer ; les pistes de réflexion de Jacques 2.14-26 sont réellement taillées sur le passage et non génériques. La citation biblique contrôlée (Mt 3.9) est exacte au mot près contre le texte NEG embarqué.

**Ce qui ne tient pas.**

1. **Le gabarit gouverne, pas le texte.** Une variation de 4 à 6 mots-clés, 7 à 9 renvois et 4 à 5 thèmes sur 886 péricopes de longueurs et de genres très différents (généalogie de Matthieu 1, Philémon, Apocalypse 14) n'est pas le résultat d'une analyse conduite par le texte : c'est la signature d'une génération par gabarit à paramètres fixes. Une méthode exégétique honnête produit des sorties de tailles inégales.
2. **Les séries contredisent la méthode déclarée.** Les 30 fichiers `Serie.md` contiennent tous « Propositions de titre » avec slogans, « Arc narratif de la série » et « Recommandation pour le lancement ». Or le skill `sermon-series` du même dépôt interdit explicitement ces trois éléments (« options de titres pour bannière », « arc émotionnel », « stratégie de lancement ») comme relevant du « pragmatisme de croissance d'église ». Aucune des 30 séries ne contient la « base du découpage » par unité, la « carte doctrinale » ni les « textes exigeants » que le skill exige. Seule la série Psaume 119 refaite dans `4 - Sermon` (1er septembre) suit la méthode déclarée. Le corpus a donc été produit avec une méthode que l'auteur a ensuite désavouée, sans reprise.
3. **Aucun niveau de source n'est déclaré.** Le skill rend `source_level` obligatoire et impose le « protocole de lacune » (ne jamais écrire « MacArthur enseigne que » sans source de niveau 1 à 4). Sur 886 recherches : 0 mention de niveau, 0 lien de sermon, 0 occurrence de « gty ». Pour l'Ancien Testament, où l'auteur reconnaît lui-même que « sur bien des textes il n'y a pas de sermon MacArthur », les 38 recherches attribuent pourtant des lectures à MacArthur sans dire de quel niveau elles viennent.
4. **Pas de travail sur les langues originales au-delà de la translittération.** Les tableaux donnent translittération, sens littéral, champ sémantique ; aucune discussion de variante textuelle, de syntaxe, de forme verbale, d'usage dans la LXX. C'est une étude de mots de niveau lexique de poche, non d'exégèse universitaire. Le sondage sur Romains 9.1-5 (anathema, lupe, huiothesia, diathekai, theos eulogetos) ne montre pas d'erreur, mais pas de profondeur non plus.
5. **La rigueur de l'audit est réelle mais confinée.** Le gauntlet (bâtisseur, critique, juge à l'aveugle en ordre alterné) est une méthode de contrôle sérieuse et bien conçue. Elle a été appliquée à 7 pages sur 8 en Vision et Mission et à 13 pages sur 916 en Pérégrination. L'auteur écrit lui-même que le triage par signature sur les 903 autres « ne détecte que des erreurs affirmées » et que le mode d'échec dominant, la mésattribution, « ne se grep pas ».

### C4. Sources, citation, attribution, intégrité : 5 / 20 (Insuffisant)

C'est le critère qui décide de la recevabilité académique, et c'est celui où le travail échoue.

**4.1 Absence d'appareil de références.** Sur 886 recherches : 0 note de bas de page, 0 numéro de page, 0 référence à un volume du *MacArthur New Testament Commentary*, 0 code de sermon. Le nom « MacArthur » apparaît en moyenne 15,6 fois par recherche, soit environ 13 800 attributions dans le corpus, aucune n'étant rattachée à une source localisable. Les 4 pages Vision citent *Théologie systématique* une seule fois, dans le pied de page, sans aucune page ; or la structure de la page Bibliologie (inspiration, autorité, inerrance, préservation, obligations : recevoir, prier, s'en nourrir, obéir, honorer, étudier, prêcher, contraindre, faire des disciples, trembler) reprend chapitre par chapitre celle de l'ouvrage. Ce sont des condensés d'un manuel protégé, présentés sans pagination. Dans un travail universitaire, cela seul entraîne le renvoi pour révision.

**4.2 Qualité de l'attribution, sur échantillon.** La recherche Matthieu 3.1-12 a été confrontée note par note à `JMA - Matthieu.md`. Résultat : la paraphrase des notes de la Bible d'étude est fidèle et souvent littérale (désert de Judée et Esséniens, six mille pharisiens, prosélytes, trois baptêmes). Mais plusieurs phrases attribuées à MacArthur vont au-delà de la note : « opérée à la conversion et non comme une seconde expérience postérieure », « ce dernier mot interdit tout universalisme ». Ces extrapolations sont conformes à la théologie de MacArthur ; elles ne sont pas dans la source consultée. C'est exactement le mode d'échec que l'auteur a lui-même identifié sur Genèse (10 mésattributions sur 246 attributions vérifiées, soit 4 %). Extrapolé au corpus, sans prétendre à la précision, cela représente plusieurs centaines d'énoncés attribués à MacArthur qu'il n'a pas formulés.

**4.3 Droit d'auteur.** Le dépôt public contient :

- `NEG - MacArthur.pdf`, 2 216 pages, dont la page 2 porte : « Ce document est destiné à votre strict usage personnel [...] de ne pas le copier ni le transférer à qui que ce soit [...] Toute duplication du contenu de ce document ou d'une partie de son contenu [est] strictement interdite. Toute citation de 500 mots ou plus [...] est soumise à une autorisation écrite de La Maison de la Bible. »
- 30 fichiers `JMA - <Livre>.md`, soit 527 538 mots de notes d'étude extraites de ce PDF, et 30 fichiers `NEG - <Livre>.md`, soit 197 218 mots du texte biblique NEG 1979, lui aussi sous droits de la Société Biblique de Genève.
- `Vallée de la Vision.pdf`, 434 pages, « © 2023 Publications Chrétiennes Inc. Tous droits réservés. [...] Pour usage personnel seulement. »

Le README présente ces fichiers comme « source qui tranche la conformité doctrinale » et documente les scripts qui les régénèrent. Il ne s'agit donc pas d'un oubli mais d'une architecture qui repose sur la redistribution publique de deux ouvrages entiers. Aucun fichier `LICENSE` ne précise par ailleurs les droits sur le contenu produit. Dans un cadre universitaire, ce point est bloquant indépendamment de tout le reste.

**4.4 Paternité et usage de l'IA générative.** Le README signe : « Recherches et séries signées AGB · EBC ». Les skills fixent « L'auteur est toujours André-Guy Bruneau ». Or :

- 915 des 916 recherches et introductions sont datées de juin 2026 ; les commits du 15, 16 et 17 juin ajoutent respectivement 379, 592 et 385 fichiers (« Luc », « 15 épîtres d'une saison », « Jalon J3 »). Quinze épîtres en une journée n'est pas un rythme de rédaction humaine.
- 91 des 177 messages de commit mentionnent Claude ou portent une ligne `Co-Authored-By` ; deux des trois demandes de tirage viennent de branches `claude/…`.
- Les deux skills sont des instructions de génération, et le journal d'audit décrit des « bâtisseurs », « critiques » et « juges » qui sont des agents.

Le travail est donc, pour l'essentiel, généré par un modèle de langage sous la direction de l'auteur, avec un contrôle humain réel mais partiel (13 + 7 pages auditées en profondeur). Rien dans le README, les pages ou les PDF ne le déclare. Toute politique universitaire actuelle sur l'IA générative exige cette déclaration, et la plupart exigent aussi que l'étudiant puisse rendre compte de chaque affirmation. La signature « AGB » sur 886 recherches non relues individuellement n'est pas soutenable comme paternité académique.

**Ce qui est correct :** les sources sont nommées globalement (bibliographie du README, pied de page des pages) ; la citation biblique contrôlée est exacte ; le texte biblique de référence est identifié ; le journal d'audit déclare loyalement ses limites.

### C5. Contribution et pertinence : 6 / 10 (Passable)

**Contribution réelle.**

1. Il n'existait pas, en français, de corpus de recherche exégétique couvrant les 27 livres du Nouveau Testament péricope par péricope dans une tradition confessionnelle unique, gratuit et hors ligne. Pour l'église destinataire, la valeur d'usage est élevée : un prédicateur y trouve pour chaque dimanche un dossier structuré, dans une langue soignée, adapté à des lecteurs aînés (grands caractères, interligne aéré, ce que le CSS commente explicitement).
2. **La méthode d'audit est la contribution la plus originale du dépôt.** La boucle bâtisseur / critique / juge à l'aveugle avec ordre alterné, la typologie des modes d'échec (omission en théologie systématique, mésattribution en exposition), la constatation que « la signature d'erreurs affirmées » donne 109 déclenchements pour un seul écart réel, et l'échelle de sources à six niveaux avec protocole de lacune : tout cela est transférable à d'autres corpus confessionnels et mériterait une publication méthodologique en soi.
3. L'outillage d'extraction (séparation texte biblique / notes par police, taille et région) est un travail technique correct et documenté.

**Limites de la contribution.**

- Le contenu est **dérivé par conception** : paraphrase de MacArthur, condensé de *Théologie systématique*, plan de *The Redeemed Man*. Aucune thèse propre, aucune lecture nouvelle, aucun dialogue avec la recherche. Le README le revendique (« la seule lentille de MacArthur »), ce qui est honnête, mais borne la contribution scientifique à zéro.
- La contribution méthodologique n'est appliquée qu'à 2 % du corpus exégétique.

### C6. Forme : langue, structure, ergonomie, accessibilité : 7 / 10 (Bien)

**Langue.** Le français est de bonne tenue dans tout l'échantillon : phrases construites, vocabulaire théologique juste, aucun anglicisme, aucun mojibake sur les 1 945 fichiers texte contrôlés, aucun tiret cadratin dans les 886 recherches (règle déclarée et tenue). Le registre est homogène.

**Incohérences.** « oeuvre » (597 fichiers) coexiste avec « œuvre » (266 fichiers), de même « coeur » et « cœur », parfois dans un même document. Le README a un décalage de nomenclature avec le dépôt : `0 - Avant-propos` pour `00 - Avant-propos`, `4 - Fin` pour `4 - Héritage`, `HistoireBible.md` annoncé mais supprimé (commit `f2ef0d5`), 923 pages annoncées pour 925 réelles.

**Structure et ergonomie.** Système visuel unique sur 925 pages, barre de progression, navigation escamotable, sommaire en cartes, pied de page avec source. Aucune dépendance externe ; les 925 pages fonctionnent hors ligne, ce qui a été vérifié sur les URL présentes (seules `ebcharlesbourg.com`, `ftscriptura.com` et l'espace de noms SVG apparaissent).

**Accessibilité.** Points positifs : `lang="fr"` sur les 925 pages, `prefers-reduced-motion` respecté sur les 925 pages, contraste élevé, taille de police adaptée aux aînés, `focus-visible` stylé. Points négatifs : **2 793 liens dont le seul contenu est une image avec `alt=""`**, soit les logos de l'Église et de la Faculté en tête et en pied de chaque page. Un lecteur d'écran annonce ces liens sans nom. C'est une non-conformité WCAG 2.4.4 sur toutes les pages, corrigeable en une passe. Aucune page n'offre de thème clair (`prefers-color-scheme` absent sur 925 pages) ; le noir profond avec grain et vignette est un choix esthétique qui ne convient pas à tous les lecteurs aînés ni à l'impression.

### C7. Réalisation technique, documentation, reproductibilité : 6 / 10 (Passable)

**Ce qui tient.** Site statique sans étape de compilation, 0 lien brisé sur 5 578, `.gitattributes` qui corrige un vrai problème (PDF reportlab sans octet nul), `.gitignore` raisonné, scripts d'extraction commentés avec les polices et tailles utilisées, bibliothèque PDF partagée entre les deux skills, `README` détaillé (près de 20 Ko) avec anatomie d'un dossier de livre.

**Ce qui ne tient pas.**

1. **Le triplet .md / .pdf / .html n'est pas synchronisé.** Le README affirme que « le `.md` est la source rédigée et le `.pdf` en est l'export ». Or le commit d'audit `2cf6eba` (25 août) modifie 13 `index.html` de Genèse et aucun `.md` ni `.pdf`. Vérification directe : la recherche globale de Genèse en `.md` attribue encore à MacArthur « un nuage de vapeur d'eau enveloppant le globe [...] expliquant les longévités », thèse que le journal d'audit classe comme mésattribution corrigée (Whitcomb et Morris, non MacArthur). Le `.md` et le `.pdf` datent du 22 août, le `.html` du 25. Pour Genèse, trois formats disent deux choses différentes ; le lecteur du PDF reçoit la version fautive.
2. **La génération n'est pas reproductible depuis le dépôt.** Les JSON intermédiaires sont supprimés par protocole ; les skills actuels ne produisent plus le format des 886 recherches existantes (absence de `source_level`, de `sermon_links`) ; aucun script ne régénère un `index.html` de péricope depuis son `.md`. Un tiers ne peut ni reconstruire ni mettre à jour le corpus.
3. **Documentation obsolète** : voir C1 et C6. S'y ajoutent des liens du README vers des dossiers renommés.
4. **Aucun test, aucune intégration continue, aucune vérification automatisée des liens ou de la structure**, alors que le corpus s'y prête parfaitement (les contrôles faits pour cette évaluation ont pris quelques secondes).
5. **Poids** : 225 Mo pour Pérégrination, dont 954 PDF versionnés en binaire et un PDF de 32 Mo ; chaque régénération de PDF alourdit l'historique.
6. **Pas de `LICENSE`.**

### C8. Réflexivité, limites, éthique : 6 / 10 (Passable)

**Réflexivité : forte.** `gauntlet-log.md` est le document le plus solide du dépôt sur ce plan. Il fixe le plafond de budget avant de lancer, déclare la « limite honnête de l'aveugle » (six versions révisées sur sept sont plus longues), consigne deux corrections de méthode contre lui-même (« la borne source non récupérable était fausse », « le corpus MacArthur se contredit lui-même ») et termine sur « 903 pages non auditées ». Les skills codifient un « protocole de lacune » qui préfère « un livrable honnête au niveau ∅ » à « un livrable confiant et inventé ». C'est une posture rare et à saluer.

**Éthique : absente sur les deux points qui comptent.** Aucune réflexion sur la redistribution publique de deux ouvrages protégés ni sur la déclaration de l'IA générative. Le README signe « AGB » et parle de « recherches signées » là où le journal parle de « bâtisseurs » et de « 26 agents ». Les deux textes coexistent dans le même dépôt sans que l'un rende compte de l'autre.

**Limites : partiellement nommées.** Le journal nomme la limite de l'audit ; le README ne la répercute pas. Un lecteur qui n'ouvre que le site croit lire 916 pages « conformes à la théologie de John MacArthur » alors que l'auteur sait que 903 n'ont pas été vérifiées contre la mésattribution.

---

## Partie IV : constats transversaux

**T1. Un corpus généré, un contrôle humain partiel, une signature humaine intégrale.** C'est le nœud du dossier. La méthode de génération est sophistiquée et le contrôle est mieux pensé que dans la plupart des projets comparables, mais l'échelle (886 recherches en juin) dépasse ce qui a été relu, et rien ne le dit au lecteur.

**T2. Le dépôt contient deux méthodes qui se contredisent.** Les skills actuels (rédigés fin août, début septembre) décrivent une méthode plus exigeante que celle qui a produit le corpus (juin). Les 30 séries violent les interdits du skill `sermon-series`. Les 886 recherches ignorent l'obligation de `source_level` du skill `sermon-research`. Le dépôt documente une norme qu'il ne respecte pas.

**T3. La conformité doctrinale est affirmée partout et vérifiée sur 2 % du corpus.** Le README, chaque page et chaque PDF affirment la conformité. Le journal la restreint à 20 pages. L'affirmation devrait suivre la vérification, pas la précéder.

**T4. La source d'autorité est distribuée en violation de sa licence.** Le cœur de la méthode (vérifier l'attribution contre `JMA - <Livre>.md`) suppose la présence de ces fichiers, et leur présence dans un dépôt public est interdite par l'éditeur. La méthode est bonne ; son support est illégal tant que le dépôt est public.

**T5. Trois formats, deux contenus.** La correction des erreurs a été faite sur le HTML seul. Le format que le prédicateur imprime (PDF) est celui qui n'a pas été corrigé.

---

## Partie V : recommandations, par priorité

**P0. Bloquant avant tout dépôt ou toute diffusion académique.**

1. Retirer du dépôt public `NEG - MacArthur.pdf`, `Vallée de la Vision.pdf`, les 30 `JMA - <Livre>.md` et les 30 `NEG - <Livre>.md`, puis purger l'historique Git (les fichiers restent accessibles dans les commits antérieurs). Deux options durables : rendre le dépôt privé, ou garder ces fichiers hors dépôt et les référencer par chemin local dans les scripts. Demander l'autorisation écrite aux deux éditeurs si une forme de redistribution est voulue.
2. Ajouter au README, à chaque page et à chaque PDF une déclaration d'usage de l'IA générative : outil, rôle de l'auteur, portée du contrôle humain, pages auditées et pages non auditées.
3. Ajouter un fichier `LICENSE` pour le contenu produit.

**P1. Nécessaire pour atteindre la recevabilité académique.**

4. Doter chaque recherche d'un appareil de références : niveau de source par section « Apports », code et lien du sermon Grace to You quand il existe, référence de volume et de page pour le *NT Commentary*, référence de note (`Mt 3.7`) pour la Bible d'étude, chapitre et page pour *Théologie systématique* dans les pages Vision. Le skill actuel prévoit déjà les champs ; il reste à régénérer ou à annoter.
5. Étendre la vérification d'attribution aux 903 pages restantes selon le protocole que l'auteur a lui-même défini (relever chaque phrase qui nomme MacArthur, la confronter à la note locale puis au sermon). Le journal estime le coût : un agent par tranche de quatre pages.
6. Régénérer les `.md` et `.pdf` de Genèse (et de 1 Corinthiens 16) depuis les `.html` corrigés, ou l'inverse, et instaurer une règle : une correction touche les trois formats ou aucun.
7. Reprendre les 30 séries selon le skill `sermon-series` actuel, ou amender le skill pour qu'il reconnaisse le format existant. L'un ou l'autre, mais pas la contradiction.

**P2. Amélioration.**

8. Nommer les liens-logos (`alt="Site de l'Église Baptiste de Charlesbourg"`, etc.) sur les 925 pages ; une substitution suffit.
9. Ajouter un thème clair ou une feuille d'impression.
10. Mettre le README à jour : quatre pages Vision, `4 - Héritage`, `00 - Avant-propos`, `4 - Sermon`, retrait de `HistoireBible`, compte des pages ; y répercuter la portée réelle de l'audit.
11. Unifier « œuvre » / « cœur » (ligature) dans tout le corpus.
12. Ajouter un script de vérification (liens, structure des sept sections, présence du niveau de source, synchronisation des dates md/pdf/html) exécutable à chaque commit.
13. Sortir les PDF du dépôt Git (Git LFS ou génération à la demande) pour contenir la taille de l'historique.
14. Pour une version académique du travail : ouvrir dans chaque « texte exigeant » une note qui nomme les lectures concurrentes avant de retenir celle de MacArthur. Cela ne change pas la position ; cela restitue la distance critique.

---

## Partie VI : note globale

| Critère | Points | Note | Niveau |
|---|---|---|---|
| C1 Objet, objectifs, cohérence | 10 | 8 | Très bien |
| C2 Cadre théologique et herméneutique | 10 | 6 | Passable |
| C3 Méthode exégétique et rigueur | 20 | 12 | Passable |
| C4 Sources, citation, attribution, intégrité | 20 | 5 | Insuffisant |
| C5 Contribution et pertinence | 10 | 6 | Passable |
| C6 Forme et accessibilité | 10 | 7 | Bien |
| C7 Technique, documentation, reproductibilité | 10 | 6 | Passable |
| C8 Réflexivité, limites, éthique | 10 | 6 | Passable |
| **Total** | **100** | **56** | **D+** |

**Verdict : révision majeure requise.** En l'état, le travail n'est pas recevable comme production académique, pour deux raisons indépendantes et chacune suffisante : l'absence complète d'appareil de références sur un corpus qui attribue environ 13 800 énoncés à un auteur nommé, et la redistribution publique de deux ouvrages protégés en violation explicite de leur licence. La non-déclaration de l'IA générative s'y ajoute.

**Ce que la note ne dit pas.** Le même dépôt, jugé comme ressource pastorale pour l'église qui l'a commandé, est une réalisation d'une ampleur et d'une tenue rares : une couverture complète du Nouveau Testament, une langue soignée, un site qui fonctionne hors ligne, et surtout une méthode d'audit doctrinal dont la lucidité dépasse celle de la plupart des travaux universitaires sur l'IA appliquée aux textes religieux. La contribution méthodologique (échelle de sources, protocole de lacune, boucle de jugement à l'aveugle, typologie des modes d'échec) vaut à elle seule un article.

**Note atteignable.** Si les recommandations P0 et P1 sont exécutées (retrait des sources protégées, déclaration de l'IA, références, vérification d'attribution étendue, synchronisation des formats, alignement des séries), C4 remonterait dans la zone 14 à 16, C3 dans la zone 14 à 15, C6, C7 et C8 à 8. Le total se situerait entre 71 et 75, soit **B- à B**. Le plafond au-delà vient de C2 et C5 : la lentille unique et le caractère dérivé du contenu sont des choix de conception, cohérents avec la finalité du projet, et incompatibles avec une note d'excellence académique. Ce plafond n'est pas un défaut à corriger ; c'est la conséquence assumée d'avoir fait une ressource d'église et non une thèse.

---

## Partie VII : réévaluation après exécution de la planification (21 septembre 2026)

Les lots 0 à 8 et 10 de `Planification-execution-CoramDeo.md` ont été exécutés du 15 au 21 septembre ; le lot 9 (distance critique) a été écarté par décision D8. Le détail est dans `gauntlet-log.md`. La grille C1 à C8 est rejouée ci-dessous sur l'état du dépôt au commit de clôture du lot 7.

**Correction d'un constat de l'évaluation initiale.** Le constat P2.8 (C6, annexe B : « 2 793 liens dont le seul contenu est une image avec `alt=""` ») était un faux positif : chacun de ces liens porte un `aria-label`, et le `alt=""` de l'image est alors le motif correct. Les liens ont un nom accessible ; il n'y avait pas de non-conformité WCAG 2.4.4. La règle `liens-sans-nom` de `tools/check.py` vérifie désormais le nom accessible du lien et non l'attribut `alt`. La note initiale de C6 est corrigée en conséquence dans le tableau ci-dessous.

**Vérifications de l'annexe B, rejouées.**

| Vérification | Avant (septembre, évaluation) | Après (clôture) |
|---|---|---|
| Liens internes brisés | 0 | 0 (`check.py`, règle `liens`) |
| Sept sections du gabarit | 886 conformes | 886 conformes (HTML et `.md`) |
| Appareil de références | 0 lien de sermon, 0 niveau de source | 886 blocs « Niveau de source », dont 864 avec liens de sermons Grace to You ; 22 au niveau des notes |
| Pied « attribution vérifiée » | 0 | 886 péricopes, datées |
| Déclaration de l'IA | 0 page | 925 pages, README, PDF |
| Liens sans nom accessible | 2 793 (faux positif) | 0 |
| Feuille d'impression | 0 | 925 pages |
| `prefers-color-scheme` | 0 | 0 (inchangé) |
| Mojibake | 0 | 0 |
| « oeuvre » / « œuvre » dans les `.md` | 597 / 266 | 0 / 807 |
| Synchronisation `.html` / `.md` / `.pdf` | non (Genèse) | empreinte `source_hash` vérifiée pour les 886 péricopes et les 30 séries ; `check.py --strict` passe |
| Sources protégées dans le dépôt | 62 fichiers et 2 PDF, historique compris | 0, historique purgé ; dépôt privé |
| `LICENSE` | absent | présent |

**Grille rejouée.**

| Critère | Points | Avant | Après | Justification du delta |
|---|---|---|---|---|
| C1 Objet, objectifs, cohérence | 10 | 8 | 9 | README réécrit ; les écarts de l'annexe A sont corrigés et contrôlés (`readme-comptes`, `readme-dossiers`). |
| C2 Cadre théologique et herméneutique | 10 | 6 | 6 | Lentille unique inchangée (plafond de conception, D8). La hiérarchie des sources (le sermon prime sur la note) est désormais explicite, mais ne change pas la nature du cadre. |
| C3 Méthode exégétique et rigueur | 20 | 12 | 15 | Les extrapolations attribuées ont été corrigées sur tout le corpus ; les séries ont une base de découpage, une structure de l'argument et 166 textes exigeants. Aucune lecture concurrente n'est discutée. |
| C4 Sources, citation, attribution, intégrité | 20 | 5 | 14 | Sources protégées retirées et historique purgé ; IA déclarée partout ; `LICENSE` ; niveau de source et liens de sermons sur 886 pages ; attributions vérifiées sur les 886 péricopes et les 30 recherches globales, 85 jugements à l'aveugle gagnés par la version vérifiée. Restent : pas de référence de page pour les pages Vision (tâche 6.5 non faite, ouvrage non disponible), aucune référence de volume du *NT Commentary*, réserve D3 non levée auprès des éditeurs. |
| C5 Contribution et pertinence | 10 | 6 | 7 | La méthode d'audit, présentée comme la contribution principale, est désormais appliquée à tout le corpus exégétique, et non plus à 2 %. |
| C6 Forme et accessibilité | 10 | 7 | 8 | Ligatures unifiées, feuille d'impression ; le constat P2.8 était un faux positif. Pas de thème clair. |
| C7 Technique, documentation, reproductibilité | 10 | 6 | 8 | HTML canonique, `.md` et `.pdf` dérivés avec empreinte ; `tools/` (extraction, régénération, sources, séries, contrôle) et intégration continue. Les PDF restent versionnés en binaire. |
| C8 Réflexivité, limites, éthique | 10 | 6 | 8 | Déclaration de l'IA et portée réelle de l'audit dans le README, le pied de chaque page et le journal ; divergences de chaire laissées visibles. |
| **Total** | **100** | **56 (D+)** | **75 (B)** | |

**Verdict révisé : recevable avec révisions mineures** comme ressource documentée ; la note se situe au haut de la zone annoncée (71 à 75). Ce qui la plafonne tient aux choix de conception (C2, C5) et à trois restes : références de page pour les pages Vision, avis des éditeurs sur l'usage des sources (D3), PDF hors de l'historique Git.

**Décision de republication (tâche 10.3).** Les conditions cumulatives de D1 ne sont pas toutes remplies : les lots 1 et 2 sont terminés, mais la réserve de D3 (avis des éditeurs) n'est ni levée ni assumée par écrit. Le dépôt reste privé jusqu'à cette décision de l'auteur.

---

## Annexe A : écarts entre le README et le dépôt

| README affirme | Le dépôt contient |
|---|---|
| `1 - Vision/` : 2 pages (Christologie, Ecclésiologie) | 4 pages (Bibliologie, Christologie, Pneumatologie, Ecclésiologie) |
| `2 - Mission/4 - Fin/` | `2 - Mission/4 - Héritage/` |
| `3 - Pérégrination/0 - Avant-propos/` | `00 - Avant-propos/` |
| `HistoireBible.md` et `.pdf` décrits | supprimés au commit `f2ef0d5` |
| 923 pages `index.html` | 925 |
| Trois volets | quatre dossiers : `4 - Sermon/` non documenté |
| « le `.md` est la source, le `.pdf` son export » | Genèse : `.html` corrigé le 25 août, `.md` et `.pdf` non corrigés |
| « Recherches et séries signées AGB » | 91 commits co-signés par un agent ; 886 recherches produites en juin ; audit humain approfondi sur 20 pages |

## Annexe B : vérifications réalisées

| Vérification | Portée | Résultat |
|---|---|---|
| Résolution des liens internes (`href`, `src`) | 925 pages, 5 578 liens | 0 brisé |
| Sept sections du gabarit de recherche | 886 fichiers `.md` | 886 conformes |
| Distribution mots-clés / renvois / thèmes | 886 fichiers | 4-6 / 7-9 / 4-5 |
| Appareil de références (`gty`, `Niveau`, `source_level`, notes, pages) | 886 fichiers | 0 / 0 / 0 / 0 / 7 |
| Dates des recherches et introductions | 916 fichiers | 915 en juin 2026, 1 en mai |
| `lang="fr"`, `prefers-reduced-motion` | 925 pages | 925 / 925 |
| Liens dont le seul contenu est une image `alt=""` | 925 pages | 2 793 |
| `prefers-color-scheme` | 925 pages | 0 |
| Mojibake (`Ã©`, `Ã¨`) | 1 945 fichiers texte | 0 |
| Tiret cadratin dans les recherches | 886 fichiers | 0 |
| Ligature « œuvre » vs « oeuvre » | fichiers `.md` de Pérégrination | 266 vs 597 |
| Citation Mt 3.9 contre `NEG - Matthieu.md` | 1 verset | exacte |
| Attributions de Matthieu 3.1-12 contre `JMA - Matthieu.md` | 1 recherche | paraphrase fidèle, 2 extrapolations attribuées |
| Fichiers touchés par le commit d'audit `2cf6eba` | 14 fichiers | 13 `index.html`, 1 journal, 0 `.md`, 0 `.pdf` |
| Mentions légales des PDF de référence | 3 PDF | usage personnel strict (2), confession de foi (1) |
| Visibilité du dépôt | GitHub | public, sans `LICENSE` |
