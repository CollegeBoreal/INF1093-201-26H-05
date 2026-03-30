# check_results.py
from dijkstra_tp import g, shortest

target = g.get_vertex('Nice')
path = shortest(target)

expected = ['Paris', 'Lyon', 'Nice']

if path == expected:
    print("✅ Bravo, chemin correct !")
else:
    print("❌ Incorrect")
    print("Ton chemin :", path)
    print("Attendu :", expected)