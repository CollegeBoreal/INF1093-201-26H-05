"""
Fichier : main.py
Description : Point d'entrée du programme. Crée plusieurs formes et affiche leurs informations.
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from Rectangle import Rectangle
from Losange import Losange
from Trapeze import Trapeze
from Parallelogramme import Parallelogramme
from Pentagone import Pentagone
from Hexagone import Hexagone
from Octogone import Octogone
from Ellipse import Ellipse
from Etoile import Etoile
from Cube3D import Cube3D

def main():
    """
    Fonction principale du programme.
    Crée plusieurs formes et affiche leurs informations.
    """

    # Création des formes
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(3, 4,),
        Rectangle(4, 6),
        Losange(5, 6),
        Trapeze(3, 5, 4),
        Parallelogramme(4, 5),
        Pentagone(3),
        Hexagone(3),
        Octogone(3),
        Ellipse(4, 2),
        Etoile(5,2),
        Cube3D(3)
    ]

    # Affichage des informations
    for forme in formes:
        print("-------------")
        print(forme.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()