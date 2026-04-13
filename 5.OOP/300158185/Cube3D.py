from Figure import Figure

class Cube3D(Figure):
    def __init__(self, cote: float):
        self.cote = cote

    def aire(self):
        return 6 * (self.cote ** 2)

    def volume(self):
        return self.cote ** 3

    def afficher_info(self):
        return f"Cube 3D de côté {self.cote}"
