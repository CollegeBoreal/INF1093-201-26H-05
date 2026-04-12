from figure import Figure
import math

class Pentagone(Figure):
    def __init__(self, cote):
        super().__init__("Pentagone")
        self.cote = cote

    def aire(self):
        return (5 * self.cote**2) / (4 * math.tan(math.pi/5))

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire():.2f}"