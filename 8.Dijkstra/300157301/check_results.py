from  djikstra_tp import shortest, g, dijkstra

start = g.get_vertex('a')
dijkstra(g, start)

target = g.get_vertex('e')
path = shortest(target)

expected_path = ['a', 'c', 'f', 'e']

if path == expected_path:
    print("✅ Bravo, le chemin est correct !")
else:
    print("❌ Chemin incorrect.")
    print("Votre chemin:", path)
    print("Chemin attendu:", expected_path)