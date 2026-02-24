with open('entree_quick.txt', 'r') as f:
    tab = list(map(int, f.read().split()))

def quick_sort(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[0]
    gauche = [x for x in tab[1:] if x <= pivot]
    droite = [x for x in tab[1:] if x > pivot]
    return quick_sort(gauche) + [pivot] + quick_sort(droite)

tab = quick_sort(tab)
print('Resultat :', tab)
