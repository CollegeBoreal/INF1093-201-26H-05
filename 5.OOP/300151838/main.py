"""
Fichier : main.py
Description : Point d'entrée du programme. Crée plusieurs figures et affiche leurs informations.
Auteur : abdelkader.messali
Date : 2026-04-06
"""

from carre import Carre
from cercle import Cercle
from Triangle import Triangle
from Cube import Cube


def main():
    """
    Fonction principale du programme.
    Crée des figures, puis affiche leurs informations.
    """
    formes = [Carre(4), Cercle(3), Triangle(5, 2), Cube(3)]

    for forme in formes:
        print(forme.afficher_info())
        print(f"Aire: {forme.aire()} 📏")
        if hasattr(forme, "volume"):
            print(f"Volume: {forme.volume()} 🧊")


if __name__ == "__main__":
    main()
