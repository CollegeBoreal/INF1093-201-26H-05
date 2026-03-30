def insertion_sort(liste):
    for i in range(1, len(liste)):
        valeur = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > valeur:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = valeur
    return liste

with open("entree_insertion.txt", "r") as f:
    data = list(map(int, f.read().split()))

print("Résultat :", insertion_sort(data))
