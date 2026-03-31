# check_results.py
from dijkstra_tp import shortest, g

# Sommet cible
target = g.get_vertex('Johannesburg')

# Chemin calculé
path = shortest(target)

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
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin :", path)
    print("Chemin attendu :", expected_path)
