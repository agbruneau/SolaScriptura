# Paulinisme

Ce dépôt réunit les études des treize épîtres de Paul dans l'ordre chronologique de leur rédaction selon John MacArthur (table et conventions générales dans `README.md`). Les dossiers `01 - Galates/`, `02 - 1-Thessaloniciens/` et `03 - 2-Thessaloniciens/` servent d'implémentations de référence.

## Conventions du dépôt

- **Un sermon par chapitre.** Le plan de série d'un livre compte autant de prédications que le livre compte de chapitres (`N` chapitres = `N` sermons), regroupés selon les grands blocs structurels que dégage MacArthur. Ce découpage par chapitre prime sur le découpage par péricopes de la skill `sermon-series`.
- **Charnières.** Lorsqu'une unité de pensée du texte ou un sermon Grace to You (GTY) enjambe une frontière de chapitre (p. ex. `Galates 1.11-2.10` ou `1 Thessaloniciens 2.17-3.13`), la recherche et le plan en rendent compte dans l'introduction et la transition des chapitres concernés.
- **Dossiers numérotés.** Chaque livre vit dans `<Rang> - <Livre>/`, où `<Rang>` (sur 2 chiffres) est sa place dans la table chronologique de `README.md` (p. ex. `05 - 2 - Corinthiens/`). Le préfixe ne touche que le nom du dossier : sous-dossiers et fichiers gardent le slug du livre (`01-Galates-1/`, `Plan-Serie-Galates-1-6.md`). La skill `etude-livre` parle de `<Livre>/`; passer le chemin numéroté à `--book-dir` et aux autres options de chemin. Dans les liens Markdown, entourer ces chemins de chevrons à cause des espaces : `[index](<01 - Galates/index.html>)`.
- **Livrables (`4 × N + 7` fichiers par dossier `<Rang> - <Livre>/`).** Recherche globale dans `Sommaire/`, recherches par chapitre dans `01-<Livre>-1/` à `<pad(N)>-<Livre>-<N>/` (le `.json` est l'unique source de vérité), plan de série `Plan-Serie-<Livre>-<Plage>.{md,pdf}` et portail autonome `index.html`.
- **Production et vérification.** Utiliser la skill locale `etude-livre` (`.agents/skills/etude-livre/SKILL.md` et son outil CLI `.agents/skills/etude-livre/scripts/etude_livre.py`), puis mettre à jour la table chronologique de `README.md`.
