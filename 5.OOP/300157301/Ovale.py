
import math


class Ovale:
    def __init__(self, demi_grand_axe, demi_petit_axe):
        self.demi_grand_axe = demi_grand_axe
        self.demi_petit_axe = demi_petit_axe

    def aire(self):
        return math.pi * self.demi_grand_axe * self.demi_petit_axe

    def afficher_info(self):
        return f"Ovale de demi-axes {self.demi_grand_axe} et {self.demi_petit_axe}"
