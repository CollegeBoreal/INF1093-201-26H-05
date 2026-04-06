# ex3_search.py
# Recherche dans une table de hachage

def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
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

# Créer et remplir la table
table = [[] for _ in range(5)]
inserer(table, "alice", 25)
inserer(table, "bob", 30)
inserer(table, "charlie", 28)
inserer(table, "david", 40)

# Rechercher
mots = ["alice", "bob", "zoe"]
for mot in mots:
    print(f"{mot}:{rechercher(table, mot)}")

# Écriture dans resultats/ex3.txt
with open("resultats/ex3.txt", "w") as f:
    for mot in mots:
        f.write(f"{mot}:{rechercher(table, mot)}\n")

print("\n✅ Résultats sauvegardés dans resultats/ex3.txt")
