import sys
def main():
    try:
        with open("etudiants.txt", "r") as f:
            lignes = f.readlines()
        notes = [int(l.split()[1]) for l in lignes if len(l.split()) == 2]
        recus = [l.strip() for l in lignes if len(l.split()) == 2 and int(l.split()[1]) >= 60]
        with open("resultats.txt", "w") as f_out:
            f_out.write("Admis :\n" + "\n".join(recus))
            f_out.write(f"\nMoyenne : {sum(notes)/len(notes):.2f}")
    except Exception as e:
        print(f"Erreur : {e}", file=sys.stderr)
if __name__ == "__main__":
    main()
