from Figure import Figure

class Carre(Figure):
    def __init__(self, cote: float):
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"Carré de côté {self.cote}"
