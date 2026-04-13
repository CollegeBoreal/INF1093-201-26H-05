from Figure import Figure

class Parallelogramme(Figure):
    def __init__(self, base: float, hauteur: float, decalage: float = 1.5):
        self.base = base
        self.hauteur = hauteur
        self.decalage = decalage

    def aire(self):
        return self.base * self.hauteur

    def afficher_info(self):
        return f"Parallélogramme de base {self.base} et hauteur {self.hauteur}"
