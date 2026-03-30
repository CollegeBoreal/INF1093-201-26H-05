"""
Fichier : Triangle.py
Description : Classe représentant un triangle.
Auteur : BELAID Rabah
ID : 300158058
"""

from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return (
            f"{self.description()} | base = {self.base} | hauteur = {self.hauteur} | "
            f"aire = {self.aire()}"
        )
