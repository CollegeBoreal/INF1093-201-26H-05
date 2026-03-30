"""
Fichier : Carre.py
Description : Classe Carré héritant de Figure
Auteur : [300151781]
Date : 2026-03-29
"""

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")  # Appel du constructeur de la classe de base
        self.cote = cote           # Longueur du côté du carré

    def aire(self):
        # Calcul de l'aire du carré
        return self.cote ** 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, le côté et l'aire
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
 