class Losange:
    def __init__(self, diagonale1, diagonale2):
        self.diagonale1 = diagonale1
        self.diagonale2 = diagonale2

    def aire(self):
        return (self.diagonale1 * self.diagonale2) / 2

    def afficher_info(self):
        return f"Losange de diagonales {self.diagonale1} et {self.diagonale2}"
