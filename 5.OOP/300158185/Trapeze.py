from Figure import Figure

class Trapeze(Figure):
    def __init__(self, base1: float, base2: float, hauteur: float):
        self.base1 = base1
        self.base2 = base2
        self.hauteur = hauteur

    def aire(self):
        return ((self.base1 + self.base2) * self.hauteur) / 2

    def afficher_info(self):
        return f"Trapèze de bases {self.base1} et {self.base2}, hauteur {self.hauteur}"
