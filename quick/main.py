<<<<<<< HEAD
with open('entree_quick.txt', 'r') as f:
    tab = list(map(int, f.read().split()))

def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab) // 2]
    gauche, milieu, droite = [], [], []
=======
def tri_rapide(tab):
    if len(tab) <= 1:
        return tab

    pivot = tab[len(tab) // 2]

    gauche = []
    milieu = []
    droite = []

>>>>>>> f75369750f191cd4ffd5a76d85918eca3211a2c2
    for x in tab:
        if x < pivot:
            gauche.append(x)
        elif x == pivot:
            milieu.append(x)
        else:
            droite.append(x)
<<<<<<< HEAD
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

tab_trie = tri_rapide(tab)
print('Résultat :', tab_trie)
=======

    return tri_rapide(gauche) + milieu + tri_rapide(droite)


with open("entree_quick.txt", "r") as f:
    tab = list(map(int, f.read().split()))

tab_trie = tri_rapide(tab)
print("Résultat :", tab_trie)
>>>>>>> f75369750f191cd4ffd5a76d85918eca3211a2c2
