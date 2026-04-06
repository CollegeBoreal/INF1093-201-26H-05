import os

os.makedirs("resultats", exist_ok=True)

texte = "python est simple et python est puissant"
mots = texte.split()

compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

with open("resultats/ex5.txt", "w", encoding="utf-8") as f:
    for mot, nb in compteur.items():
        f.write(f"{mot}:{nb}\n")
