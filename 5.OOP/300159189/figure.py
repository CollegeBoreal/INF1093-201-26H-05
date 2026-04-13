"""
Fichier : figure.py
Classe de base Figure
Auteur : 300159189
"""

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure: {self.nom}"

    def aire(self):
        raise NotImplementedError("Cette méthode doit être implémentée.")