"""
Fichier : Pentagone.py
Description : Classe Pentagone heritant de Figure
Auteur : Ouassim Ahmed Benamira
Date : 2026-04-10
"""

from figure import Figure
import math

class Pentagone(Figure):
    def __init__(self, cote):
        super().__init__("Pentagone")
        self.cote = cote

    def aire(self):
        return (self.cote ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4

    def afficher_info(self):
        return f"{super().afficher_info()}, cote={self.cote}, aire={self.aire():.2f}"
        