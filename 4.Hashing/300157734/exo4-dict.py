notes = {
    "madjid": 15,
    "yanis": 90,
    "mohamed": 58,
    "abdenoor": 60,
    "liza": 100
    "ryma": 100
    "lounes": 100
}

with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
