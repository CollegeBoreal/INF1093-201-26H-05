import math
from Figure import Figure

class Ellipse(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def aire(self):
        return math.pi * self.a * self.b

    def afficher_info(self):
        return f"Ellipse de demi-axes {self.a} et {self.b}"
