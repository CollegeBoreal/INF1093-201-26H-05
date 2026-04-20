class Cube:
    def __init__(self, cote):
        self.cote = cote

    def aire(self):
        return 6 * self.cote ** 2

    def volume(self):
        return self.cote ** 3

    def afficher_info(self):
        return f"Cube de côté {self.cote}"
