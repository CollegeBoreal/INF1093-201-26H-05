with open("entree_quick.txt", "r") as f:
    tab = list(map(int, f.read().split()))

def tri_rapide(tab):
    if len(tab) <= 1:  # SI longueur(tab) ≤ 1
        return tab     # RETOURNER tab
    
    pivot = tab[len(tab) // 2]  # pivot ← tab[longueur(tab) ÷ 2]
    
    gauche = []    # liste vide
    milieu = []
    droite = []
    
    for x in tab:  # POUR chaque élément x DANS tab
        if x < pivot:      # SI x < pivot
            gauche.append(x)
        elif x == pivot:   # SINON SI x = pivot
            milieu.append(x)
        else:              # SINON
            droite.append(x)
    
    # RETOURNER concaténer(tri_rapide(gauche), milieu, tri_rapide(droite))
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

print("Avant:", tab)
tab_trie = tri_rapide(tab)
print("Après:", tab_trie)
