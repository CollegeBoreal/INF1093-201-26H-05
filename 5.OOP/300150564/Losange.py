"""
Fichier : Losange.py
Description : Classe Losange heritant de Figure
Auteur : Ouassim Ahmed Benamira
Date : 2026-04-10
"""

from figure import Figure

class Losange(Figure):
    def __init__(self, d1, d2):
        super().__init__("Losange")
        self.d1 = d1
        self.d2 = d2

    def aire(self):
        return (self.d1 * self.d2) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, d1={self.d1}, d2={self.d2}, aire={self.aire()}"