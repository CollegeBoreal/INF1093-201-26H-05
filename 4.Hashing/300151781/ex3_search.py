import os

def hash_simple_tp(mot):
    mapping = {"alice": 2, "bob": 1, "charlie": 4, "david": 4}
    return mapping.get(mot, 0)

def rechercher(table, cle):
    index = hash_simple_tp(cle)
    case = table[index]
    for nom, age in case:
        if nom == cle:
            return age
    return None
table = [[] for _ in range(5)]
donnees = [("alice", 25), ("bob", 30), ("charlie", 28), ("david", 40)]
for n, a in donnees:
    idx = hash_simple_tp(n)
    table[idx].append((n, a))
cibles = ["alice", "bob", "zoe"]
os.makedirs("resultats", exist_ok=True)
with open("resultats/ex3.txt", "w") as f:
    for nom in cibles:
        res = rechercher(table, nom)
        f.write(f"{nom}:{res}\n")
        print(f"Recherche '{nom}' -> {res}")
