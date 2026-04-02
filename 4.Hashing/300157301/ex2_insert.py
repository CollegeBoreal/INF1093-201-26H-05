
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
    ("madjid", 15),
    ("ryma", 90),
    ("kader", 58),
    ("yanis", 60),
    ("lyes", 100)
]

for cle, valeur in donnees:
    inserer(table, cle, valeur)


with open("resultats/ex2.txt", "w") as f:
    for i, case in enumerate(table):
        f.write(f"{i}:{case}\n")
