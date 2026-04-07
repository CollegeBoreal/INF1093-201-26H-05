def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total += ord(lettre)
    return total % taille

mots = ["chat", "chien", "oiseau", "python"]
table_taille = 10

with open("resultats/ex1.txt", "w", encoding="utf-8") as f:
    for mot in mots:
        valeur = hash_simple(mot, table_taille)
        f.write(f"{mot}:{valeur}\n")
