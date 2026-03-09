notes = []
reussite = []

try:
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            nom, note = ligne.split()
            note = int(note)
            notes.append(note)

            if note >= 60:
                reussite.append(f"{nom} {note}")

    moyenne = sum(notes) / len(notes)

    with open("resultats.txt", "w") as f:
        f.write("Étudiants ayant >= 60\n")

        for etu in reussite:
            f.write(etu + "\n")

        f.write("\nMoyenne du groupe : " + str(moyenne))

    print("Traitement terminé")

except FileNotFoundError:
    print("Erreur : fichier etudiants.txt introuvable")

except ValueError:
    print("Erreur : format invalide")