def dijkstra(graph, entry_point):
    def relax_edge(edge):
        for connection in graph[edge]:
            if distance_to[connection[0]] == "inf" or \
                    distance_to[connection[0]] > distance_to[edge] + connection[1]:
                distance_to[connection[0]] = distance_to[edge] + connection[1]

    def _dijkstra(starting_edge):
        relax_edge(starting_edge)
        is_visited_node[starting_edge] = True
        for edge_connection in graph[starting_edge]:
            if not is_visited_node[edge_connection[0]]:
                _dijkstra(edge_connection[0])

    if entry_point not in graph.keys():
        raise ValueError("Edge with name {point} does not exist".format(point=entry_point))
    if len(graph) == 0:
        return {}
    distance_to = {i: "inf" for i in graph.keys()}
    is_visited_node = {i: False for i in graph.keys()}
    distance_to[entry_point] = 0

    _dijkstra(entry_point)

    return distance_to
