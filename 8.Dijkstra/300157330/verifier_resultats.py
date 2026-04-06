from dijkstra_tp import g, reconstruire_chemin

arrivee = g.obtenir_sommet("e")
chemin = reconstruire_chemin(arrivee)

chemin_attendu = ["a", "c", "f", "e"]

if chemin == chemin_attendu:
    print("✅ Résultat correct")
    print("Chemin trouvé :", chemin)
else:
    print("❌ Résultat incorrect")
    print("Chemin trouvé :", chemin)
    print("Chemin attendu :", chemin_attendu)