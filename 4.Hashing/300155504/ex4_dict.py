notes = {
    "Badreddine": 92,
    "Karim": 85,
    "Sara": 78,
    "Nour": 88,
    "Amine": 74
}

with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
