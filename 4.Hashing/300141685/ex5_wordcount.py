# INF1093 - Programmation 2
# Hashing et Dictionnaires
# Nom: Souleymane Barry
# ID: 300141685
# Exercice 5 - Compteur de mots

texte = "python est simple et python est puissant"

mots = texte.split()
compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] = compteur[mot] + 1
    else:
        compteur[mot] = 1

with open("resultats/ex5.txt", "w", encoding="utf-8") as f:
    for mot, nombre in compteur.items():
        f.write(f"{mot}:{nombre}\n")

print("Exercice 5 termine - resultats/ex5.txt cree")
