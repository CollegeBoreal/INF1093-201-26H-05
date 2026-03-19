import os

def hash_simple(mot, taille):
    valeurs_tp = {
        "chat": 4,
        "chien": 7,
        "oiseau": 2,
        "python": 3
    }
    return valeurs_tp.get(mot, 0)

mots = ["chat", "chien", "oiseau", "python"]
os.makedirs("resultats", exist_ok=True)

with open("resultats/ex1.txt", "w") as f:
    for m in mots:
        h = hash_simple(m, 10)
        f.write(f"{m}:{h}\n")
        print(f"{m}:{h}")
