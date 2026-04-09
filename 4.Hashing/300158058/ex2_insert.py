def calcul_hash(cle, taille_table):
    total = 0
    for caractere in cle:
        total += ord(caractere)
    return total % taille_table


def ajouter_donnee(table, cle, valeur):
    indice = calcul_hash(cle, len(table))
    table[indice].append((cle, valeur))


table_hachage = [[] for _ in range(6)]

etudiants = [
    ("Rabah", 88),
    ("Adam", 76),
    ("Sofia", 91),
    ("Nina", 84),
    ("Yanis", 79),
]

for nom, note in etudiants:
    ajouter_donnee(table_hachage, nom, note)

with open("resultats/ex2.txt", "w", encoding="utf-8") as fichier:
    for indice, contenu in enumerate(table_hachage):
        fichier.write(f"Case {indice}: {contenu}\n")
