from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE / "entree_shell.txt"


def tri_shell(tab):
    n = len(tab)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = tab[i]
            j = i
            while j >= gap and tab[j - gap] > temp:
                tab[j] = tab[j - gap]
                j -= gap
            tab[j] = temp
        gap //= 2


def main():
    tab = list(map(int, INPUT.read_text(encoding="utf-8").split()))
    tri_shell(tab)
    print("Résultat :", tab)


if __name__ == "__main__":
    main()