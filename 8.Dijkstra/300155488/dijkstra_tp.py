# dijkstra_tp.py
from graph import Graph

# --- Création du graphe  ---



g = Graph()

# Ajout des villes
for node in ['Paris', 'London', 'New York', 'Tokyo', 'Berlin', 'Dubai']:
    g.add_vertex(node)

# Ajout des connexions (distances approximatives ou arbitraires)
g.add_edge('Paris', 'London', 400)
g.add_edge('Paris', 'New York', 800)
g.add_edge('Paris', 'Dubai', 140)

g.add_edge('London', 'New York', 100)
g.add_edge('London', 'Tokyo', 152)
g.add_edge('New York', 'Tokyo', 311)
g.add_edge('New York', 'Dubai', 100)
g.add_edge('Tokyo', 'Berlin', 600)
g.add_edge('Berlin', 'Dubai', 900)
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
start = g.get_vertex('Paris')
target = g.get_vertex('Berlin')

dijkstra(g, start)

path = shortest(target)
print("Le plus court chemin:", path)