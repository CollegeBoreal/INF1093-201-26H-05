from dijkstra_tp import g, dijkstra, shortest, path_distance

# --- Configuration ---
start_city = 'Toronto'
target_city = 'Johannesburg'

# --- Préparation ---
start = g.get_vertex(start_city)
target = g.get_vertex(target_city)

# --- Exécution Dijkstra ---
dijkstra(g, start)

# --- Résultat obtenu ---
path = shortest(target)
distance = path_distance(g, path)

# --- Résultat attendu ---
expected_path = [
    'Toronto','New York','London','Paris',
    'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
]

# --- Affichage ---
print("Chemin trouvé :", " → ".join(path))
print("Distance :", distance, "km")

if path == expected_path:
    print("\n✅ Bravo, le chemin est correct !")
else:
    print("\n❌ Chemin incorrect.")
    print("Chemin attendu :", " → ".join(expected_path))
