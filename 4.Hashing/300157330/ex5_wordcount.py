import os

texte = "python est simple et python est puissant"
compteur = {}

for mot in texte.split():
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

os.makedirs("resultats", exist_ok=True)

with open("resultats/ex5.txt", "w", encoding="utf-8") as fichier:
    for mot, nombre in compteur.items():
        fichier.write(f"{mot}:{nombre}\n")

print("Exercice 5 terminé")
