# 🏎️ PROJET DE PRÉDICTION DU CHAMPIONNAT CONSTRUCTEUR DE FORMULE 1

## 🎯 Objectif du projet

Ce projet vise à prédire l’écurie qui remportera le **championnat constructeur de Formule 1** à partir de données historiques.
L’objectif principal est de concevoir un **modèle de machine learning** capable d’estimer, en fonction de variables pertinentes, l’écurie ayant le plus de chances de terminer en tête du classement à la fin d’une saison.

---

## 🗂️ Données utilisées (`/data/Data_Final`)

Les données proviennent de plusieurs fichiers CSV historiques, notamment :

* `constructor_standings.csv` → contient les points, victoires et positions des écuries.
* `races.csv` → utilisé pour relier chaque course à son année (`year`).
* La **dernière course de chaque saison** est utilisée pour fixer le classement final des constructeurs.

### 🧾 Variables finales

| Variable             | Type    | Description                                                                                             |
| -------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `year`               | `int`   | Saison F1 (ex : 2022, 2023). Permet un suivi chronologique.                                             |
| `constructorId`      | `int`   | Identifiant unique de l’écurie (clé de jointure).                                                       |
| `name`               | `str`   | Nom lisible de l’écurie (ex : "Red Bull", "Ferrari").                                                   |
| `points`             | `float` | Points marqués dans la saison. Ne doit **pas être utilisée** pour l’entraînement (contient la réponse). |
| `wins`               | `int`   | Nombre de victoires. Indicateur de domination ponctuelle.                                               |
| `target`             | `0/1`   | **Variable à prédire** : 1 = vainqueur, 0 = non-vainqueur.                                              |
| `avg_driver_points`  | `float` | Moyenne des points marqués par les pilotes de l’écurie (par course).                                    |
| `avg_grid_position`  | `float` | Position moyenne de départ en qualification. Indicateur de vitesse pure.                                |
| `avg_final_position` | `float` | Position moyenne à l’arrivée. Mesure de régularité et de performance en course.                         |
| `dnf_count`          | `int`   | Nombre total de courses non terminées (DNF) par les pilotes de l’écurie. Mesure de fiabilité.           |

---

## 🧠 Interprétation de certaines variables clés

* `wins` :

  * **10 victoires** → domination claire.
  * **0 victoire** → saison plus régulière ou manquant de performance pure.

* `avg_driver_points` :

  * Indique la **performance individuelle cumulée** des pilotes.
  * Ne prend pas en compte les abandons.

* `avg_grid_position` vs `avg_final_position` :

  * Un bon différentiel positif = écurie capable de **remonter en course**.
  * Un différentiel négatif = perte de position → gestion ou fiabilité à améliorer.

* `dnf_count` :

  * Élevé = **problèmes mécaniques fréquents**, erreurs pilotes, incidents.
  * Impact négatif direct sur les chances de titre.

---

dans les pages disponible sur le site nous avons la liste des pilotes, la liste des écuries, et enfin la prediction

Travail de Hugo Mintegui et Romain Augé

