from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from graphique import afficher_carre, afficher_cercle, afficher_triangle

def main():
    # Création des figures
    formes = [Carre(4), Cercle(3), Triangle(5, 2)]
    
    # Affichage des informations dans la console
    for f in formes:
        print(f.afficher_info())

    # Affichage graphique des figures
    afficher_carre(formes[0])
    afficher_cercle(formes[1])
    afficher_triangle(formes[2])

# Point d'entrée du programme
if __name__ == "__main__":
    main()