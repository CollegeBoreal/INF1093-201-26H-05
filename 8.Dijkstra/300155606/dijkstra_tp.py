from graph import Graph

g = Graph()

# 🌍 Villes
cities = [
    'Toronto','New York','London','Paris','Berlin','Rome',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]

for city in cities:
    g.add_vertex(city)

# 🌍 Connexions
edges = [
    ('Toronto','New York',800),
    ('New York','London',5600),
    ('London','Paris',340),
    ('Paris','Berlin',1050),
    ('Berlin','Rome',1180),
    ('Paris','Casablanca',2000),
    ('Casablanca','Dakar',2700),
    ('Dakar','Lagos',3000),
    ('Lagos','Nairobi',4400),
    ('Nairobi','Johannesburg',2900),
]

for u, v, w in edges:
    g.add_edge(u, v, w)

# --- Dijkstra ---
def dijkstra(graph, start):
    start.set_distance(0)
    unvisited = list(graph)

    while unvisited:
        current = min(unvisited, key=lambda v: v.get_distance())
        unvisited.remove(current)
        current.set_visited()

        for neighbor in current.adjacent:
            if neighbor.visited:
                continue

            new_dist = current.get_distance() + current.get_weight(neighbor)

            if new_dist < neighbor.get_distance():
                neighbor.set_distance(new_dist)
                neighbor.set_previous(current)

# --- Chemin ---
def shortest(v):
    path = []
    while v:
        path.append(v.get_id())
        v = v.previous
    return path[::-1]

# --- Exécution ---
start = g.get_vertex('Toronto')
target = g.get_vertex('Johannesburg')

dijkstra(g, start)

path = shortest(target)

print("🌍 Chemin :", " → ".join(path))
print("📏 Distance :", target.get_distance(), "km")
