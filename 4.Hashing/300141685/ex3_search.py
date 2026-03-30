# INF1093 - Programmation 2
# Hashing et Dictionnaires
# Nom: Souleymane Barry
# ID: 300141685
# Exercice 3 - Recherche dans une table de hachage

def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total = total + ord(lettre)
    return total % taille

def inserer(table, cle, valeur):
    index = hash_simple(cle, len(table))
    table[index].append((cle, valeur))

def rechercher(table, cle):
    index = hash_simple(cle, len(table))
    for c, v in table[index]:
        if c == cle:
            return v
    return None

table = [[] for _ in range(5)]

donnees = [("alice", 25), ("bob", 30), ("charlie", 28), ("david", 40)]

for cle, valeur in donnees:
    inserer(table, cle, valeur)

cles_a_chercher = ["alice", "bob", "zoe"]

with open("resultats/ex3.txt", "w", encoding="utf-8") as f:
    for cle in cles_a_chercher:
        resultat = rechercher(table, cle)
        if resultat is not None:
            f.write(f"{cle}:{resultat}\n")
        else:
            f.write(f"{cle}:None\n")

print("Exercice 3 termine - resultats/ex3.txt cree")
