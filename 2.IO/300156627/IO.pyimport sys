import sys

try:
    with open("etudiants.txt", "r", encoding="utf-8") as f:
        lignes = f.readlines()

    etudiants = []
    notes = []

    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne:
            continue

        parties = ligne.split(",")

        if len(parties) != 2:
            raise ValueError("Format incorrect")

        nom = parties[0].strip()
        note = float(parties[1].strip())

        etudiants.append((nom, note))
        notes.append(note)

    moyenne = sum(notes) / len(notes)

    with open("resultats.txt", "w", encoding="utf-8") as out:
        out.write("Étudiant.e.s ayant ≥ 60 :\n")
        for nom, note in etudiants:
            if note >= 60:
                out.write(f"{nom} : {note}\n")

        out.write(f"\nMoyenne du groupe : {moyenne:.2f}\n")

    print("Traitement terminé.")

except FileNotFoundError:
    print("Erreur : fichier etudiants.txt introuvable.", file=sys.stderr)

except ValueError:
    print("Erreur : format invalide dans le fichier.", file=sys.stderr)
