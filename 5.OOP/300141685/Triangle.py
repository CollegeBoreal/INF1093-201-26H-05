# INF1093 - Programmation 2 - POO
# Souleymane Barry - 300141685

from figure import Figure
import math

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def perimetre(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.hauteur ** 2)
        return self.base + self.hauteur + hypotenuse

    def afficher_info(self):
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire():.2f}, perimetre={self.perimetre():.2f}"
