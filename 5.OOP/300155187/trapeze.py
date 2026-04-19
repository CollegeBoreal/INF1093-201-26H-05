"""
Fichier : trapeze.py
Description : Classe Trapèze héritant de Figure
Auteur : [300155187]
Date : 2025-04-13
"""

from figure import Figure

class Trapeze(Figure):
    def __init__(self, base_grande, base_petite, hauteur):
        super().__init__("Trapèze")
        self.base_grande = base_grande
        self.base_petite = base_petite
        self.hauteur = hauteur

    def aire(self):
        return ((self.base_grande + self.base_petite) * self.hauteur) / 2

    def afficher_info(self):
        return (f"{super().afficher_info()}, grande base={self.base_grande}, "
                f"petite base={self.base_petite}, hauteur={self.hauteur}, aire={self.aire()}")