"""
Fichier : Triangle.py
Description : Classe Triangle héritant de Figure
Auteur : CHOUAIB AIT CHOUAIB
ID : 300155045
Date : 2026-04-06
"""

from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")  # Appel du constructeur de la classe de base
        self.base = base               # Base du triangle
        self.hauteur = hauteur         # Hauteur du triangle

    def aire(self):
        # Calcul de l'aire du triangle
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, la base, la hauteur et l'aire
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"
