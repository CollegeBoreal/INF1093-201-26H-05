class Pyramide:
    def __init__(self, aire_base, hauteur):
        self.aire_base = aire_base
        self.hauteur = hauteur

    def volume(self):
        return (self.aire_base * self.hauteur) / 3

    def afficher_info(self):
        return f"Pyramide d'aire de base {self.aire_base} et hauteur {self.hauteur}"
