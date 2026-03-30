"""
graph.py
Auteur : BELAID Rabah
ID : 300158058
Description : Définition des classes Vertex et Graph pour représenter un graphe pondéré.
"""

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = float("inf")
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        voisins = [x.id for x in self.adjacent]
        return f"{self.id} adjacent à {voisins}"


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        nouveau = Vertex(node)
        self.vert_dict[node] = nouveau
        return nouveau

    def get_vertex(self, node):
        return self.vert_dict.get(node, None)

    def add_edge(self, source, destination, cost=0):
        if source not in self.vert_dict:
            self.add_vertex(source)
        if destination not in self.vert_dict:
            self.add_vertex(destination)

        self.vert_dict[source].add_neighbor(self.vert_dict[destination], cost)
        self.vert_dict[destination].add_neighbor(self.vert_dict[source], cost)

    def get_vertices(self):
        return self.vert_dict.keys()
