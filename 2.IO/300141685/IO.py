import sys

try:
    etudiants = []

    with open("etudiants.txt", encoding="utf-8") as fichier:
        for ligne in fichier:
            texte = ligne.strip()

            if texte == "":
                continue

            elements = texte.split(",")

            if len(elements) != 2:
                raise ValueError

            nom = elements[0].strip()
            note = float(elements[1].strip())

            etudiants.append((nom, note))

    # calcul de la moyenne directement
    moyenne = sum(note for _, note in etudiants) / len(etudiants)

    with open("resultats.txt", "w", encoding="utf-8") as fichier_sortie:
        fichier_sortie.write("Étudiants ayant une note >= 60\n")

        for nom, note in etudiants:
            if note >= 60:
                fichier_sortie.write(f"{nom} - {note}\n")

        fichier_sortie.write(f"\nMoyenne : {round(moyenne, 2)}\n")

    print("Fichier traité avec succès.")

except FileNotFoundError:
    print("Le fichier etudiants.txt est introuvable.", file=sys.stderr)

except ValueError:
    print("Le fichier contient des données invalides.", file=sys.stderr)