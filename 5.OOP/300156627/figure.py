"""
Fichier : figure.py
Description : Classe Carré héritant de Figure
Auteur : [300156627]
Date : 2002-05-10
"""

class Figure:
    def __init__(self, nom):
        # Nom de la figure (ex: Carré, Cercle)
        self.nom = nom

    def afficher_info(self):
        # Retourne une chaîne contenant le nom de la figure
        return f"Figure: {self.nom}"

    def aire(self):
        # Méthode à implémenter par les sous-classes
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")