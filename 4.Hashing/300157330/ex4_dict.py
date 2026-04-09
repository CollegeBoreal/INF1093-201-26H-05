import os

notes = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

os.makedirs("resultats", exist_ok=True)

with open("resultats/ex4.txt", "w", encoding="utf-8") as fichier:
    for nom, note in notes.items():
        fichier.write(f"{nom}:{note}\n")

print("Exercice 4 terminé")
