"""
Fichier : Etoile.py
Description : Classe Etoile heritant de Figure
Auteur : Ouassim Ahmed Benamira
Date : 2026-04-10
"""

from figure import Figure
import math

class Etoile(Figure):
    def __init__(self, rayon_ext, rayon_int):
        super().__init__("Etoile")
        self.rayon_ext = rayon_ext
        self.rayon_int = rayon_int

    def aire(self):
        return 2.5 * math.sqrt(5 + 2 * math.sqrt(5)) * self.rayon_int ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon_ext={self.rayon_ext}, rayon_int={self.rayon_int}, aire={self.aire():.2f}"