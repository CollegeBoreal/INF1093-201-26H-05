from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote * self.cote

    def description(self):
        return f"{super().description()}, côté = {self.cote}, aire = {self.aire()}"