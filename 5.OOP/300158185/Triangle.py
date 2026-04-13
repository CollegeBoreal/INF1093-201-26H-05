from Figure import Figure

class Triangle(Figure):
    def __init__(self, base: float, hauteur: float):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return f"Triangle de base {self.base} et hauteur {self.hauteur}"
