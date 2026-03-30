# ex3_search.py

def hash_simple(mot, taille):
    return sum(ord(c) for c in mot) % taille

# même table que dans ex2
table = [[] for _ in range(5)]
table[hash_simple("alice",5)].append(("alice",25))
table[hash_simple("bob",5)].append(("bob",30))
table[hash_simple("charlie",5)].append(("charlie",28))
table[hash_simple("david",5)].append(("david",40))

def rechercher(table, cle):
    h = hash_simple(cle, len(table))
    for k, v in table[h]:
        if k == cle:
            return v
    return None

cles_a_rechercher = ["alice", "bob", "zoe"]

with open("resultats/ex3.txt", "w") as f:
    for cle in cles_a_rechercher:
        valeur = rechercher(table, cle)
        f.write(f"{cle}:{valeur}\n")

print("Exercice 3 terminé !")