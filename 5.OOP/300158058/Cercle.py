"""
Fichier : Cercle.py
Description : Classe représentant un cercle.
Auteur : BELAID Rabah
ID : 300158058
"""

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def circonference(self):
        return 2 * math.pi * self.rayon

    def afficher_info(self):
        return (
            f"{self.description()} | rayon = {self.rayon} | "
            f"circonférence = {self.circonference():.2f} | aire = {self.aire():.2f}"
        )
