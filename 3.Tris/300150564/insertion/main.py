from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE / "entree_insertion.txt"


# Trés bien Ouassin, t'es le meilleur
def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle


def main():
    tab = list(map(int, INPUT.read_text(encoding="utf-8").split()))
    tri_insertion(tab)
    print("Résultat :", tab)


if __name__ == "__main__":
    main()