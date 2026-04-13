from Figure import Figure

class Rectangle(Figure):
    def __init__(self, longueur: float, largeur: float):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def afficher_info(self):
        return f"Rectangle de longueur {self.longueur} et largeur {self.largeur}"
