# check_results.py
from dijkstra_tp import shortest, g

target = g.get_vertex('Prague')
path = shortest(target)

expected_path = ['Paris', 'Berlin', 'Prague']

if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin  :", path)
    print("Chemin attendu:", expected_path)
