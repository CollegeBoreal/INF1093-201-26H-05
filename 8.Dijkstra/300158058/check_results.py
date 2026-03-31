"""
check_results.py
Auteur : BELAID Rabah
ID : 300158058
Description : Vérification simple du chemin le plus court.
"""

from dijkstra_tp import creer_graphe, dijkstra, reconstruire_chemin

def verifier_resultats():
    g = creer_graphe()
    depart = g.get_vertex("A")
    arrivee = g.get_vertex("G")

    dijkstra(g, depart)
    chemin = reconstruire_chemin(arrivee)
    distance = arrivee.get_distance()

    print("Chemin calculé :", chemin)
    print("Distance calculée :", distance)

    chemin_attendu = ["A", "C", "F", "G"]
    distance_attendue = 14

    if chemin == chemin_attendu and distance == distance_attendue:
        print("Vérification réussie : le résultat est correct.")
    else:
        print("Vérification échouée : le résultat ne correspond pas à l'attendu.")

if __name__ == "__main__":
    verifier_resultats()
