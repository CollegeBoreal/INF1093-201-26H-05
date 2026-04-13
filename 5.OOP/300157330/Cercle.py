from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def description(self):
        return f"{super().description()}, rayon = {self.rayon}, aire = {self.aire():.2f}"
