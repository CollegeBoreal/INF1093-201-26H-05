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

inserer(table, "alice", 25)
inserer(table, "bob", 30)
inserer(table, "charlie", 28)
inserer(table, "david", 40)

cles = ["alice", "bob", "zoe"]

with open("resultats/ex3.txt", "w") as f:
    for cle in cles:
        resultat = rechercher(table, cle)
        f.write(f"{cle}:{resultat}\n")