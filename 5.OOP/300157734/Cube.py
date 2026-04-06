"""
Fichier : Cube.py
Description : Classe Cube héritant de Figure
Auteur : abdelkader messali
Date : 2026-04-06
"""

from figure import Figure


class Cube(Figure):
    def __init__(self, arete):
        super().__init__("Cube")
        self.arete = arete

    def aire(self):
        # Aire totale de la surface du cube
        return 6 * (self.arete ** 2)

    def volume(self):
        # Volume du cube
        return self.arete ** 3

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, arête={self.arete}, "
            f"aire={self.aire()}, volume={self.volume()}"
        )
