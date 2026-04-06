class Sommet:
    def __init__(self, nom):
        self.nom = nom
        self.voisins = {}
        self.distance = float("inf")
        self.visite = False
        self.precedent = None

    def ajouter_voisin(self, voisin, poids=0):
        self.voisins[voisin] = poids

    def connexions(self):
        return self.voisins.keys()

    def obtenir_nom(self):
        return self.nom

    def obtenir_poids(self, voisin):
        return self.voisins[voisin]

    def definir_distance(self, distance):
        self.distance = distance

    def obtenir_distance(self):
        return self.distance

    def definir_precedent(self, precedent):
        self.precedent = precedent

    def definir_visite(self):
        self.visite = True

    def __str__(self):
        return f"{self.nom} -> {[v.nom for v in self.voisins]}"


class Graphe:
    def __init__(self):
        self.sommets = {}
        self.nombre_sommets = 0

    def __iter__(self):
        return iter(self.sommets.values())

    def ajouter_sommet(self, nom):
        self.nombre_sommets += 1
        sommet = Sommet(nom)
        self.sommets[nom] = sommet
        return sommet

    def obtenir_sommet(self, nom):
        return self.sommets.get(nom, None)

    def ajouter_arete(self, debut, fin, poids=0):
        if debut not in self.sommets:
            self.ajouter_sommet(debut)
        if fin not in self.sommets:
            self.ajouter_sommet(fin)

        self.sommets[debut].ajouter_voisin(self.sommets[fin], poids)
        self.sommets[fin].ajouter_voisin(self.sommets[debut], poids)

    def obtenir_sommets(self):
        return self.sommets.keys()