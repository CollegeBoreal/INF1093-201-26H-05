import math


class Cylindre:
    def __init__(self, rayon, hauteur):
        self.rayon = rayon
        self.hauteur = hauteur

    def aire(self):
        return 2 * math.pi * self.rayon * (self.rayon + self.hauteur)

    def volume(self):
        return math.pi * self.rayon ** 2 * self.hauteur

    def afficher_info(self):
        return f"Cylindre de rayon {self.rayon} et hauteur {self.hauteur}"
