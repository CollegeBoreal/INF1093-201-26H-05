# dijkstra_tp.py
from graph import Graph

# --- Création du graphe avec des villes ---
g = Graph()
for node in ['Toronto', 'Montreal', 'Ottawa', 'Quebec', 'Halifax', 'Calgary']:
    g.add_vertex(node)

g.add_edge('Toronto', 'Montreal', 7)
g.add_edge('Toronto', 'Ottawa', 9)
g.add_edge('Toronto', 'Calgary', 14)
g.add_edge('Montreal', 'Ottawa', 10)
g.add_edge('Montreal', 'Quebec', 15)
g.add_edge('Ottawa', 'Quebec', 11)
g.add_edge('Ottawa', 'Calgary', 2)
g.add_edge('Quebec', 'Halifax', 6)
g.add_edge('Halifax', 'Calgary', 9)

print("Graph data:")
for v in g:
    for w in v.get_connections():
        print(f"( {v.get_id()} , {w.get_id()}, {v.get_weight(w):3d} )")

# --- Dijkstra ---
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
                print(f"updated : {current.get_id()} → {neighbor.get_id()} = {neighbor.get_distance()}")
            else:
                print(f"not updated : {current.get_id()} → {neighbor.get_id()}")

# --- Chemin ---
def shortest(v):
    path = [v.get_id()]
    while v.previous:
        v = v.previous
        path.append(v.get_id())
    return path[::-1]

# --- Exécution ---
if __name__ == "__main__":
    start = g.get_vertex('Toronto')
    target = g.get_vertex('Halifax')

    dijkstra(g, start)

    path = shortest(target)
    print("Le plus court chemin:", path)