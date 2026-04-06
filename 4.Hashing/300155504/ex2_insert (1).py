def hash_simple(cle, taille):
    total = 0
    for lettre in cle:
        total += ord(lettre)
    return total % taille


def inserer(table, cle, valeur):
    index = hash_simple(cle, len(table))
    table[index].append((cle, valeur))


table = [[] for _ in range(5)]

donnees = [
    ("Badreddine", 92),
    ("Karim", 85),
    ("Sara", 78),
    ("Nour", 88),
    ("Amine", 74)
]

for cle, valeur in donnees:
    inserer(table, cle, valeur)


with open("resultats/ex2.txt", "w") as f:
    for i, case in enumerate(table):
        f.write(f"{i}:{case}\n")
