# ex4_dict.py
# Dictionnaires Python

notes = {}

# Ajouter les étudiants
notes["Alice"] = 85
notes["Bob"] = 78
notes["Charlie"] = 92
notes["Diana"] = 88

# Affichage
for nom, note in notes.items():
    print(f"{nom}:{note}")

# Écriture dans resultats/ex4.txt
with open("resultats/ex4.txt", "w") as f:
    for nom, note in notes.items():
        f.write(f"{nom}:{note}\n")

print("\n✅ Résultats sauvegardés dans resultats/ex4.txt")
