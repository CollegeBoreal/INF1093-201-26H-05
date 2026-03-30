"""
Fichier : main.py
Description : Programme principal pour tester les classes de formes géométriques.
Auteur : BELAID Rabah
ID : 300158058
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from Cube import Cube

def main():
    figures = [
        Carre(5),
        Cercle(4),
        Triangle(6, 3),
        Cube(2)
    ]

    print("=== Test du projet POO ===")
    for figure in figures:
        print(figure.afficher_info())
        print(f"Aire calculée : {figure.aire()}")
        if hasattr(figure, "volume"):
            print(f"Volume calculé : {figure.volume()}")
        print("-" * 40)

if __name__ == "__main__":
    main()
