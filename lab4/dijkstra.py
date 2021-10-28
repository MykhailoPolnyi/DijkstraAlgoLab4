def dijkstra(graph, entry_point):
    def relax_edge(edge):
        for connection in graph[edge]:
            if distance_to[connection[0]] == "inf" or \
                    distance_to[connection[0]] > distance_to[edge] + connection[1]:
                distance_to[connection[0]] = distance_to[edge] + connection[1]

    def _dijkstra(starting_edge):
        relax_edge(starting_edge)
        is_visited_node[starting_edge] = True
        for edge_con in graph[starting_edge]:
            if not is_visited_node[edge_con[0]]:
                _dijkstra(edge_con[0])

    if entry_point > len(graph):
        raise ValueError("Entry point should be in graph range")
    distance_to = {i: "inf" for i in range(len(graph))}
    is_visited_node = {i: False for i in range(len(graph))}
    distance_to[entry_point] = 0

    _dijkstra(entry_point)

    return distance_to
