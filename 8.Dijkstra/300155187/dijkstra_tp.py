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

# Chemin optimal
path = shortest(target)
print("Chemin Dijkstra :", " → ".join(path))
print("Distance :", target.get_distance(), "km")


# Plusieurs chemins
all_paths = find_all_paths(g, 'Toronto', 'Johannesburg')

# Trier par distance
sorted_paths = sorted(all_paths, key=lambda p: path_distance(g, p))

print("\nTop 3 chemins :")
for i, p in enumerate(sorted_paths[:3]):
    print(f"{i+1}. {' → '.join(p)} | {path_distance(g, p)} km")
