# INF1093 - Programmation 2 - POO
# Souleymane Barry - 300141685

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    print("=" * 50)
    print("PROJET POO - FORMES GEOMETRIQUES")
    print("Souleymane Barry - 300141685")
    print("=" * 50)

    carre = Carre(4)
    cercle = Cercle(3)
    triangle = Triangle(5, 2)

    figures = [carre, cercle, triangle]

    print("\n--- INFORMATIONS DES FIGURES ---")
    for f in figures:
        print(f.afficher_info())

    print("\n--- AIRES ---")
    for f in figures:
        print(f"Aire du {f.nom}: {f.aire():.2f}")

    print("\n--- PERIMETRES ---")
    for f in figures:
        print(f"Perimetre du {f.nom}: {f.perimetre():.2f}")

if __name__ == "__main__":
    main()
