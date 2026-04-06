from graph import Graphe

# Création du graphe
g = Graphe()

for sommet in ["a", "b", "c", "d", "e", "f"]:
    g.ajouter_sommet(sommet)

g.ajouter_arete("a", "b", 7)
g.ajouter_arete("a", "c", 9)
g.ajouter_arete("a", "f", 14)
g.ajouter_arete("b", "c", 10)
g.ajouter_arete("b", "d", 15)
g.ajouter_arete("c", "d", 11)
g.ajouter_arete("c", "f", 2)
g.ajouter_arete("d", "e", 6)
g.ajouter_arete("e", "f", 9)

print("Liste des arêtes du graphe :")
for sommet in g:
    for voisin in sommet.connexions():
        print(f"({sommet.obtenir_nom()}, {voisin.obtenir_nom()}, {sommet.obtenir_poids(voisin)})")


def dijkstra(graphe, depart):
    depart.definir_distance(0)
    non_visites = [s for s in graphe]

    while non_visites:
        courant = min(non_visites, key=lambda s: s.obtenir_distance())
        non_visites.remove(courant)
        courant.definir_visite()

        for voisin in courant.voisins:
            if voisin.visite:
                continue

            nouvelle_distance = courant.obtenir_distance() + courant.obtenir_poids(voisin)

            if nouvelle_distance < voisin.obtenir_distance():
                voisin.definir_distance(nouvelle_distance)
                voisin.definir_precedent(courant)
                print(
                    f"mise à jour : {courant.obtenir_nom()} -> {voisin.obtenir_nom()} distance = {voisin.obtenir_distance()}"
                )
            else:
                print(
                    f"pas de changement : {courant.obtenir_nom()} -> {voisin.obtenir_nom()} distance = {voisin.obtenir_distance()}"
                )


def reconstruire_chemin(sommet):
    chemin = [sommet.obtenir_nom()]
    while sommet.precedent:
        sommet = sommet.precedent
        chemin.append(sommet.obtenir_nom())
    return chemin[::-1]


depart = g.obtenir_sommet("a")
arrivee = g.obtenir_sommet("e")

dijkstra(g, depart)

chemin_final = reconstruire_chemin(arrivee)
print("Chemin le plus court :", chemin_final)
print("Distance totale :", arrivee.obtenir_distance())