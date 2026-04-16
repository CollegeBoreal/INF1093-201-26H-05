from world_graph import WorldGraph
from dijkstra_tp import dijkstra, shortest, path_distance

g = WorldGraph()

start_city = 'Toronto'
target_city = 'Johannesburg'

start = g.get_vertex(start_city)
target = g.get_vertex(target_city)

dijkstra(g, start)

path = shortest(target)
distance = path_distance(g, path)

print("Chemin trouvé :", " → ".join(path))
print("Distance :", distance, "km")

expected = [
    'Toronto','London','Paris',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]

if path == expected:
    print("✅ Correct")
else:
    print("❌ Incorrect")
    print("Attendu :", " → ".join(expected))