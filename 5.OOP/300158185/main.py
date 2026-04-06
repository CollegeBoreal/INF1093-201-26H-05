"""
Fichier : main.py
Description : Point d'entrée du programme. Crée plusieurs figures et affiche leurs informations.
Auteur : ahmed.bergui
Date : 2026-03-25
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle



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
