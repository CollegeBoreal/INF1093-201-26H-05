"""
Fichier : Triangle.py
Description : Classe Triangle héritant de Figure
Auteur : Djelloul msili
Date : 2026-04-13
"""

from figure import Figure


class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        # Calcul de l'aire du triangle
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, les dimensions et l'aire
        return (
            f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, "
            f"aire={self.aire()}"
        )
