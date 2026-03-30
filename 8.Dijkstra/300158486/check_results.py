from dijkstra_tp import build_graph, dijkstra, shortest


graph = build_graph()
start = graph.get_vertex("a")
target = graph.get_vertex("e")

dijkstra(graph, start)
path = shortest(target)
distance = target.get_distance()

expected_path = ["a", "c", "f", "e"]
expected_distance = 20

if path == expected_path and distance == expected_distance:
    print("✅ Bravo, le chemin est correct !")
    print("Chemin :", path)
    print("Distance :", distance)
else:
    print("❌ Résultat incorrect.")
    print("Votre chemin :", path)
    print("Distance trouvée :", distance)
    print("Chemin attendu :", expected_path)
    print("Distance attendue :", expected_distance)
