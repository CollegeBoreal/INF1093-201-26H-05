try:
    total = 0
    count = 0
    admis = []

    with open("etudiants.txt", "r") as f:
        for ligne in f:
            nom, note = ligne.split()
            note = float(note)

            total += note
            count += 1

            if note >= 60:
                admis.append(f"{nom} {note}")

    moyenne = total / count

    with open("resultats.txt", "w") as f_out:
        f_out.write("Étudiants admis (>=60):\n")
        for e in admis:
            f_out.write(e + "\n")

        f_out.write(f"\nMoyenne du groupe: {moyenne:.2f}")

    print("Traitement terminé ✔")

except FileNotFoundError:
    print("Erreur : fichier etudiants.txt introuvable")

except ValueError:
    print("Erreur : format invalide dans le fichier")
