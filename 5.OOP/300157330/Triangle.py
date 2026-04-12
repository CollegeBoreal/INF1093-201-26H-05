from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def description(self):
        return f"{super().description()}, base = {self.base}, hauteur = {self.hauteur}, aire = {self.aire()}"