from pathlib import Path

ENTREE = Path("etudiants.txt")
SORTIE = Path("resultats.txt")


def lire_etudiants(chemin: Path):
    etudiants = []
    with chemin.open("r", encoding="utf-8") as f:
        for numero_ligne, ligne in enumerate(f, start=1):
            ligne = ligne.strip()
            if not ligne:
                continue

            morceaux = ligne.split()
            if len(morceaux) < 2:
                raise ValueError(
                    f"Format invalide a la ligne {numero_ligne}: '{ligne}'"
                )

            nom = " ".join(morceaux[:-1])
            try:
                note = float(morceaux[-1])
            except ValueError as exc:
                raise ValueError(
                    f"Note invalide a la ligne {numero_ligne}: '{morceaux[-1]}'"
                ) from exc

            etudiants.append((nom, note))
    return etudiants


def generer_resultats(etudiants, chemin_sortie: Path):
    if not etudiants:
        raise ValueError("Le fichier d'entree est vide.")

    moyenne = sum(note for _, note in etudiants) / len(etudiants)
    admis = [(nom, note) for nom, note in etudiants if note >= 60]

    with chemin_sortie.open("w", encoding="utf-8") as f:
        f.write("Resultats des etudiant.e.s\n")
        f.write("=" * 28 + "\n\n")
        f.write("Etudiant.e.s ayant une note >= 60 :\n")
        for nom, note in admis:
            f.write(f"- {nom} : {note:.1f}\n")

        f.write("\n")
        f.write(f"Moyenne du groupe : {moyenne:.2f}\n")
        f.write(f"Nombre total d'etudiant.e.s : {len(etudiants)}\n")
        f.write(f"Nombre d'etudiant.e.s admis : {len(admis)}\n")

    return moyenne, admis


def main():
    etudiants = lire_etudiants(ENTREE)
    moyenne, admis = generer_resultats(etudiants, SORTIE)
    print("Traitement termine avec succes.")
    print(f"Moyenne du groupe : {moyenne:.2f}")
    print(f"Etudiant.e.s admis : {len(admis)}")
    print(f"Fichier genere : {SORTIE}")


if __name__ == "__main__":
    main()
