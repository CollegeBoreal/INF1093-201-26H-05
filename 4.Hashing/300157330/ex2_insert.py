import os

def obtenir_position(cle, taille):
    total = 0
    for caractere in cle:
        total += ord(caractere)
    return total % taille

def inserer(table, cle, valeur):
    indice = obtenir_position(cle, len(table))
    table[indice].append((cle, valeur))

table = [[] for _ in range(5)]

donnees = [
    ("alice", 25),
    ("bob", 30),
    ("charlie", 28),
    ("david", 40)
]

for nom, age in donnees:
    inserer(table, nom, age)

os.makedirs("resultats", exist_ok=True)

with open("resultats/ex2.txt", "w", encoding="utf-8") as fichier:
    for i, contenu in enumerate(table):
        fichier.write(f"{i}:{contenu}\n")

print("Exercice 2 terminé")
