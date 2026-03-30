# ex1_hash.py
# Fonction de hachage simple

def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total += ord(lettre)
    return total % taille

mots = ["chat", "chien", "oiseau", "python"]
taille = 10

# Affichage
for mot in mots:
    print(f"{mot}:{hash_simple(mot, taille)}")

# Écriture dans resultats/ex1.txt
with open("resultats/ex1.txt", "w") as f:
    for mot in mots:
        f.write(f"{mot}:{hash_simple(mot, taille)}\n")

print("\n✅ Résultats sauvegardés dans resultats/ex1.txt")