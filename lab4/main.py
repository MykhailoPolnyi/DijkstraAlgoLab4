from graph_reading import create_graph_from_file
from dijkstra import dijkstra

if __name__ == "__main__":
    graph_example, entry_point = create_graph_from_file("dijkstra_example.txt")
    distances = dijkstra(graph_example, 500)
    for edge, distance in distances.items():
        print(edge, ": ", distance)
