INPUT_FILE = "etudiants.txt"
OUTPUT_FILE = "resultats.txt"
PASSING = 60


def main():
    students = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Ligne {line_no}: format invalide -> {line!r}")
            name = parts[0]
            try:
                grade = float(parts[1])
            except ValueError:
                raise ValueError(f"Ligne {line_no}: note invalide -> {parts[1]!r}")
            students.append((name, grade))

    if not students:
        raise ValueError("Fichier vide ou aucune ligne valide.")

    avg = sum(g for _, g in students) / len(students)
    passing_students = [(n, g) for n, g in students if g >= PASSING]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("Étudiant(e)s ayant >= 60:\n")
        if passing_students:
            for n, g in passing_students:
                out.write(f"- {n} {g}\n")
        else:
            out.write("- Aucun\n")
        out.write(f"\nMoyenne du groupe: {avg:.2f}\n")

    print("OK: resultats.txt généré.")


if __name__ == "__main__":
    main()

