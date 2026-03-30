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


table = [[] for _ in range(7)]

donnees = [
    ("madjid", 15),
    ("yanis", 90),
    ("mohamed", 58),
    ("abdenoor", 60),
    ("liza", 100)
    ("ryma", 88)
    ("lounes", 92)
]

for cle, valeur in donnees:
    inserer(table, cle, valeur)


cles_recherche = ["ajax", "bread", "zinzibar"]

with open("resultats/ex3.txt", "w") as f:
    for cle in cles_recherche:
        resultat = rechercher(table, cle)
        f.write(f"{cle}:{resultat}\n")
