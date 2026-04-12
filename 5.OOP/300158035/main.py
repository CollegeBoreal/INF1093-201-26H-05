"""
Auteur : 300158035
Date : 2026-04-06
"""

from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle
from Triangle import Triangle

def main():
    c1 = Carre(4)
    c2 = Cercle(3)
    r = Rectangle(5, 3)
    t = Triangle(6, 2)

    print(c1.afficher_info())
    print(c2.afficher_info())
    print(r.afficher_info())
    print(t.afficher_info())

if __name__ == "__main__":
    main()
