notes = {
    "aymen": 15,
    "Mellissa": 90,
    "Rabah": 58,
    "Ibrahim": 60,
    "walid": 100
}

with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
