"""
Fichier : rectangle.py
Description : Classe Rectangle héritant de Figure
Auteur : [300155187]
Date : 2025-04-13
"""

from figure import Figure

class Rectangle(Figure):
    def __init__(self, largeur, longueur):
        super().__init__("Rectangle")
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        return self.largeur * self.longueur

    def afficher_info(self):
        return f"{super().afficher_info()}, largeur={self.largeur}, longueur={self.longueur}, aire={self.aire()}"