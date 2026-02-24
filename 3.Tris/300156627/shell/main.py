with open('entree_shell.txt', 'r') as f:
    tab = list(map(int, f.read().split()))

def tri_shell(tab):
    n = len(tab)
    ecart = n // 2
    while ecart > 0:
        for i in range(ecart, n):
            temp = tab[i]
            j = i
            while j >= ecart and tab[j - ecart] > temp:
                tab[j] = tab[j - ecart]
                j -= ecart
            tab[j] = temp
        ecart //= 2

tri_shell(tab)
print('Resultat :', tab)
