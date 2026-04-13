import math


class Anneau:
    def __init__(self, rayon_externe, rayon_interne):
        self.rayon_externe = rayon_externe
        self.rayon_interne = rayon_interne

    def aire(self):
        return math.pi * (self.rayon_externe ** 2 - self.rayon_interne ** 2)

    def afficher_info(self):
        return f"Anneau de rayon externe {self.rayon_externe} et rayon interne {self.rayon_interne}"

