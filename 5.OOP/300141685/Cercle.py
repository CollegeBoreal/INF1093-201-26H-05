# INF1093 - Programmation 2 - POO
# Souleymane Barry - 300141685

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}, perimetre={self.perimetre():.2f}"
