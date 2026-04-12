"""
Fichier : Carre.py
Classe Carré
Auteur : 300159189
"""

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, cote={self.cote}, aire={self.aire()}"