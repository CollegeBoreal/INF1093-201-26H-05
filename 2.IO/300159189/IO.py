notes = []
admis = []

try:
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            nom, note = ligne.split()
            note = float(note)
            notes.append(note)

            if note >= 60:
                admis.append(f"{nom} {note}")

    moyenne = sum(notes) / len(notes)

    with open("resultats.txt", "w") as f:
        f.write("Étudiants admis (>=60):\n")
        for a in admis:
            f.write(a + "\n")

        f.write(f"\nMoyenne: {moyenne:.2f}\n")

    print("Traitement terminé.")

except Exception as e:
    print("Erreur :", e)
