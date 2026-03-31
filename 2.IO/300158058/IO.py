"""
Fichier : IO.py
Auteur : BELAID Rabah
ID : 300158058
Description : Lecture d'un fichier texte, calcul de la moyenne et écriture des résultats.
"""

def lire_etudiants(nom_fichier):
    donnees = []
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for numero, ligne in enumerate(fichier, start=1):
                ligne = ligne.strip()
                if not ligne:
                    continue

                parties = ligne.split()
                if len(parties) != 2:
                    print(f"Ligne ignorée {numero} : format invalide -> {ligne}")
                    continue

                nom, note_str = parties
                try:
                    note = float(note_str)
                    donnees.append((nom, note))
                except ValueError:
                    print(f"Ligne ignorée {numero} : note invalide -> {ligne}")

    except FileNotFoundError:
        print(f"Erreur : le fichier {nom_fichier} est introuvable.")

    return donnees


def calculer_moyenne(donnees):
    if not donnees:
        return 0
    total = sum(note for _, note in donnees)
    return total / len(donnees)


def ecrire_resultats(nom_fichier, donnees, moyenne):
    reussite = [element for element in donnees if element[1] >= 60]

    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write("=== Résultats des étudiants ===\n")
        fichier.write("\nÉtudiants ayant réussi (note >= 60) :\n")

        for nom, note in reussite:
            fichier.write(f"- {nom} : {note}\n")

        fichier.write("\n")
        fichier.write(f"Moyenne du groupe : {moyenne:.2f}\n")
        fichier.write(f"Nombre total d'étudiants lus : {len(donnees)}\n")
        fichier.write(f"Nombre d'étudiants ayant réussi : {len(reussite)}\n")


def main():
    entree = "etudiants.txt"
    sortie = "resultats.txt"

    donnees = lire_etudiants(entree)
    moyenne = calculer_moyenne(donnees)
    ecrire_resultats(sortie, donnees, moyenne)

    print("Traitement terminé.")
    print(f"Moyenne calculée : {moyenne:.2f}")


if __name__ == "__main__":
    main()
