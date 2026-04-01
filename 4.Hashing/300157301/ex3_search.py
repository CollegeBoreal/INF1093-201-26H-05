
def hash_simple(cle, taille):
    total = 0
    for lettre in cle:
        total += ord(lettre)
    return total % taille


def inserer(table, cle, valeur):
    index = hash_simple(cle, len(table))
    table[index].append((cle, valeur))


def rechercher(table, cle):
    index = hash_simple(cle, len(table))
    for k, v in table[index]:
        if k == cle:
            return v
    return None


table = [[] for _ in range(5)]

donnees = [
    ("madjid", 15),
    ("ryma", 90),
    ("kader", 58),
    ("yanis", 60),
    ("lyes", 60)
]

for cle, valeur in donnees:
    inserer(table, cle, valeur)


cles_recherche = ["alice", "bob", "zoe"]

with open("resultats/ex3.txt", "w") as f:
    for cle in cles_recherche:
        resultat = rechercher(table, cle)
        f.write(f"{cle}:{resultat}\n")
