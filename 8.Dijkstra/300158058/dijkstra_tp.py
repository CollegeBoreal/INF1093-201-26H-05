"""
dijkstra_tp.py
Auteur : BELAID Rabah
ID : 300158058
Description : Exécution de l'algorithme de Dijkstra sur un graphe pondéré.
"""

from graph import Graph


def dijkstra(graphe, depart):
    depart.set_distance(0)
    non_visites = [sommet for sommet in graphe]

    while non_visites:
        courant = min(non_visites, key=lambda sommet: sommet.get_distance())
        courant.set_visited()
        non_visites.remove(courant)

        for voisin in courant.get_connections():
            if voisin.visited:
                continue

            nouvelle_distance = courant.get_distance() + courant.get_weight(voisin)

            if nouvelle_distance < voisin.get_distance():
                voisin.set_distance(nouvelle_distance)
                voisin.set_previous(courant)
                print(
                    f"Mise à jour : {courant.get_id()} -> {voisin.get_id()} | "
                    f"distance = {voisin.get_distance()}"
                )
            else:
                print(
                    f"Aucun changement : {courant.get_id()} -> {voisin.get_id()} | "
                    f"distance actuelle = {voisin.get_distance()}"
                )


def reconstruire_chemin(sommet):
    chemin = [sommet.get_id()]
    while sommet.previous:
        sommet = sommet.previous
        chemin.append(sommet.get_id())
    return chemin[::-1]


def creer_graphe():
    g = Graph()

    for node in ["A", "B", "C", "D", "E", "F", "G"]:
        g.add_vertex(node)

    # Graphe différent de l'exemple, mais même principe
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "D", 5)
    g.add_edge("B", "E", 12)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "F", 7)
    g.add_edge("D", "E", 2)
    g.add_edge("D", "F", 6)
    g.add_edge("E", "G", 3)
    g.add_edge("F", "G", 4)

    return g


def afficher_graphe(g):
    print("=== Données du graphe ===")
    for sommet in g:
        for voisin in sommet.get_connections():
            print(f"({sommet.get_id()}, {voisin.get_id()}, poids={sommet.get_weight(voisin)})")


def main():
    g = creer_graphe()
    afficher_graphe(g)

    depart = g.get_vertex("A")
    arrivee = g.get_vertex("G")

    print("\n=== Exécution de Dijkstra ===")
    dijkstra(g, depart)

    chemin = reconstruire_chemin(arrivee)

    print("\n=== Résultat final ===")
    print("Distance minimale vers G :", arrivee.get_distance())
    print("Chemin le plus court :", " -> ".join(chemin))


if __name__ == "__main__":
    main()
