from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")  # Nom de la figure
        self.cote = cote           # Longueur du côté

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"