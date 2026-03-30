def calcul_hash(cle, taille_table):
    valeur = 0
    for caractere in cle:
        valeur += ord(caractere)
    return valeur % taille_table


def inserer(table, cle, valeur):
    indice = calcul_hash(cle, len(table))
    table[indice].append((cle, valeur))


def chercher(table, cle):
    indice = calcul_hash(cle, len(table))
    for element_cle, element_valeur in table[indice]:
        if element_cle == cle:
            return element_valeur
    return None


table = [[] for _ in range(6)]

donnees = [
    ("Rabah", 88),
    ("Adam", 76),
    ("Sofia", 91),
    ("Nina", 84),
    ("Yanis", 79),
]

for cle, valeur in donnees:
    inserer(table, cle, valeur)

recherches = ["Rabah", "Nina", "Karim"]

with open("resultats/ex3.txt", "w", encoding="utf-8") as fichier:
    for nom in recherches:
        resultat = chercher(table, nom)
        fichier.write(f"{nom}: {resultat}\n")
