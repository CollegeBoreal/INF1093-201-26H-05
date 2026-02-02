# IO.py

def main():
    try:
        # Ouvrir le fichier d'entrée
        with open("etudiants.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()

        etudiants_reussis = []
        total_notes = 0
        nombre_etudiants = 0

        # Traitement des lignes
        for ligne in lignes:
            ligne = ligne.strip()

            # Ignorer les lignes vides
            if not ligne:
                continue

            try:
                nom, note = ligne.split()
                note = float(note)
            except ValueError:
                print(f"Format invalide ignoré : {ligne}")
                continue

            total_notes += note
            nombre_etudiants += 1

            if note >= 60:
                etudiants_reussis.append(f"{nom} {note}")

        # Vérifier s'il y a des étudiants
        if nombre_etudiants == 0:
            print("Aucune donnée valide trouvée.")
            return

        moyenne = total_notes / nombre_etudiants

        # Écrire le fichier de sortie
        with open("resultats.txt", "w", encoding="utf-8") as resultat:
            resultat.write("Étudiants ayant une note ≥ 60 :\n")
            for etudiant in etudiants_reussis:
                resultat.write(etudiant + "\n")

            resultat.write("\n")
            resultat.write(f"Moyenne du groupe : {moyenne:.2f}\n")

        print("Traitement terminé avec succès ✅")
        print("Résultats écrits dans resultats.txt")

    except FileNotFoundError:
        print("Erreur : le fichier 'etudiants.txt' est introuvable ❌")


# Point d'entrée du script
if __name__ == "__main__":
    main()

