# Sola Scriptura

Dépôt parapluie qui réunit les ressources d'étude biblique et de préparation de prédication
expositive d'André-Guy Bruneau, dans un cadre baptiste réformé conforme à la théologie de
John MacArthur, sur le texte de la Nouvelle Édition de Genève 1979 (NEG79).

Chaque projet reste un dépôt autonome, intégré ici comme **submodule git** :

| Projet | Dépôt | Contenu |
|---|---|---|
| [`CoramDeo/`](CoramDeo) | [agbruneau/CoramDeo](https://github.com/agbruneau/CoramDeo) | Ressource de l'Église Baptiste de Charlesbourg en trois volets : **Vision** (bibliologie, christologie, pneumatologie, ecclésiologie), **Mission** (Dieu, autrui, travail, héritage) et **Pérégrination** (expositions suivies : Nouveau Testament complet, 27 livres, et séries de l'Ancien Testament : Genèse 1-11, Psaumes 19 et 119). |
| [`Paulus/`](Paulus) | [agbruneau/Paulus](https://github.com/agbruneau/Paulus) | Les épîtres de Paul (et Hébreux) dans l'ordre chronologique de rédaction selon MacArthur, de Galates à Hébreux : recherches exégétiques (MD, HTML, PDF, JSON) et plans de série, plus deux synthèses sur la vie de l'apôtre. |

Le détail de chaque projet (structure, méthode, couverture, audits) est dans son propre README :
[`CoramDeo/README.md`](CoramDeo/README.md) et [`Paulus/README.md`](Paulus/README.md).

## Cloner

```bash
git clone --recurse-submodules https://github.com/agbruneau/SolaScriptura.git
```

Pour un clone déjà fait sans les submodules :

```bash
git submodule update --init
```

## Mettre à jour

Le travail se fait dans chaque projet, qui se commite et se pousse vers son propre dépôt. Ce dépôt
fixe ensuite la version référencée :

```bash
git submodule update --remote
git commit -am "Mise à jour des submodules"
```

## Production

Les recherches et les pages ont été produites avec Claude Code (Anthropic) sous la direction de
l'auteur, qui en a fixé le cadre théologique, les sources et les règles de vérification. La portée
des relectures et des audits est documentée dans chaque projet.
