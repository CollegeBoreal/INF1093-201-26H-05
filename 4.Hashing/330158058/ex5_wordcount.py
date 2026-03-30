phrase = "python est rapide et python est pratique pour apprendre python"
liste_mots = phrase.split()

frequences = {}

for mot in liste_mots:
    if mot in frequences:
        frequences[mot] += 1
    else:
        frequences[mot] = 1

with open("resultats/ex5.txt", "w", encoding="utf-8") as fichier:
    for mot, nombre in frequences.items():
        fichier.write(f"{mot}: {nombre}\n")
