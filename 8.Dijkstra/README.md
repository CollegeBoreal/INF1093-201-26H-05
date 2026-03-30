# 📉 Dijkstra

[🎉 Participations](.scripts/Participations.md)

## 🐍 :a: On crée trois fichiers : 

- `graph.py`,
- `dijkstra_tp.py` et
- `check_results.py`.

## 🧾 :n: `RAPPORT.ipynb` – Visualisation du graphe

Créer un fichier `RAPPORT.ipynb` permettant de :

* Reproduire le graphe utilisé dans `dijkstra_tp.py`
* **Afficher visuellement le graphe sous forme de diagramme**
* Mettre en évidence le chemin le plus court (couleur différente)

💡 Vous pouvez utiliser `matplotlib` et/ou `networkx` pour la visualisation.

---

## 1️⃣ `graph.py` – Classes Vertex et Graph

```python
# graph.py
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = float('inf')   # distance initiale infinie
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return f"{self.id} adjacent: {[x.id for x in self.adjacent]}"


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        return self.vert_dict.get(n, None)

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()
```

---

## 2️⃣ `dijkstra_tp.py` – TP principal

```python
# dijkstra_tp.py
from graph import Graph

# --- Création du graphe ---
g = Graph()
for node in ['a','b','c','d','e','f']:
    g.add_vertex(node)

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

print("Graph data:")
for v in g:
    for w in v.get_connections():
        print(f"( {v.get_id()} , {w.get_id()}, {v.get_weight(w):3d} )")

# --- Dijkstra simple ---
def dijkstra(aGraph, start):
    start.set_distance(0)
    unvisited = [v for v in aGraph]

    while unvisited:
        # Choisir le sommet avec distance minimale
        current = min(unvisited, key=lambda v: v.get_distance())
        current.set_visited()
        unvisited.remove(current)

        for neighbor in current.adjacent:
            if neighbor.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(neighbor)
            if new_dist < neighbor.get_distance():
                neighbor.set_distance(new_dist)
                neighbor.set_previous(current)
                print(f"updated : current = {current.get_id()} next = {neighbor.get_id()} new_dist = {neighbor.get_distance()}")
            else:
                print(f"not updated : current = {current.get_id()} next = {neighbor.get_id()} new_dist = {neighbor.get_distance()}")

# --- Reconstruction du plus court chemin ---
def shortest(v):
    path = [v.get_id()]
    while v.previous:
        v = v.previous
        path.append(v.get_id())
    return path[::-1]

# --- Exécution ---
start = g.get_vertex('a')
target = g.get_vertex('e')

dijkstra(g, start)

path = shortest(target)
print("Le plus court chemin:", path)
```

---

## 3️⃣ `check_results.py` – Auto-correction

```python
# check_results.py
from dijkstra_tp import shortest, g

target = g.get_vertex('e')
path = shortest(target)

expected_path = ['a', 'c', 'f', 'e']

if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin:", path)
    print("Chemin attendu:", expected_path)
```

---
