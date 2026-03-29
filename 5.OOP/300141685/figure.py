# INF1093 - Programmation 2 - POO
# Souleymane Barry - 300141685

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure: {self.nom}"

    def aire(self):
        raise NotImplementedError("A implementer par les sous-classes")

    def perimetre(self):
        raise NotImplementedError("A implementer par les sous-classes")
