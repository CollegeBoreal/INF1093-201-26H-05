def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total += ord(lettre)
    return total % taille

mots = ["chat", "chien", "oiseau", "python"]

with open("resultats/ex1.txt", "w") as f:
    for mot in mots:
        h = hash_simple(mot, 10)
        f.write(f"{mot}:{h}\n")