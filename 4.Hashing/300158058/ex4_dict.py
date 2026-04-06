notes_etudiants = {
    "Rabah": 88,
    "Adam": 76,
    "Sofia": 91,
    "Nina": 84,
    "Yanis": 79
}

with open("resultats/ex4.txt", "w", encoding="utf-8") as fichier:
    for nom, note in notes_etudiants.items():
        fichier.write(f"{nom} = {note}\n")
