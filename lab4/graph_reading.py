def create_graph_from_file(file_to_read):

    with open(file_to_read, "r") as graph_file:
        main_data = list(graph_file.readline().split(" "))
        entry_point = int(main_data[1])
        result_graph = {}

        for line in graph_file:
            connection = list(line.split(" "))
            connection[0] = int(connection[0])
            connection[1] = int(connection[1])
            connection[2] = int(connection[2])
            if connection[0] in result_graph.keys():
                result_graph[connection[0]].append((connection[1], connection[2]))
            else:
                result_graph[connection[0]] = [(connection[1], connection[2])]
            if connection[1] not in result_graph.keys():
                result_graph[connection[1]] = []

        return result_graph, entry_point
