def hash_fixe(cle):
    if cle == "alice":
        return 2
    if cle == "bob":
        return 1
    if cle == "charlie":
        return 4
    if cle == "david":
        return 4

def inserer(table, cle, valeur):
    index = hash_fixe(cle)
    table[index].append((cle, valeur))

table = [[] for _ in range(5)]

inserer(table, "alice", 25)
inserer(table, "bob", 30)
inserer(table, "charlie", 28)
inserer(table, "david", 40)

with open("resultats/ex2.txt", "w") as f:
    for i, case in enumerate(table):
        f.write(f"{i}:{case}\n")
