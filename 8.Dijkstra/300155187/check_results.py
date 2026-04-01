# check_results.py
from dijkstra_tp import shortest, g, dijkstra, path_distance

# Sommet de départ et de fin
start_city = 'Toronto'
target_city = 'Johannesburg'

# Préparer le graphe
start = g.get_vertex(start_city)
target = g.get_vertex(target_city)

# Exécuter Dijkstra
dijkstra(g, start)

# Chemin calculé
path = shortest(target)

# Chemin attendu
expected_path = [
    'Toronto','New York','London','Paris','Casablanca',
    'Dakar','Lagos','Nairobi','Johannesburg'
]

# Calculer distance
distance = path_distance(g, path)

# Vérification
if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
    print(f"Distance totale : {distance} km")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin :", " → ".join(path))
    print("Chemin attendu :", " → ".join(expected_path))
    print(f"Distance calculée : {distance} km")
