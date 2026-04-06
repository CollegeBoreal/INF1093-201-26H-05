"""
Exercice : Tri de Shell
Nom : Rabah Belaid
ID : 300158058
"""

def lire_tableau(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return [int(x) for x in f.read().split()]

def tri_shell(tab):
    n = len(tab)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = tab[i]
            j = i
            while j >= gap and tab[j - gap] > temp:
                tab[j] = tab[j - gap]
                j -= gap
            tab[j] = temp
        gap //= 2
    return tab

def main():
    tableau = lire_tableau("entree_shell.txt")
    print("Tableau avant tri :", tableau)
    resultat = tri_shell(tableau)
    print("Tableau après tri :", resultat)

if __name__ == "__main__":
    main()
