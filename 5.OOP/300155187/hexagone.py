"""
Fichier : hexagone.py
Description : Classe Hexagone régulier héritant de Figure
Auteur : [300155187]
Date : 2025-04-13
"""

import math
from figure import Figure

class Hexagone(Figure):
    def __init__(self, cote):
        super().__init__("Hexagone")
        self.cote = cote

    def aire(self):
        # Formule : (3 * sqrt(3) / 2) * côté²
        return (3 * math.sqrt(3) / 2) * self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire():.2f}"