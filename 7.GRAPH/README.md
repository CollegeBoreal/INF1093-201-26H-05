# **Leçon : Les Graphes 📊✨**

## 1️⃣ Qu’est-ce qu’un graphe ? 🤔

Un **graphe** est une structure pour représenter des **relations entre objets**.

* **Sommets (nœuds)** 🟢 : les objets eux-mêmes.
* **Arêtes (liens)** 🔗 : les relations entre ces objets.

### Exemple concret :

* Réseau social : chaque personne = 🟢, amitié = 🔗
* Carte routière : chaque ville = 🟢, route = 🔗

```
Alice 🟢 — Bob 🟢 — Charlie 🟢
```

---

## 2️⃣ Types de graphes 🧩

1. **Graphe non orienté** 🔗

   * Les liens n’ont pas de sens particulier.
   * Ex : amitié mutuelle

```
A 🟢 — B 🟢
B 🟢 — C 🟢
```

2. **Graphe orienté (digraphe)** ➡️

   * Les liens ont un sens (flèche).
   * Ex : Fans (A suit B, mais B ne suit pas forcément A)

```
A 🟢 → B 🟢 → C 🟢
```

3. **Graphe pondéré** ⚖️

   * Chaque lien a un **poids** (distance, coût, temps…).
   * Ex : carte routière avec distances

```
A 🟢 —5km— B 🟢
B 🟢 —10km— C 🟢
```

---

## 3️⃣ Représentation des graphes 🖥️

### a) Liste d’adjacence 📋

* Chaque sommet garde la **liste de ses voisins**.
* Pratique si le graphe est **peu dense**.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
```

### b) Matrice d’adjacence 🟦

* Tableau 2D où `mat[i][j] = 1` si une arête existe.
* Pratique pour graphes **denses**.

```
   A B C D
A [0 1 1 0]
B [1 0 0 1]
C [1 0 0 1]
D [0 1 1 0]
```

---

## 4️⃣ Parcours de graphes 🔍

### a) DFS – profondeur 🏔️

* Explore **le plus loin possible** avant de revenir.
* Utilise **pile** ou **récursion**.

```python
def dfs(graph, start, visited=set()):
    visited.add(start)
    print(start, "🟢")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### b) BFS – largeur 🌊

* Explore **tous les voisins d’abord**.
* Utilise **file (queue)**.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, "🟢")
            visited.add(node)
            queue.extend(graph[node])
```

---

## 5️⃣ Applications des graphes 🌐🚀

* Réseaux sociaux : 👥 amis, suggestions
* GPS et cartes : 🚗 chemin le plus court
* Internet : 🌍 liens entre pages web
* Jeux / IA : 🎮 navigation et puzzles

---

## 6️⃣ Concepts importants 💡

* **Degré d’un sommet** 🎯 : nombre de liens connectés
* **Cycle** 🔄 : chemin qui revient au départ
* **Connexité** 🔗 : tous les sommets sont atteignables
* **Arbre** 🌳 : graphe sans cycle

