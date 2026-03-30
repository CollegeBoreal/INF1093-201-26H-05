"""
Fichier : main.py
Description : Point d'entrée du programme.
Auteur : Ouassim Ahmed Benamira
Date : 2026-03-30
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    formes = [Carre(4), Cercle(3), Triangle(5, 2)]
    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()