
import math


class Cone:
    def __init__(self, rayon, hauteur):
        self.rayon = rayon
        self.hauteur = hauteur

    def aire(self):
        generatrice = math.sqrt(self.rayon ** 2 + self.hauteur ** 2)
        return math.pi * self.rayon * (self.rayon + generatrice)

    def volume(self):
        return (math.pi * self.rayon ** 2 * self.hauteur) / 3

    def afficher_info(self):
        return f"Cône de rayon {self.rayon} et hauteur {self.hauteur}"
