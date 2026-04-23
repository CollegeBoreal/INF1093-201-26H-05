from graph import Graph


def build_graph():
    g = Graph()
    for node in ["a", "b", "c", "d", "e", "f"]:
        g.add_vertex(node)

    g.add_edge("a", "b", 7)
    g.add_edge("a", "c", 9)
    g.add_edge("a", "f", 14)
    g.add_edge("b", "c", 10)
    g.add_edge("b", "d", 15)
    g.add_edge("c", "d", 11)
    g.add_edge("c", "f", 2)
    g.add_edge("d", "e", 6)
    g.add_edge("e", "f", 9)
    return g


def reset_graph(a_graph):
    for vertex in a_graph:
        vertex.set_distance(float("inf"))
        vertex.visited = False
        vertex.previous = None


def dijkstra(a_graph, start):
    reset_graph(a_graph)
    start.set_distance(0)
    unvisited = [v for v in a_graph]

    while unvisited:
        current = min(unvisited, key=lambda v: v.get_distance())
        current.set_visited()
        unvisited.remove(current)

        for neighbor in current.adjacent:
            if neighbor.visited:
                continue

            new_dist = current.get_distance() + current.get_weight(neighbor)

            if new_dist < neighbor.get_distance():
                neighbor.set_distance(new_dist)
                neighbor.set_previous(current)
                print(
                    f"updated : current = {current.get_id()} "
                    f"next = {neighbor.get_id()} "
                    f"new_dist = {neighbor.get_distance()}"
                )
            else:
                print(
                    f"not updated : current = {current.get_id()} "
                    f"next = {neighbor.get_id()} "
                    f"new_dist = {neighbor.get_distance()}"
                )


def shortest(vertex):
    path = [vertex.get_id()]
    while vertex.previous:
        vertex = vertex.previous
        path.append(vertex.get_id())
    return path[::-1]


def run_demo():
    graph = build_graph()

    print("Graph data:")
    for vertex in graph:
        for neighbor in vertex.get_connections():
            print(f"( {vertex.get_id()} , {neighbor.get_id()}, {vertex.get_weight(neighbor):3d} )")

    start = graph.get_vertex("a")
    target = graph.get_vertex("e")
    dijkstra(graph, start)

    path = shortest(target)
    print("Le plus court chemin:", path)
    print("Distance totale:", target.get_distance())
    return graph, path, target.get_distance()


if __name__ == "__main__":
    run_demo()
