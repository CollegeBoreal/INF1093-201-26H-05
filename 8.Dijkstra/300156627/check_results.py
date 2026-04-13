# check_results.py
from dijkstra_tp import g, shortest

target = g.get_vertex('Rome')
path = shortest(target)

expected = ['Paris', 'Berlin', 'Bruxelles', 'Rome']

if path == expected:
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Incorrect")
    print("Ton chemin :", path)
    print("Attendu :", expected)