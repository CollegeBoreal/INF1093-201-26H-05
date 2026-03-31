"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [Ton ID Boreal]
Date : 2026-03-30
"""

from Carre import Carre
from Cercle import Cercle

def main():
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Affichage des informations
    print(c1.afficher_info())
    print(c2.afficher_info())

if __name__ == "__main__":
    main()

from Triangle import Triangle

formes = [Carre(4), Cercle(3), Triangle(5, 2)]
for f in formes:
    print(f.afficher_info())