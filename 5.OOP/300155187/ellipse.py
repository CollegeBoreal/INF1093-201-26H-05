"""
Fichier : ellipse.py
Description : Classe Ellipse héritant de Figure
Auteur : [300155187]
Date : 2025-04-13
"""

import math
from figure import Figure

class Ellipse(Figure):
    def __init__(self, demi_axe_a, demi_axe_b):
        super().__init__("Ellipse")
        self.demi_axe_a = demi_axe_a   # grand demi-axe
        self.demi_axe_b = demi_axe_b   # petit demi-axe

    def aire(self):
        return math.pi * self.demi_axe_a * self.demi_axe_b

    def afficher_info(self):
        return (f"{super().afficher_info()}, demi-axe a={self.demi_axe_a}, "
                f"demi-axe b={self.demi_axe_b}, aire={self.aire():.2f}")