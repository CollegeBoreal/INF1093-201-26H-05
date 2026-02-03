# IO.py
# Traitement des entrées/sorties
# ID : 300156627

total = 0
count = 0
admis = []

with open("entree.txt", "r") as f:
    for ligne in f:
        ligne = ligne.strip()
        if not ligne:
            continue

        nom, note = ligne.split()
        note = float(note)

        total += note
        count += 1

        if note >= 60:
            admis.append(f"{nom} {note}")

moyenne = total / count

with open("resultats.txt", "w") as f:
    f.write("Étudiants admis (>=60):\n")
    for a in admis:
        f.write(a + "\n")

    f.write(f"\nMoyenne du groupe : {moyenne:.2f}\n")

print("Traitement terminé avec succès.")

