import os


notes = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}
os.makedirs("resultats", exist_ok=True)
with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")
        print(f"Enregistré : {nom} a obtenu {note}/100")
