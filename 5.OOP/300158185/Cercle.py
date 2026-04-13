import math
from Figure import Figure

class Cercle(Figure):
    def __init__(self, rayon: float):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        return f"Cercle de rayon {self.rayon}"
