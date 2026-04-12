def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total += ord(lettre)
    return total % taille


# Mots à traiter
mots = ["chat", "chien", "oiseau", "python"]
taille_table = 10

# Écriture du fichier resultats/ex1.txt
with open("resultats/ex1.txt", "w") as f:
    for mot in mots:
        f.write(f"{mot}:{hash_simple(mot, taille_table)}\n")

