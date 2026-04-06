"""
Auteur : 300158035
Date : 2026-04-06
"""

from Carre import Carre
from Cercle import Cercle

def main():
    c1 = Carre(4)
    c2 = Cercle(3)

    print(c1.afficher_info())
    print(c2.afficher_info())

if __name__ == "__main__":
    main()
