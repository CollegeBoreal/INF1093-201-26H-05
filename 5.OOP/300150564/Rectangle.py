"""
Fichier : Rectangle.py
Description : Classe Rectangle heritant de Figure
Auteur : Ouassim Ahmed Benamira
Date : 2026-04-10
"""

from figure import Figure

class Rectangle(Figure):
    def __init__(self, largeur, hauteur):
        super().__init__("Rectangle")
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def afficher_info(self):
        return f"{super().afficher_info()}, largeur={self.largeur}, hauteur={self.hauteur}, aire={self.aire()}"