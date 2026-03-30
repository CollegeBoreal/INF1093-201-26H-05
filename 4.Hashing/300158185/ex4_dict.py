notes = {
    "Nasro": 15,
    "Djawed": 90,
    "Lahlou": 58,
    "Ahmed": 60,
    "Sara": 100
}

with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
