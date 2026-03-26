<<<<<<< HEAD
with open('entree_insertion.txt', 'r') as f:
    tab = list(map(int, f.read().split()))

=======
>>>>>>> f75369750f191cd4ffd5a76d85918eca3211a2c2
def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i - 1
<<<<<<< HEAD
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle

tri_insertion(tab)
print('Résultat :', tab)
=======

        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1

        tab[j + 1] = cle


with open("entree_insertion.txt", "r") as f:
    tab = list(map(int, f.read().split()))

tri_insertion(tab)
print("Résultat :", tab)
>>>>>>> f75369750f191cd4ffd5a76d85918eca3211a2c2
