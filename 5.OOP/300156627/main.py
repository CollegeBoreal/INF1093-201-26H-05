"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [Ton ID Boreal]
Date : 2026-03-30
"""
from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from Rectangle import Rectangle

def main():
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(5, 2),
        Rectangle(6, 3)
    ]

    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()