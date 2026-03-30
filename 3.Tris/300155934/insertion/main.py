def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i - 1
        # On décale les éléments plus grands que la clé vers la droite
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle

# Lecture du fichier
try:
    with open("entree_insertion.txt", "r") as f:
        tab = list(map(int, f.read().split()))

    print("Tableau original :   ", tab)
    tri_insertion(tab)
    print("Résultat Insertion :", tab)
except FileNotFoundError:
    print("Erreur : Le fichier entree_insertion.txt est introuvable.")