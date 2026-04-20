"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : 300155488
Date : 2026-04-20
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    """
    Fonction principale du programme.
    Crée un carré et un cercle, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)
    t1=Triangle(5,2)

    # Affichage des informations des deux figures
    print(c1.afficher_info())
    print(c2.afficher_info())
    print(t1.afficher_info())

    # Démonstration du POLYMORPHISME
    formes = [c1, c2, t1]
    for f in formes:
        print(f"Aire: {f.aire()}")

# Point d'entrée du programme
if __name__ == "__main__":
    main()