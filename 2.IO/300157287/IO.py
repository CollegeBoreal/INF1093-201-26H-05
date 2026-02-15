# IO.py

def etudiantliste(entree):
    etudiants = []
    with open(entree, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                nom, note = ligne.split()
                note = float(note)
                etudiants.append((nom, note))
            except ValueError:
       
                raise ValueError(f" : '{ligne}'")
    return etudiants


def moy(etudiants):
    if not etudiants:
        return 0.0
    total = sum(note for _, note in etudiants)
    return total / len(etudiants)


def resultats(fichiersortie, etudiants, moyenne):
    with open(fichiersortie, "w", encoding="utf-8") as f:
        f.write("Etudiants avec note >= 60\n")
        for nom, note in etudiants:
            if note >= 60:
                f.write(f"{nom} {note}\n")
        f.write("\n")
        f.write(f"Moyenne du groupe: {moyenne:.2f}\n")


def main():
    fichierentree = "etudiants.txt"
    fichiersortie = "resultats.txt"

    try:
        etudiants = etudiantliste(fichierentree)
        moyenne = moy(etudiants)
        resultats(fichiersortie, etudiants, moyenne)
        print("Traitement termine. Resultats  dans resultats.txt")
    except FileNotFoundError:
        print(f"Erreur: le fichier {fichierentree} est introuvable.")
    except ValueError as e:
        print(f"Erreur de format de donnees: {e}")


if __name__ == "__main__":
    main()