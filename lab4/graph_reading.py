def create_graph_from_file(file_to_read):

    with open(file_to_read, "r") as graph_file:
        main_data = list(graph_file.readline().split(" "))
        edge_counter = int(main_data[0])
        entry_point = int(main_data[1])
        result_graph = {i: [] for i in range(edge_counter)}

        for line in graph_file:
            connection = list(line.split(" "))
            result_graph[int(connection[0])].append((int(connection[1]), int(connection[2])))

        return result_graph, entry_point

