import os


os.makedirs("resultats", exist_ok=True)

notes = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
}

with open("resultats/ex4.txt", "w", encoding="utf-8") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
