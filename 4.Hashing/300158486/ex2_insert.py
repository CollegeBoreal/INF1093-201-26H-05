import os


def hash_simple(cle, taille):
    total = 0
    for lettre in cle:
        total += ord(lettre)
    return total % taille


def inserer(table, cle, valeur):
    index = hash_simple(cle, len(table))
    table[index].append((cle, valeur))


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

with open("resultats/ex2.txt", "w", encoding="utf-8") as f:
    for i, case in enumerate(table):
        f.write(f"{i}:{case}\n")
