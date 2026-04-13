import math
from Figure import Figure

class Octogone(Figure):
    def __init__(self, rayon: float):
        self.rayon = rayon

    def aire(self):
        n = 8
        return (n * self.rayon ** 2 * math.sin(2 * math.pi / n)) / 2

    def afficher_info(self):
        return f"Octogone régulier de rayon {self.rayon}"
