from Figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return f"{self.nom} - base : {self.base}, hauteur : {self.hauteur}"
