# INF1093 - Programmation 2 - Dijkstra
# Souleymane Barry - 300141685
# Fichier: dijkstra_tp.py

from graph import Graph

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

print("=" * 50)
print("GRAPHE - LISTE DES ARETES")
print("=" * 50)
for v in g:
    for w in v.get_connections():
        print(f"( {v.get_id()} , {w.get_id()} , {v.get_weight(w):3d} )")

print("\n" + "=" * 50)
print("ALGORITHME DE DIJKSTRA")
print("=" * 50)

def dijkstra(aGraph, start):
    start.set_distance(0)
    unvisited = [v for v in aGraph]

    while unvisited:
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
                print(f"MISE A JOUR: {current.get_id()} -> {neighbor.get_id()} (distance: {neighbor.get_distance()})")
            else:
                print(f"PAS DE MAJ: {current.get_id()} -> {neighbor.get_id()} (distance actuelle: {neighbor.get_distance()})")

def shortest(v):
    path = [v.get_id()]
    while v.previous:
        v = v.previous
        path.append(v.get_id())
    return path[::-1]

start = g.get_vertex('a')
target = g.get_vertex('e')

print(f"\nDepart: {start.get_id()}")
print(f"Cible: {target.get_id()}\n")

dijkstra(g, start)

print("\n" + "=" * 50)
print("RESULTAT FINAL")
print("=" * 50)
path = shortest(target)
print(f"Le plus court chemin de {start.get_id()} a {target.get_id()}: {path}")
print(f"Distance totale: {target.get_distance()}")
