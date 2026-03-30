# INF1093 - Programmation 2
# Traitement I/O (Input/Output)
# Souleymane Barry - 300141685
# Fichier: IO.py

import sys

def lire_notes(nom_fichier):
    \"\"\"Lit le fichier etudiants.txt et retourne les listes noms et notes\"\"\"
    noms = []
    notes = []
    
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    parties = ligne.split(",")
                    if len(parties) == 2:
                        nom = parties[0]
                        try:
                            note = float(parties[1])
                            noms.append(nom)
                            notes.append(note)
                        except ValueError:
                            print(f"Erreur: Note invalide pour {nom}", file=sys.stderr)
                    else:
                        print(f"Erreur: Format invalide: {ligne}", file=sys.stderr)
        return noms, notes
    except FileNotFoundError:
        print(f"Erreur: Fichier {nom_fichier} introuvable", file=sys.stderr)
        sys.exit(1)

def calculer_moyenne(notes):
    \"\"\"Calcule la moyenne des notes\"\"\"
    if not notes:
        return 0
    return sum(notes) / len(notes)

def ecrire_resultats(nom_fichier, noms, notes, moyenne):
    \"\"\"Ecrit les resultats dans resultats.txt\"\"\"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("RAPPORT DES NOTES\n")
        f.write(f"Souleymane Barry - 300141685\n")
        f.write("=" * 40 + "\n\n")
        
        f.write("Etudiant.e.s ayant la moyenne (>=60):\n")
        f.write("-" * 40 + "\n")
        nb_reussite = 0
        for i in range(len(noms)):
            if notes[i] >= 60:
                f.write(f"{noms[i]} : {notes[i]}\n")
                nb_reussite += 1
        
        f.write("\n" + "-" * 40 + "\n")
        f.write(f"Moyenne du groupe : {moyenne:.2f}\n")
        f.write(f"Nombre d'etudiant.e.s : {len(noms)}\n")
        f.write(f"Reussite (>=60) : {nb_reussite}\n")
        f.write(f"Taux de reussite : {(nb_reussite/len(noms))*100:.1f}%\n")
        f.write("=" * 40 + "\n")

def main():
    print("=== Traitement des notes ===\n")
    
    # Lecture du fichier
    noms, notes = lire_notes("etudiants.txt")
    
    if not noms:
        print("Aucune donnee valide a traiter.", file=sys.stderr)
        sys.exit(1)
    
    # Affichage dans la console
    print("Liste des etudiant.e.s :")
    for i in range(len(noms)):
        print(f"  {noms[i]} : {notes[i]}")
    
    # Calcul de la moyenne
    moyenne = calculer_moyenne(notes)
    print(f"\nMoyenne du groupe : {moyenne:.2f}")
    
    # Ecriture des resultats
    ecrire_resultats("resultats.txt", noms, notes, moyenne)
    print("\nResultats enregistres dans resultats.txt")

if __name__ == "__main__":
    main()
