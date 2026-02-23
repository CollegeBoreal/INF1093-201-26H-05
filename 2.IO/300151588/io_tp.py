# -----------------
# Author: Ryma
# -----------------

import sys

def traiter_notes(fichier_entree, fichier_sortie):
    total = 0
    compteur = 0
    admis = []

    try:
        with open(fichier_entree, "r") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue

                try:
                    nom, note = ligne.split()
                    note = float(note)
                except ValueError:
                    print(f"Format invalide : {ligne}", file=sys.stderr)
                    continue

                total += note
                compteur += 1

                if note >= 60:
                    admis.append((nom, note))

        if compteur == 0:
            raise ValueError("Fichier vide")

        moyenne = total / compteur

        with open(fichier_sortie, "w") as f:
            f.write("Étudiant.e.s admis (≥ 60)\n")
            for nom, note in admis:
                f.write(f"{nom} {note}\n")

            f.write(f"\nMoyenne du groupe : {moyenne:.2f}\n")

    except FileNotFoundError:
        print("Fichier d'entrée introuvable", file=sys.stderr)
    except Exception as e:
        print(f"Erreur : {e}", file=sys.stderr)

if __name__ == "__main__":
    traiter_notes("etudiants.txt", "resultats.txt")
