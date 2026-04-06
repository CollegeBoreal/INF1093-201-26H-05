"""
Exercice : Tri par insertion
Nom : Rabah Belaid
ID : 300158058
"""

def lire_tableau(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return [int(x) for x in f.read().split()]

def tri_insertion(tab):
    for i in range(1, len(tab)):
        valeur = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > valeur:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = valeur
    return tab

def main():
    tableau = lire_tableau("entree_insertion.txt")
    print("Tableau avant tri :", tableau)
    resultat = tri_insertion(tableau)
    print("Tableau après tri :", resultat)

if __name__ == "__main__":
    main()
