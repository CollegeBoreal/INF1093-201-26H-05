"""
Fichier : Carre.py
Description : Classe représentant un carré.
Auteur : BELAID Rabah
ID : 300158058
"""

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote * self.cote

    def perimetre(self):
        return 4 * self.cote

    def afficher_info(self):
        return (
            f"{self.description()} | côté = {self.cote} | "
            f"périmètre = {self.perimetre()} | aire = {self.aire()}"
        )
