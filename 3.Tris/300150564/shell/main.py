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


with open("entree_shell.txt", "r") as f:
    tab = list(map(int, f.read().split()))

tri_shell(tab)
print("Résultat :", tab)