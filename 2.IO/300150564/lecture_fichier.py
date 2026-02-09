with open("fichier.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(f"Traitement: {ligne.strip()}")

