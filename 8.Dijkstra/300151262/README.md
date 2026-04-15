# Dijkstra – Réseau de métro intelligent

## 📌 Objectif
Ce projet a pour but d’implémenter l’algorithme de **Dijkstra** en Python afin de calculer le **trajet le plus rapide** entre plusieurs stations de métro, puis de vérifier automatiquement le résultat et de visualiser le graphe.

---

## 📂 Fichiers du projet

- `graph_metro.py`
- `dijkstra_metro.py`
- `check_metro.py`
- `rapport_metro.ipynb`

---

## 1️⃣ `graph_metro.py` – Structure du graphe

Ce fichier contient les classes nécessaires à la représentation du graphe :
- Sommets (stations)
- Arêtes (temps de trajet entre les stations)

---

## 2️⃣ `dijkstra_metro.py` – Implémentation principale

Ce fichier :
- Crée le graphe du réseau de métro
- Applique l’algorithme de **Dijkstra**
- Calcule les temps minimaux
- Reconstruit le plus court chemin

---

## 3️⃣ `check_metro.py` – Vérification

Ce fichier permet de :
- Tester automatiquement le résultat
- Vérifier si le chemin trouvé est correct

---

## 🧾 4️⃣ `RAPPORT.ipynb` – Visualisation

Ce notebook permet de :
- Représenter le graphe avec **NetworkX**
- Visualiser les connexions entre les stations
- Mettre en évidence le **plus court chemin**

---

## 🌍 Données utilisées

### Stations du réseau :
- **Ligne 1** : Station A, Station B, Station C
- **Ligne 2** : Station D, Station E, Station F

### Connexions et temps :
- **A → B** : 4 min
- **A → C** : 2 min
- **B → D** : 5 min
- **C → D** : 8 min
- **C → E** : 10 min
- **D → E** : 2 min
- **D → F** : 6 min
- **E → F** : 3 min

---

## ▶️ Exécution du projet

Lancer les fichiers dans cet ordre :

```bash
python dijkstra_metro.py
python check_metro.py
```

---

## ✅ Résultat attendu

Le programme affiche :
- Le temps minimal entre la station de départ et la station d’arrivée
- Le chemin le plus court trouvé par l’algorithme

Exemple :
```bash
Temps minimal : 12 minutes
Chemin le plus court : A -> B -> D -> E -> F
```

---

## 🛠️ Outils utilisés

- **Python**
- **heapq** pour la file de priorité
- **NetworkX** pour la visualisation du graphe
- **Matplotlib** pour l’affichage graphique

---

## 📚 Principe de l’algorithme de Dijkstra

L’algorithme de Dijkstra permet de trouver le plus court chemin entre un sommet de départ et tous les autres sommets d’un graphe pondéré avec des poids positifs.

Dans ce projet :
- chaque **station** est un sommet
- chaque **liaison** entre stations est une arête
- chaque **poids** représente un temps de trajet en minutes

---

## 🎯 Conclusion

Ce projet montre comment utiliser l’algorithme de Dijkstra dans un contexte réel de transport urbain. Il permet de modéliser un réseau de métro, de calculer efficacement le meilleur trajet et de visualiser le résultat sous forme de graphe.
