"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré, un cercle et un triangle et affiche leurs informations.
Auteur : CHOUAIB AIT CHOUAIB
ID : 300155045
Date : 2026-04-06
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    """
    Fonction principale du programme.
    Crée les figures et affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Création d'un triangle de base 5 et hauteur 2
    c3 = Triangle(5, 2)

    formes = [c1, c2, c3]
    for f in formes:
        print(f"Aire: {f.aire():.2f} 📏")
        print(f.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()
