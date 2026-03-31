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

# --- Chemin le plus court ---
def shortest(v):
    path = []
    while v:
        path.append(v.get_id())
        v = v.previous
    return path[::-1]

# ✅ --- AJOUT ICI ---
# --- Tous les chemins ---
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    paths = []

    for node in graph.get_vertex(start).adjacent:
        if node.get_id() not in path:
            newpaths = find_all_paths(graph, node.get_id(), end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

# --- Distance d’un chemin ---
def path_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        v = graph.get_vertex(path[i])
        next_v = graph.get_vertex(path[i+1])
        distance += v.get_weight(next_v)
    return distance

# --- Exécution ---
start = g.get_vertex('Toronto')
target = g.get_vertex('Johannesburg')

dijkstra(g, start)

# 🔴 Chemin optimal
path = shortest(target)
print("🌍 Chemin Dijkstra :", " → ".join(path))
print("📏 Distance :", target.get_distance(), "km")

# 🔵 Plusieurs chemins
all_paths = find_all_paths(g, 'Toronto', 'Johannesburg')

# Trier par distance
sorted_paths = sorted(all_paths, key=lambda p: path_distance(g, p))

print("\n🌍 Top 3 chemins :")
for i, p in enumerate(sorted_paths[:3]):
    print(f"{i+1}. {' → '.join(p)} | {path_distance(g, p)} km")
