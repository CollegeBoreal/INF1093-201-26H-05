# ex5_wordcount.py

texte = "python est simple et python est puissant"
mots = texte.split()

compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1

with open("resultats/ex5.txt", "w") as f:
    for mot, count in compteur.items():
        f.write(f"{mot}:{count}\n")

print("Exercice 5 terminé !")