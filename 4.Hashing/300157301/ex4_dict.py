
notes = {
    "madjid": 15,
    "ryma": 90,
    "kader": 58,
    "yanis": 60,
    "lyes": 100
}

with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
