# -----------------
# Author: Toufik Mekbel
# -----------------

import sys

def analyser_fichier(entree, sortie):
    somme_notes = 0
    nb_etudiants = 0
    liste_admis = []

    try:
        fichier = open(entree, "r")

        for ligne in fichier:
            ligne = ligne.strip()

            if ligne == "":
                continue

            infos = ligne.split()

            if len(infos) != 2:
                print("Erreur format :", ligne, file=sys.stderr)
                continue

            nom = infos[0]
            try:
                note = float(infos[1])
            except:
                print("Note invalide :", ligne, file=sys.stderr)
                continue

            somme_notes += note
            nb_etudiants += 1

            if note >= 60:
                liste_admis.append((nom, note))

        fichier.close()

        if nb_etudiants == 0:
            print("Aucune donnée trouvée", file=sys.stderr)
            return

        moyenne = somme_notes / nb_etudiants

        # écrire le résultat
        fichier_sortie = open(sortie, "w")

        fichier_sortie.write("Liste des étudiants admis :\n")

        for nom, note in liste_admis:
            fichier_sortie.write(f"{nom} -> {note}\n")

        fichier_sortie.write("\n")
        fichier_sortie.write(f"Moyenne générale : {moyenne:.2f}\n")

        fichier_sortie.close()

        print("Traitement terminé avec succès ✔")

    except FileNotFoundError:
        print("Fichier non trouvé ❌", file=sys.stderr)


# exécution
if __name__ == "__main__":
    analyser_fichier("etudiants.txt", "resultats.txt")