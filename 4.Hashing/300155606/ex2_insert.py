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

inserer(table, "alice", 25)
inserer(table, "bob", 30)
inserer(table, "charlie", 28)
inserer(table, "david", 40)

with open("resultats/ex2.txt", "w", encoding="utf-8") as f:
    for i in range(len(table)):
        f.write(f"{i}:{table[i]}\n")
