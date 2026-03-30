import sys

fichier_entree = "etudiants.txt"
fichier_sortie = "resultats.txt"

try:
    notes = []
    admis = []

    with open(fichier_entree, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    if not lignes:
        raise ValueError("Le fichier etudiants.txt est vide.")

    for numero, ligne in enumerate(lignes, start=1):
        ligne = ligne.strip()

        if not ligne:
            continue

        morceaux = ligne.split()

        if len(morceaux) != 2:
            raise ValueError(f"Format invalide à la ligne {numero} : '{ligne}'")

        nom, note_str = morceaux

        try:
            note = float(note_str)
        except ValueError:
            raise ValueError(f"Note invalide à la ligne {numero} : '{note_str}'")

        notes.append(note)

        if note >= 60:
            admis.append((nom, note))

    if not notes:
        raise ValueError("Aucune note valide trouvée dans le fichier.")

    moyenne = sum(notes) / len(notes)

    with open(fichier_sortie, "w", encoding="utf-8") as f:
        f.write("Etudiants ayant une note >= 60\n")
        f.write("---------------------------------\n")
        for nom, note in admis:
            f.write(f"{nom} {note}\n")

        f.write("\n")
        f.write(f"Moyenne du groupe : {moyenne:.2f}\n")

    print("Traitement termine avec succes.")
    print(f"Le fichier '{fichier_sortie}' a ete genere.")

except FileNotFoundError:
    print(f"Erreur : le fichier '{fichier_entree}' est introuvable.", file=sys.stderr)
    sys.exit(1)

except ValueError as e:
    print(f"Erreur : {e}", file=sys.stderr)
    sys.exit(1)

except Exception as e:
    print(f"Erreur inattendue : {e}", file=sys.stderr)
    sys.exit(1)
