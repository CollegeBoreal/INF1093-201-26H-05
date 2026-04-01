# check_results.py
from dijkstra_tp import shortest, g

# Sommet cible
target_city = 'Johannesburg'
target = g.get_vertex(target_city)

# Chemin calculé
path = shortest(target)

# Chemin attendu (chemin minimal réel)
expected_path = [
    'Toronto','New York','London','Paris','Casablanca',
    'Dakar','Lagos','Nairobi','Johannesburg'
]

# Vérification simple
if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin:", path)
    print("Chemin attendu:", expected_path)
