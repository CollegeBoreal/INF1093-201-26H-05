with open('entree_insertion.txt', 'r') as f:
    tab = list(map(int, f.read().split()))

def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle

tri_insertion(tab)
print('Resultat :', tab)
