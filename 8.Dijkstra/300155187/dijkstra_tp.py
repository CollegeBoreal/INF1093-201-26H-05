# dijkstra_tp.py
from graph import Graph

# Création du graphe
g = Graph()
villes = [
    'Toronto','New York','London','Paris','Berlin','Rome',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]
for ville in villes:
    g.add_vertex(ville)

# Arêtes avec distances
edges = [
    ('Toronto','New York',800),
    ('New York','London',5600),
    ('New York','Paris',5800),
    ('Toronto','London',5900),
    ('London','Paris',340),
    ('Paris','Berlin',1050),
    ('Berlin','Rome',1180),
    ('Paris','Casablanca',2000),
    ('London','Casablanca',3000),
    ('Berlin','Casablanca',2800),
    ('Rome','Dakar',3500),
    ('Casablanca','Dakar',2700),
    ('Dakar','Lagos',3000),
    ('Lagos','Nairobi',4400),
    ('Nairobi','Johannesburg',2900),
]

for u,v,w in edges:
    g.add_edge(u,v,w)

# Dijkstra
def dijkstra(aGraph, start):
    start.set_distance(0)
    unvisited = [v for v in aGraph]

    while unvisited:
        current = min(unvisited, key=lambda v: v.get_distance())
        current.set_visited()
        unvisited.remove(current)

        for neighbor in current.get_connections():
            if neighbor.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(neighbor)
            if new_dist < neighbor.get_distance():
                neighbor.set_distance(new_dist)
                neighbor.set_previous(current)

# Reconstitution chemin
def shortest(v):
    path = [v.get_id()]
    while v.previous:
        v = v.previous
        path.append(v.get_id())
    return path[::-1]

# Distance totale
def path_distance(path):
    dist = 0
    for i in range(len(path)-1):
        dist += g.get_vertex(path[i]).get_weight(g.get_vertex(path[i+1]))
    return dist
