def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0

try:
    etudiants = []
    notes = []
    
    print("Lecture du fichier etudiants.txt...")
    
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            print(f"Ligne lue: '{ligne}'")
            if ligne:
                # Utiliser la virgule comme séparateur
                parts = ligne.split(',')
                if len(parts) == 2:
                    nom, note = parts[0].strip(), int(parts[1].strip())
                    etudiants.append((nom, note))
                    notes.append(note)
                    print(f"  -> Ajoute: {nom} avec {note}")
                else:
                    print(f"  -> Ignoree (format incorrect)")
    
    print(f"\nTotal etudiants trouves: {len(etudiants)}")
    
    if len(notes) > 0:
        moyenne = calculer_moyenne(notes)
    else:
        moyenne = 0
    
    with open("resultats.txt", "w") as f:
        f.write("=== Etudiants ayant reussi (note >= 60) ===\n")
        for nom, note in etudiants:
            if note >= 60:
                f.write(f"{nom}: {note}\n")
        f.write("\n=== Moyenne du groupe ===\n")
        f.write(f"Moyenne: {moyenne:.2f}\n")
    
    print(f"\n✅ resultats.txt genere avec succes")
    print(f"Moyenne: {moyenne:.2f}")
    
except FileNotFoundError:
    print("❌ Erreur: Fichier etudiants.txt introuvable")
except ValueError as e:
    print(f"❌ Erreur: Format de note invalide - {e}")