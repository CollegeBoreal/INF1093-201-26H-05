import math
from Figure import Figure

class Hexagone(Figure):
    def __init__(self, rayon: float):
        self.rayon = rayon

    def aire(self):
        n = 6
        return (n * self.rayon ** 2 * math.sin(2 * math.pi / n)) / 2

    def afficher_info(self):
        return f"Hexagone régulier de rayon {self.rayon}"
