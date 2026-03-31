with open("entree_quick.txt", "r") as f:
    tab = list(map(int, f.read().split()))

def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab) // 2]
    gauche, milieu, droite = [], [], []
    for x in tab:
        if x < pivot:
            gauche.append(x)
        elif x == pivot:
            milieu.append(x)
        else:
            droite.append(x)
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

print("Résultat Quick :", tri_rapide(tab))
