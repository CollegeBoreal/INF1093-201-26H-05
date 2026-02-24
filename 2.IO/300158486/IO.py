"""IO.py
Lit un fichier d'entrée (etudiants.txt), calcule la moyenne,
et génère un fichier de sortie (resultats.txt).

Format attendu (une ligne par étudiant) :
    nom note
Exemple :
    fouad 45
"""

from __future__ import annotations

def lire_notes(path: str) -> list[tuple[str, int]]:
    etudiants: list[tuple[str, int]] = []
    with open(path, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            # On accepte aussi les espaces multiples
            morceaux = ligne.split()
            if len(morceaux) != 2:
                raise ValueError(f"Ligne invalide: {ligne!r} (attendu: 'nom note')")
            nom, note_txt = morceaux
            note = int(note_txt)
            etudiants.append((nom, note))
    if not etudiants:
        raise ValueError("Le fichier est vide.")
    return etudiants


def calculer_moyenne(etudiants: list[tuple[str, int]]) -> float:
    total = sum(note for _, note in etudiants)
    return total / len(etudiants)


def ecrire_resultats(path: str, etudiants: list[tuple[str, int]], moyenne: float, seuil: int = 40) -> None:
    reussis = [(nom, note) for nom, note in etudiants if note >= seuil]

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Étudiant.e.s avec note ≥ {seuil} :\n")
        for nom, note in reussis:
            f.write(f"{nom} {note}\n")
        f.write("\n")
        f.write(f"Moyenne du groupe : {moyenne:.3f}\n")


def main() -> None:
    entree = "etudiants.txt"
    sortie = "resultats.txt"

    etudiants = lire_notes(entree)
    moyenne = calculer_moyenne(etudiants)
    ecrire_resultats(sortie, etudiants, moyenne, seuil=40)

    print(f"OK ✅ Fichier généré: {sortie}")
    print(f"Moyenne: {moyenne:.3f}")


if __name__ == "__main__":
    main()
