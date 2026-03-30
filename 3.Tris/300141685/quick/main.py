
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE / "entree_quick.txt"


def tri_rapide(tab):
    if len(tab) <= 1:
        return tab

    pivot = tab[len(tab) // 2]
    gauche = [x for x in tab if x < pivot]
    milieu = [x for x in tab if x == pivot]
    droite = [x for x in tab if x > pivot]

    return tri_rapide(gauche) + milieu + tri_rapide(droite)


def main():
    tab = list(map(int, INPUT.read_text(encoding="utf-8").split()))
    tab_trie = tri_rapide(tab)
    print("Résultat :", tab_trie)


if __name__ == "__main__":
    main()
