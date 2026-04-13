class Hexagone:
    def __init__(self, cote, apothem):
        self.cote = cote
        self.apothem = apothem

    def aire(self):
        perimetre = 6 * self.cote
        return (perimetre * self.apothem) / 2

    def afficher_info(self):
        return f"Hexagone de côté {self.cote} et apothème {self.apothem}"
      
