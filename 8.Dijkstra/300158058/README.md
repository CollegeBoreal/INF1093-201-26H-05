# Projet Dijkstra – INF1093

**Nom :** BELAID Rabah  
**ID :** 300158058  

## Fichiers du projet
Ce projet contient les fichiers suivants :
- `graph.py`
- `dijkstra_tp.py`
- `check_results.py`
- `RAPPORT.ipynb`
- `images/`

## Description
Le but de ce travail est de représenter un graphe pondéré en Python
et d’utiliser l’algorithme de Dijkstra pour trouver le plus court chemin
entre un sommet de départ et un sommet d’arrivée.

## Contenu
- `graph.py` contient les classes `Vertex` et `Graph`
- `dijkstra_tp.py` crée le graphe, exécute Dijkstra et affiche le résultat
- `check_results.py` vérifie si le chemin et la distance obtenus sont corrects
- `RAPPORT.ipynb` montre une visualisation simple du graphe et du chemin minimal

## Exécution
```bash
python dijkstra_tp.py
python check_results.py
```

## Résultat attendu
Dans cette version, le plus court chemin calculé de `A` à `G` est :

`A -> C -> F -> G`

avec une distance totale de `14`.
