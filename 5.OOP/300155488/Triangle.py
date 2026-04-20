from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):  # ← 2 paramètres !
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        # Aire = (base * hauteur) / 2
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"