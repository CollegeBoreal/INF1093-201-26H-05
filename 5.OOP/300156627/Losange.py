from figure import Figure

class Losange(Figure):
    def __init__(self, d1, d2):
        super().__init__("Losange")
        self.d1 = d1
        self.d2 = d2

    def aire(self):
        return (self.d1 * self.d2) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, diagonales=({self.d1}, {self.d2}), aire={self.aire()}"