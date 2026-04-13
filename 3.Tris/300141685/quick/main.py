def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab) // 2]
    gauche = [x for x in tab if x < pivot]
    milieu = [x for x in tab if x == pivot]
    droite = [x for x in tab if x > pivot]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

with open("entree_quick.txt", "r") as f:
    tab = list(map(int, f.read().split()))

print("Avant tri :", tab)
tab_trie = tri_rapide(tab)
print("Apres tri :", tab_trie)
