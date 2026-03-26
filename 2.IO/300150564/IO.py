from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "etudiants.txt"
OUTPUT_FILE = BASE_DIR / "resultats.txt"
PASSING = 60


def parse_line(line: str, line_no: int):
    line = line.strip()
    if not line:
        return None

    parts = line.split()
    if len(parts) < 2:
        raise ValueError(f"Ligne {line_no}: format invalide (ex: Alice 85) -> {line!r}")

    note_str = parts[-1]
    nom = " ".join(parts[:-1])

    try:
        note = float(note_str)
    except ValueError:
        raise ValueError(f"Ligne {line_no}: note invalide -> {note_str!r}")

    return nom, note


def main():
    etudiants = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            item = parse_line(line, line_no)
            if item is not None:
                etudiants.append(item)

    if not etudiants:
        raise ValueError("Fichier vide ou aucune ligne valide.")

    moyenne = sum(note for _, note in etudiants) / len(etudiants)
    admis = [(nom, note) for nom, note in etudiants if note >= PASSING]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("Étudiant(e)s ayant >= 60:\n")
        if admis:
            for nom, note in admis:
                out.write(f"- {nom} {note}\n")
        else:
            out.write("- Aucun\n")

        out.write(f"\nMoyenne du groupe: {moyenne:.2f}\n")
        out.write(f"Nombre d'étudiant(e)s: {len(etudiants)}\n")

    print("OK: resultats.txt généré.")


if __name__ == "__main__":
    main()