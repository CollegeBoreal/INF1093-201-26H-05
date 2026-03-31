# ex1_hash.py
def hash_simple(mot, taille):
    # additionner les codes ASCII et faire modulo taille
    return sum(ord(c) for c in mot) % taille

mots = ["chat", "chien", "oiseau", "python"]
taille_table = 10

with open("resultats/ex1.txt", "w") as f:
    for mot in mots:
        h = hash_simple(mot, taille_table)
        f.write(f"{mot}:{h}\n")

print("Exercice 1 terminé !")