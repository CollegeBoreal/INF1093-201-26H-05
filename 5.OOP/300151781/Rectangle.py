"""
Fichier : Rectangle.py
Description : Classe Rectangle héritant de Figure
Auteur : 300151781
Date : 2026-03-29
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
        return f"{super().afficher_info()}, L={self.largeur}, H={self.hauteur}, aire={self.aire()}"