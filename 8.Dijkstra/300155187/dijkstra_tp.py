# dijkstra_tp.py
from graph import Graph

# --- Création du graphe ---
g = Graph()

cities = [
    'Toronto','New York','London','Paris','Berlin','Rome',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]

for city in cities:
    g.add_vertex(city)

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

for u, v, w in edges:
    g.add_edge(u, v, w)


# --- Dijkstra ---
def dijkstra(aGraph, start):

    # reset (important)
    for v in aGraph:
        v.distance = float('inf')
        v.visited = False
        v.previous = None

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


# --- Plus court chemin ---
def shortest(v):
    path = []
    while v:
        path.append(v.get_id())
        v = v.previous
    return path[::-1]


# --- Distance ---
def path_distance(aGraph, path):
    dist = 0
    for i in range(len(path)-1):
        u = aGraph.get_vertex(path[i])
        v = aGraph.get_vertex(path[i+1])
        dist += u.get_weight(v)
    return dist


# --- Tous les chemins ---
def find_all_paths(aGraph, start_id, end_id, path=None):
    if path is None:
        path = []

    path = path + [start_id]

    if start_id == end_id:
        return [path]

    paths = []
    for neighbor in aGraph.get_vertex(start_id).get_connections():
        if neighbor.get_id() not in path:
            newpaths = find_all_paths(aGraph, neighbor.get_id(), end_id, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths
