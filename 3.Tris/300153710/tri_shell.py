# Lecture du fichier
with open("entree_shell.txt", "r") as f:
    tab = list(map(int, f.read().split()))

# Algorithme tri de Shell
def tri_shell(tab):
    n = len(tab)
    ecart = n // 2

    while ecart > 0:
        for i in range(ecart, n):
            temp = tab[i]
            j = i

            while j >= ecart and tab[j - ecart] > temp:
                tab[j] = tab[j - ecart]
                j = j - ecart

            tab[j] = temp

        ecart = ecart // 2

    return tab

# Programme principal
tab_trie = tri_shell(tab)
print("Résultat :", tab_trie)
