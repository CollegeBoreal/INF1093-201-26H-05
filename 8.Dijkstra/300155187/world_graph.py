from graph import Graph

class WorldGraph(Graph):
    def __init__(self):
        super().__init__()
        self.build_graph()

    def build_graph(self):

        cities = [
            'Toronto','New York','London','Paris','Berlin','Rome',
            'Casablanca','Dakar','Lagos','Nairobi','Johannesburg'
        ]

        for c in cities:
            self.add_vertex(c)

        edges = [
            ('Toronto','New York',800),
            ('New York','London',5600),
            ('New York','Paris',5800),
            ('Toronto','London',5900),
            ('London','Paris',340),
            ('Paris','Berlin',1050),
            ('Berlin','Rome',1180),
            ('Paris','Casablanca',2000),
            ('London','Casablanca',3000),
            ('Berlin','Casablanca',2800),
            ('Rome','Dakar',3500),
            ('Casablanca','Dakar',2700),
            ('Dakar','Lagos',3000),
            ('Lagos','Nairobi',4400),
            ('Nairobi','Johannesburg',2900),
        ]

        for u, v, w in edges:
            self.add_edge(u, v, w)