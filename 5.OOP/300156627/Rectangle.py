from figure import Figure

class Rectangle(Figure):
    def __init__(self, longueur, largeur):
        super().__init__("Rectangle")
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def afficher_info(self):
        return f"{super().afficher_info()}, longueur={self.longueur}, largeur={self.largeur}, aire={self.aire()}"