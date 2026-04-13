"""
Exercice : Tri rapide
Nom : Rabah Belaid
ID : 300158058
"""

def lire_tableau(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return [int(x) for x in f.read().split()]

def quick_sort(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[0]
    plus_petits = [x for x in tab[1:] if x <= pivot]
    plus_grands = [x for x in tab[1:] if x > pivot]
    return quick_sort(plus_petits) + [pivot] + quick_sort(plus_grands)

def main():
    tableau = lire_tableau("entree_quick.txt")
    print("Tableau avant tri :", tableau)
    resultat = quick_sort(tableau)
    print("Tableau après tri :", resultat)

if __name__ == "__main__":
    main()
