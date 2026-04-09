import os

def calcul_index(cle, taille):
    return sum(ord(c) for c in cle) % taille

def inserer(table, cle, valeur):
    indice = calcul_index(cle, len(table))
    table[indice].append((cle, valeur))

def rechercher(table, cle):
    indice = calcul_index(cle, len(table))
    for nom, valeur in table[indice]:
        if nom == cle:
            return valeur
    return None

table = [[] for _ in range(5)]

for nom, age in [("alice", 25), ("bob", 30), ("charlie", 28), ("david", 40)]:
    inserer(table, nom, age)

recherches = ["alice", "bob", "zoe"]

os.makedirs("resultats", exist_ok=True)

with open("resultats/ex3.txt", "w", encoding="utf-8") as fichier:
    for element in recherches:
        fichier.write(f"{element}:{rechercher(table, element)}\n")

print("Exercice 3 terminé")
