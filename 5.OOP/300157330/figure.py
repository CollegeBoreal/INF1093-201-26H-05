class Figure:
    def __init__(self, nom):
        self.nom = nom

    def description(self):
        return f"Nom de la figure : {self.nom}"

    def aire(self):
        raise NotImplementedError("La méthode aire() doit être définie dans la sous-classe.")