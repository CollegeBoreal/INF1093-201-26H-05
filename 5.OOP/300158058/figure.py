"""
Fichier : figure.py
Description : Classe de base pour représenter une figure géométrique.
Auteur : BELAID Rabah
ID : 300158058
"""

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def description(self):
        return f"Figure géométrique : {self.nom}"

    def aire(self):
        raise NotImplementedError("La méthode aire() doit être définie dans les classes enfants.")
