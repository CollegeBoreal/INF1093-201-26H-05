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
