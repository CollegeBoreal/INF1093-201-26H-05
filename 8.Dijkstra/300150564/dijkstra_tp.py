# dijkstra_tp.py
from graph import Graph

# --- Création du graphe (capitales européennes) ---
g = Graph()
villes = ['Paris', 'Berlin', 'Madrid', 'Rome', 'Vienne', 'Amsterdam', 'Bruxelles', 'Prague']
for ville in villes:
    g.add_vertex(ville)

g.add_edge('Paris',     'Berlin',    1050)
g.add_edge('Paris',     'Madrid',    1270)
g.add_edge('Paris',     'Bruxelles',  305)
g.add_edge('Paris',     'Amsterdam',  480)
g.add_edge('Berlin',    'Rome',      1180)
g.add_edge('Berlin',    'Prague',     280)
g.add_edge('Berlin',    'Vienne',     680)
g.add_edge('Madrid',    'Rome',      1960)
g.add_edge('Rome',      'Vienne',    1130)
g.add_edge('Vienne',    'Prague',     290)
g.add_edge('Vienne',    'Bruxelles', 1130)
g.add_edge('Amsterdam', 'Bruxelles',  210)
g.add_edge('Bruxelles', 'Berlin',     900)

print("=== Graphe des capitales européennes ===")
for v in g:
    for w in v.get_connections():
        print(f"  {v.get_id():12s} <--> {w.get_id():12s}  {v.get_weight(w):5d} km")
# --- Algorithme de Dijkstra ---
def dijkstra(aGraph, start):
    start.set_distance(0)
    unvisited = [v for v in aGraph]

    while unvisited:
        # Choisir le sommet avec la plus petite distance
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
                print(f"  ✅ Mise à jour : {current.get_id()} → {neighbor.get_id()} = {neighbor.get_distance()} km")
            else:
                print(f"  ⏭️  Pas de maj  : {current.get_id()} → {neighbor.get_id()} = {neighbor.get_distance()} km")

# --- Reconstruction du chemin ---
def shortest(v):
    path = [v.get_id()]
    while v.previous:
        v = v.previous
        path.append(v.get_id())
    return path[::-1]

# --- Exécution : Paris → Prague ---
print("\n=== Plus court chemin : Paris → Prague ===\n")
start  = g.get_vertex('Paris')
target = g.get_vertex('Prague')

dijkstra(g, start)

path = shortest(target)
print(f"\n📍 Chemin : {' → '.join(path)}")
print(f"📏 Distance totale : {target.get_distance()} km")
