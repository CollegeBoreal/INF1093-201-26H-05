# ex5_wordcount.py
# Compteur de mots

texte = "python est simple et python est puissant"
mots = texte.split()

compteur = {}
for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

# Affichage
for mot, count in compteur.items():
    print(f"{mot}:{count}")

# Écriture dans resultats/ex5.txt
with open("resultats/ex5.txt", "w") as f:
    for mot, count in compteur.items():
        f.write(f"{mot}:{count}\n")

print("\n✅ Résultats sauvegardés dans resultats/ex5.txt")