import os

def calculer_valeur(mot, taille):
    somme = 0
    for lettre in mot:
        somme += ord(lettre)
    return somme % taille

mots = ["chat", "chien", "oiseau", "python"]

os.makedirs("resultats", exist_ok=True)

with open("resultats/ex1.txt", "w", encoding="utf-8") as fichier:
    for mot in mots:
        resultat = calculer_valeur(mot, 10)
        fichier.write(f"{mot}:{resultat}\n")

print("Exercice 1 terminé")
