# --- check_results.py ---
from dijkstra_tp import shortest, g, path_distance

def check_path(target_city, expected_path):
    """
    Vérifie si le chemin calculé vers target_city correspond au chemin attendu.
    Affiche également la distance totale.
    """
    target = g.get_vertex(target_city)
    path = shortest(target)
    distance = path_distance(g, path)

    if path == expected_path:
        print(f"✅ Bravo, le chemin vers {target_city} est correct !")
        print(f"Distance totale : {distance} km\n")
    else:
        print(f"❌ Chemin incorrect vers {target_city}.")
        print("Votre chemin :", " → ".join(path))
        print("Chemin attendu :", " → ".join(expected_path))
        print(f"Distance calculée : {distance} km\n")

# --- Test principal ---
if __name__ == "__main__":
    target_city = 'Johannesburg'
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
    
    check_path(target_city, expected_path)
