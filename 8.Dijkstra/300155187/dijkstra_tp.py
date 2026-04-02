def dijkstra(aGraph, start):

    # 🔄 RESET DES SOMMETS (IMPORTANT)
    for v in aGraph:
        v.distance = float('inf')
        v.visited = False
        v.previous = None

    # initialisation
    start.set_distance(0)
    unvisited = [v for v in aGraph]

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
