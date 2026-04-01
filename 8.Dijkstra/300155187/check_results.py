# check_results.py
from dijkstra_tp import shortest, g, path_distance

# --- Sommet cible ---
target_city = 'Johannesburg'
target = g.get_vertex(target_city)

# --- Chemin calculé ---
path = shortest(target)

# --- Chemin attendu ---
expected_path = [
    'Toronto','New York','London','Paris','Casablanca',
    'Dakar','Lagos','Nairobi','Johannesburg'
]

# --- Vérification ---
if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
    distance = path_distance(g, path)
    print(f"Distance totale : {distance} km")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin :", " → ".join(path))
    print("Chemin attendu :", " → ".join(expected_path))
    distance = path_distance(g, path)
    print(f"Distance calculée : {distance} km")
