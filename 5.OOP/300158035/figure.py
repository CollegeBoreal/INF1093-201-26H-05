"""
Auteur : 300158035
Date : 2026-04-06
"""

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure: {self.nom}"

    def aire(self):
        raise NotImplementedError("Doit être implémentée")
