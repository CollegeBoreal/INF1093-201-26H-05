from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    liste_figures = [
        Carre(5),
        Cercle(2),
        Triangle(6, 3)
    ]

    print("=== Résultats du projet POO ===")
    for figure in liste_figures:
        print(figure.description())

if __name__ == "__main__":
    main()
