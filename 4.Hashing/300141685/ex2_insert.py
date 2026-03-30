# INF1093 - Programmation 2
# Hashing et Dictionnaires
# Nom: Souleymane Barry
# ID: 300141685
# Exercice 2 - Insertion dans une table de hachage

def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total = total + ord(lettre)
    return total % taille

def inserer(table, cle, valeur):
    index = hash_simple(cle, len(table))
    table[index].append((cle, valeur))

table = [[] for _ in range(5)]

donnees = [("alice", 25), ("bob", 30), ("charlie", 28), ("david", 40)]

for cle, valeur in donnees:
    inserer(table, cle, valeur)

with open("resultats/ex2.txt", "w", encoding="utf-8") as f:
    for i, bucket in enumerate(table):
        if bucket:
            elements = []
            for elem in bucket:
                elements.append(f"('{elem[0]}',{elem[1]})")
            f.write(f"{i}:{elements}\n")
        else:
            f.write(f"{i}:[]\n")

print("Exercice 2 termine - resultats/ex2.txt cree")
