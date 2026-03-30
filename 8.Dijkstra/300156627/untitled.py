# check_results.py
from dijkstra_tp import shortest, g

target = g.get_vertex('Rome')
path = shortest(target)

# Chemin attendu pour ce graphe
expected_path = ['Paris', 'Berlin', 'Bruxelles', 'Rome']

if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin:", path)
    print("Chemin attendu:", expected_path)