notes = []
etudiants_reussite = []

try:
    with open("etudiants.txt", "r", encoding="utf-8") as fichier:
        for numero_ligne, ligne in enumerate(fichier, start=1):
            ligne = ligne.strip()

            if not ligne:
                continue  # ignore les lignes vides

            parties = ligne.split()

            if len(parties) != 2:
                raise ValueError(f"Format invalide à la ligne {numero_ligne}: {ligne}")

            nom, note_str = parties

            try:
                note = float(note_str)
            except ValueError:
                raise ValueError(f"Note invalide à la ligne {numero_ligne}: {note_str}")

            notes.append(note)

            if note >= 60:
                etudiants_reussite.append((nom, note))

    if len(notes) == 0:
        raise ValueError("Le fichier etudiants.txt est vide.")

    moyenne = sum(notes) / len(notes)

    with open("resultats.txt", "w", encoding="utf-8") as sortie:
        sortie.write("Étudiant.e.s ayant une note >= 60\n")
        sortie.write("--------------------------------\n")

        for nom, note in etudiants_reussite:
            sortie.write(f"{nom} {note}\n")

        sortie.write("\n")
        sortie.write(f"Moyenne du groupe : {moyenne:.2f}\n")

    print("Traitement terminé avec succès. Le fichier resultats.txt a été créé.")

except FileNotFoundError:
    print("Erreur : le fichier etudiants.txt est introuvable.", file=__import__("sys").stderr)

except ValueError as e:
    print(f"Erreur : {e}", file=__import__("sys").stderr)
