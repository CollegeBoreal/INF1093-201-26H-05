import os


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


os.makedirs("resultats", exist_ok=True)

table = [[] for _ in range(5)]
donnees = [
    ("alice", 25),
    ("bob", 30),
    ("charlie", 28),
    ("david", 40),
]

for cle, valeur in donnees:
    inserer(table, cle, valeur)

cles_recherche = ["alice", "bob", "zoe"]

with open("resultats/ex3.txt", "w", encoding="utf-8") as f:
    for cle in cles_recherche:
        resultat = rechercher(table, cle)
        f.write(f"{cle}:{resultat}\n")
