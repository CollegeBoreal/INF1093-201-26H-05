"""
Fichier : Cube.py
Description : Classe représentant un cube.
Auteur : BELAID Rabah
ID : 300158058
"""

from figure import Figure

class Cube(Figure):
    def __init__(self, arete):
        super().__init__("Cube")
        self.arete = arete

    def aire(self):
        return 6 * (self.arete ** 2)

    def volume(self):
        return self.arete ** 3

    def afficher_info(self):
        return (
            f"{self.description()} | arête = {self.arete} | "
            f"surface totale = {self.aire()} | volume = {self.volume()}"
        )
