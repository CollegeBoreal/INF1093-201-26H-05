from dijkstra_tp import g, reconstruire_chemin

arrivee = g.obtenir_sommet("e")
chemin = reconstruire_chemin(arrivee)

if chemin == ['a', 'c', 'f', 'e']:
    print("OK")
else:
    print("ERREUR")