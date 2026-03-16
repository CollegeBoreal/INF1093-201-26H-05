"""
IO.py - Traitement des entrées/sorties sur fichiers
Cours : INF1093 - Travail pratique I/O
Étudiant : 300155504
"""

import sys
import os

# Chemin absolu pour exécuter depuis n'importe où
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def lire_etudiants(fichier):
    """Lit le fichier etudiants.txt et retourne une liste de tuples (nom, note)."""
    etudiants = []
    chemin = os.path.join(BASE_DIR, fichier)
    try:
        with open(chemin, "r") as f:
            for i, ligne in enumerate(f, 1):
                ligne = ligne.strip()
                if not ligne:
                    continue
                parties = ligne.split()
                if len(parties) != 2:
                    print(f"ERREUR: Ligne {i} mal formée : '{ligne}'", file=sys.stderr)
                    continue
                nom = parties[0]
                try:
                    note = float(parties[1])
                except ValueError:
                    print(f"ERREUR: Note invalide à la ligne {i} : '{parties[1]}'", file=sys.stderr)
                    continue
                etudiants.append((nom, note))
    except FileNotFoundError:
        print(f"ERREUR: Le fichier '{fichier}' est introuvable.", file=sys.stderr)
        sys.exit(1)
    return etudiants


def calculer_moyenne(etudiants):
    """Calcule la moyenne des notes."""
    if not etudiants:
        return 0.0
    return sum(note for _, note in etudiants) / len(etudiants)


def generer_resultats(etudiants, fichier_sortie):
    """Génère le fichier resultats.txt avec les étudiants >= 60 et la moyenne."""
    admis = [(nom, note) for nom, note in etudiants if note >= 60]
    moyenne = calculer_moyenne(etudiants)
    chemin = os.path.join(BASE_DIR, fichier_sortie)

    with open(chemin, "w") as f:
        f.write("===== RÉSULTATS =====\n\n")
        f.write("Étudiants ayant réussi (note >= 60) :\n")
        if admis:
            for nom, note in admis:
                f.write(f"  {nom} : {note:.1f}\n")
        else:
            f.write("  Aucun étudiant n'a réussi.\n")
        f.write(f"\nMoyenne du groupe : {moyenne:.2f}\n")

    print(f"Résultats écrits dans '{fichier_sortie}'.")
    print(f"Étudiants admis : {len(admis)}/{len(etudiants)}")
    print(f"Moyenne du groupe : {moyenne:.2f}")


def main():
    fichier_entree = "etudiants.txt"
    fichier_sortie = "resultats.txt"

    print(f"Lecture du fichier : {fichier_entree}")
    etudiants = lire_etudiants(fichier_entree)

    if not etudiants:
        print("ERREUR: Aucune donnée valide trouvée.", file=sys.stderr)
        sys.exit(1)

    generer_resultats(etudiants, fichier_sortie)


if __name__ == "__main__":
    main()
