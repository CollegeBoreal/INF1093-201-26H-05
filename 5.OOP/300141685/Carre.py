# INF1093 - Programmation 2 - POO
# Souleymane Barry - 300141685

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carre")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def perimetre(self):
        return 4 * self.cote

    def afficher_info(self):
        return f"{super().afficher_info()}, cote={self.cote}, aire={self.aire()}, perimetre={self.perimetre()}"
