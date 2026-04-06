from figure import Figure
import math

class Ellipse(Figure):
    def __init__(self, a, b):
        super().__init__("Ellipse")
        self.a = a  # grand axe
        self.b = b  # petit axe

    def aire(self):
        return math.pi * self.a * self.b

    def afficher_info(self):
        return f"{super().afficher_info()}, a={self.a}, b={self.b}, aire={self.aire():.2f}"