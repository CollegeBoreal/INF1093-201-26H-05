
class Carre:
    def __init__(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"Carré de côté {self.cote}"
