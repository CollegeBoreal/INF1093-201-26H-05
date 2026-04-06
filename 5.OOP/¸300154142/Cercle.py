from Figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        return f"{self.nom} - rayon : {self.rayon}"
