# check_results.py
from dijkstra_tp import g, dijkstra, shortest, path_distance

# Définir villes de départ et d'arrivée
start_city = 'Toronto'
target_city = 'Johannesburg'

start = g.get_vertex(start_city)
target = g.get_vertex(target_city)

# Exécuter Dijkstra
dijkstra(g, start)

# Calcul chemin et distance
path = shortest(target)
distance = path_distance(path)

# Chemin attendu réel (calculé à partir des distances)
expected_path = [
    'Toronto','New York','London','Paris','Casablanca',
    'Dakar','Lagos','Nairobi','Johannesburg'
]

# Vérification
if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
    print(f"Distance totale : {distance} km")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin :", " → ".join(path))
    print("Chemin attendu :", " → ".join(expected_path))
    print(f"Distance calculée : {distance} km")
