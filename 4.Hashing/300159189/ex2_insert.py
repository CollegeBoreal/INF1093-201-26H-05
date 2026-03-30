# ex2_insert.py

def hash_simple(mot, taille):
    return sum(ord(c) for c in mot) % taille

# créer la table de 5 "cases"
table = [[] for _ in range(5)]

def inserer(table, cle, valeur):
    h = hash_simple(cle, len(table))
    table[h].append((cle, valeur))

# insérer des valeurs
inserer(table, "alice", 25)
inserer(table, "bob", 30)
inserer(table, "charlie", 28)
inserer(table, "david", 40)

# écrire dans le fichier
with open("resultats/ex2.txt", "w") as f:
    for i, case in enumerate(table):
        f.write(f"{i}:{case}\n")

print("Exercice 2 terminé !")