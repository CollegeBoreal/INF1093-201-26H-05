"""
Fichier : main.py
Point d'entrée du programme
Auteur : 300159189
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():

    # Création des figures
    c1 = Carre(4)
    c2 = Cercle(3)
    t1 = Triangle(5, 2)

    # Liste des formes
    formes = [c1, c2, t1]

    # Affichage
    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()
