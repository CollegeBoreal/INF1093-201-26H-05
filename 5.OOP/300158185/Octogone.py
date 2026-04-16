class Octogone:
    def __init__(self, cote, apothem):
        self.cote = cote
        self.apothem = apothem

    def aire(self):
        perimetre = 8 * self.cote
        return (perimetre * self.apothem) / 2

    def afficher_info(self):
        return f"Octogone de côté {self.cote} et apothème {self.apothem}"
