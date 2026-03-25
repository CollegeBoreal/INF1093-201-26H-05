# INF1093 - Programmation 2
# Hashing et Dictionnaires
# Nom: Souleymane Barry
# ID: 300141685
# Exercice 4 - Dictionnaires Python

notes = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

with open("resultats/ex4.txt", "w", encoding="utf-8") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")

print("Exercice 4 termine - resultats/ex4.txt cree")
