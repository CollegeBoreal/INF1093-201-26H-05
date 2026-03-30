# dijkstra_tp.py
from graph import Graph

# --- Création du graphe avec des villes ---
g = Graph()
for node in ['Paris', 'Londres', 'Berlin', 'Madrid', 'Rome', 'Bruxelles']:
    g.add_vertex(node)

# --- Connexions et distances ---
g.add_edge('Paris', 'Londres', 7)
g.add_edge('Paris', 'Berlin', 9)
g.add_edge('Paris', 'Bruxelles', 14)
g.add_edge('Londres', 'Berlin', 10)
g.add_edge('Londres', 'Madrid', 15)
g.add_edge('Berlin', 'Madrid', 11)
g.add_edge('Berlin', 'Bruxelles', 2)
g.add_edge('Madrid', 'Rome', 6)
g.add_edge('Rome', 'Bruxelles', 9)

# --- Affichage du graphe ---
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
target = g.get_vertex('Rome')

dijkstra(g, start)

path = shortest(target)
print("Le plus court chemin:", path)