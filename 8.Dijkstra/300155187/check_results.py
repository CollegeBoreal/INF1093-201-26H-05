# --- check_results.py ---
from dijkstra_tp import shortest, g, path_distance

# Sommet cible
target_city = 'Johannesburg'
target = g.get_vertex(target_city)

# Chemin calculé
path = shortest(target)
distance = path_distance(g, path)

# Chemin attendu
expected_path = [
    'Toronto',
    'New York',
    'London',
    'Paris',
    'Casablanca',
    'Dakar',
    'Lagos',
    'Nairobi',
    'Johannesburg'
]

# Vérification
if path == expected_path:
    print(f"✅ Bravo, le chemin vers {target_city} est correct !")
    print(f"Distance totale : {distance} km")
else:
    print(f"❌ Chemin incorrect vers {target_city}.")
    print("Votre chemin :", " → ".join(path))
    print("Chemin attendu :", " → ".join(expected_path))
    print(f"Distance calculée : {distance} km")
