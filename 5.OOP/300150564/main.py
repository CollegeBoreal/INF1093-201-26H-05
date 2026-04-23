"""
Fichier : main.py
Description : Point d'entree du programme.
Auteur : Ouassim Ahmed Benamira
Date : 2026-04-13
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from Losange import Losange
from Rectangle import Rectangle
from Pentagone import Pentagone
from Etoile import Etoile

def main():
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(5, 2),
        Losange(6, 4),
        Rectangle(5, 3),
        Pentagone(4),
        Etoile(5, 2)
    ]
    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()