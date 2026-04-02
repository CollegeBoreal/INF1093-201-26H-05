# check_results.py
from dijkstra_tp import g, dijkstra, shortest, path_distance, reset_graph

start_city = 'Toronto'
target_city = 'Johannesburg'

start = g.get_vertex(start_city)
target = g.get_vertex(target_city)

# 🔄 Réinitialisation avant Dijkstra
reset_graph(g)

dijkstra(g, start)

path = shortest(target)
distance = path_distance(g, path)

# ✅ CHEMIN CORRECT
expected_path = [
    'Toronto','New York','London','Paris',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]

print("Chemin trouvé :", " → ".join(path))
print("Distance :", distance, "km")

if path == expected_path:
    print("\n✅ Bravo, le chemin est correct !")
else:
    print("\n❌ Chemin incorrect.")
    print("Chemin attendu :", " → ".join(expected_path))
