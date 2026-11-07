# Sola Scriptura

Dépôt qui réunit les ressources d'étude biblique et de préparation de prédication expositive
d'André-Guy Bruneau, dans un cadre baptiste réformé conforme à la théologie de John MacArthur,
sur le texte de la Nouvelle Édition de Genève 1979 (NEG79).

| Projet | Contenu |
|---|---|
| [`CoramDeo/`](CoramDeo) | Ressource de l'Église Baptiste de Charlesbourg en trois volets : **Vision** (bibliologie, christologie, pneumatologie, ecclésiologie), **Mission** (Dieu, autrui, travail, héritage) et **Pérégrination** (expositions suivies : le Nouveau Testament au complet, 27 livres, et des séries de l'Ancien Testament : Genèse 1-11, Psaumes 19 et 119). Point d'entrée : [`CoramDeo/index.html`](CoramDeo/index.html). |
| [`Paulus/`](Paulus) | Les épîtres de Paul (et Hébreux), dans l'ordre chronologique de rédaction selon MacArthur, de Galates à Hébreux : recherches exégétiques (MD, HTML, PDF, JSON) et plans de série, plus deux synthèses sur la vie de l'apôtre. |

Le détail de chaque projet (structure, méthode, couverture, audits) se trouve dans son propre
README : [`CoramDeo/README.md`](CoramDeo/README.md) et [`Paulus/README.md`](Paulus/README.md).

## Origine des dossiers

Les deux dossiers ont été intégrés en entier le 7 novembre 2026, à partir des dépôts
[agbruneau/CoramDeo](https://github.com/agbruneau/CoramDeo) et
[agbruneau/Paulus](https://github.com/agbruneau/Paulus), où leur historique antérieur est
conservé. Ils sont désormais maintenus ici.

Les `.gitignore` de chaque dossier continuent de s'appliquer. Les sources protégées de CoramDeo
(licence d'usage personnel) restent hors dépôt. Le workflow
`CoramDeo/.github/workflows/check.yml` ne s'exécute pas depuis un sous-dossier : GitHub Actions
ne lit que le `.github/` à la racine.

## Production

Les recherches et les pages ont été produites avec Claude Code (Anthropic) sous la direction de
l'auteur, qui en a fixé le cadre théologique, les sources et les règles de vérification. La portée
des relectures et des audits est documentée dans chaque projet.
