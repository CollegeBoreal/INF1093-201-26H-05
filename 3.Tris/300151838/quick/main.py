def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste)//2]
    left = [x for x in liste if x < pivot]
    middle = [x for x in liste if x == pivot]
    right = [x for x in liste if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

with open("entree_quick.txt", "r") as f:
    data = list(map(int, f.read().split()))

print("Résultat :", quick_sort(data))
