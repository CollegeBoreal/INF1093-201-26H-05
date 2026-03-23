def shell_sort(liste):
    n = len(liste)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = liste[i]
            j = i
            while j >= gap and liste[j-gap] > temp:
                liste[j] = liste[j-gap]
                j -= gap
            liste[j] = temp
        gap //= 2
    return liste

with open("entree_shell.txt", "r") as f:
    data = list(map(int, f.read().split()))

print("Résultat :", shell_sort(data))
