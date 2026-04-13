# ex2_insert.py
# Insertion dans une table de hachage

def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total += ord(lettre)
    return total % taille

def inserer(table, cle, valeur):
    index = hash_simple(cle, len(table))
    table[index].append((cle, valeur))

# Créer une table de taille 5
table = [[] for _ in range(5)]

# Insérer les données
inserer(table, "alice", 25)
inserer(table, "bob", 30)
inserer(table, "charlie", 28)
inserer(table, "david", 40)

# Affichage
for i, case in enumerate(table):
    print(f"{i}:{case}")

# Écriture dans resultats/ex2.txt
with open("resultats/ex2.txt", "w") as f:
    for i, case in enumerate(table):
        f.write(f"{i}:{case}\n")

print("\n✅ Résultats sauvegardés dans resultats/ex2.txt")
