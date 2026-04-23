class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def afficher_info(self):
        return f"Rectangle de largeur {self.largeur} et hauteur {self.hauteur}"
