from figure import Figure
import math

class Hexagone(Figure):
    def __init__(self, cote):
        super().__init__("Hexagone")
        self.cote = cote

    def aire(self):
        return (3 * math.sqrt(3) * self.cote**2) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire():.2f}"