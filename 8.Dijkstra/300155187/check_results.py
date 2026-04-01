# check_results.py
from dijkstra_tp import g, dijkstra, shortest

# --- Configuration ---
start_city = 'Toronto'
target_city = 'Johannesburg'

# --- Préparer le graphe ---
start = g.get_vertex(start_city)
target = g.get_vertex(target_city)

# --- Exécuter Dijkstra ---
dijkstra(g, start)

# --- Calculer le chemin ---
path = shortest(target)

# --- Calculer la distance totale ---
distance = 0
for i in range(len(path)-1):
    u = g.get_vertex(path[i])
    v = g.get_vertex(path[i+1])
    distance += u.get_weight(v)

# --- Chemin attendu ---
expected_path = [
    'Toronto','New York','London','Paris','Casablanca',
    'Dakar','Lagos','Nairobi','Johannesburg'
]

# --- Vérification ---
if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
    print(f"Distance totale : {distance} km")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin :", " → ".join(path))
    print("Chemin attendu :", " → ".join(expected_path))
    print(f"Distance calculée : {distance} km")
