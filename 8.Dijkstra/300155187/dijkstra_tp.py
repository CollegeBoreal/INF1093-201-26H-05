def dijkstra(aGraph, start):

    for v in aGraph:
        v.distance = float('inf')
        v.visited = False
        v.previous = None

    start.set_distance(0)
    unvisited = list(aGraph)

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


def shortest(v):
    path = [v.get_id()]
    while v.previous:
        v = v.previous
        path.append(v.get_id())
    return path[::-1]


def find_all_paths(aGraph, start_id, end_id, path=None):
    if path is None:
        path = []

    path = path + [start_id]

    if start_id == end_id:
        return [path]

    paths = []
    start_vertex = aGraph.get_vertex(start_id)

    for neighbor in start_vertex.get_connections():
        if neighbor.get_id() not in path:
            newpaths = find_all_paths(
                aGraph,
                neighbor.get_id(),
                end_id,
                path
            )
            for p in newpaths:
                paths.append(p)

    return paths


def path_distance(aGraph, path):
    dist = 0
    for i in range(len(path) - 1):
        u = aGraph.get_vertex(path[i])
        v = aGraph.get_vertex(path[i + 1])
        dist += u.get_weight(v)
    return dist