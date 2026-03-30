import os


def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total += ord(lettre)
    return total % taille


os.makedirs("resultats", exist_ok=True)

mots = ["chat", "chien", "oiseau", "python"]
taille_table = 10

with open("resultats/ex1.txt", "w", encoding="utf-8") as f:
    for mot in mots:
        valeur = hash_simple(mot, taille_table)
        f.write(f"{mot}:{valeur}\n")
