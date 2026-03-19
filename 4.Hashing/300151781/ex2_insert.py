import os

def hash_simple_tp(mot):
    mapping = {"alice": 2, "bob": 1, "charlie": 4, "david": 4}
    return mapping.get(mot, 0)

table = [[] for _ in range(5)]
donnees = [("alice", 25), ("bob", 30), ("charlie", 28), ("david", 40)]

for c, v in donnees:
    index = hash_simple_tp(c)
    table[index].append((c, v))

os.makedirs("resultats", exist_ok=True)
with open("resultats/ex2.txt", "w") as f:
    for i, case in enumerate(table):
        fmt = str(case).replace(", ", ",")
        f.write(f"{i}:{fmt}\n")
        print(f"{i}:{fmt}")
