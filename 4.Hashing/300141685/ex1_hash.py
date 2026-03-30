# INF1093 - Programmation 2
# Hashing et Dictionnaires
# Nom: Souleymane Barry
# ID: 300141685
# Exercice 1 - Fonction de hachage

def hash_simple(mot, taille):
    total = 0
    for lettre in mot:
        total = total + ord(lettre)
    return total % taille

mots = ["chat", "chien", "oiseau", "python"]
taille_table = 10

with open("resultats/ex1.txt", "w", encoding="utf-8") as f:
    for mot in mots:
        valeur_hash = hash_simple(mot, taille_table)
        f.write(f"{mot}:{valeur_hash}\n")

print("Exercice 1 termine - resultats/ex1.txt cree")
