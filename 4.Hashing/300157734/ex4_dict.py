notes = {
    "madjid": 15,
    "yanis": 90,
    "mohamed": 58,
    "abdenoor": 60,
    "liza": 100
    "ryma": 88
    "lounes": 92
}

with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
