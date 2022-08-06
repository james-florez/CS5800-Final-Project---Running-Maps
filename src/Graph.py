from src.Node import Node


class Graph:

    def __init__(self):
        # TODO possibly make the adjacencyList use dictionaries
        self.adjacency_list = []
        self.points_of_interest = set()
        self.nodes = []

    def add_node(self, node) -> bool:
        # Validate parameters
        if node.get_index() < len(self.adjacency_list):
            return False  # Node already exists

        # Add node
        self.nodes.append(node)
        self.adjacency_list.append([])

        # Add points of interest
        for point_of_interest in node.get_points_of_interest():
            self.points_of_interest.add(point_of_interest)

        return True

    def add_edge(self, start_index, end_index, distance) -> bool:
        # Validate parameters
        if start_index >= len(self.adjacency_list) or end_index >= len(self.adjacency_list):
            return False  # Node does not exist

        # Add (end_index, distance) to the start node adjacency list
        list_node1 = self.adjacency_list[start_index]
        edge_tuple1 = (end_index, distance)
        list_node1.append(edge_tuple1)

        # Add (start_index, distance) to the end node adjacency list
        list_node2 = self.adjacency_list[end_index]
        edge_tuple2 = (start_index, distance)
        list_node2.append(edge_tuple2)

        return True

    def get_num_points_of_interest(self):
        return len(self.points_of_interest)

    def get_points_of_interest(self):
        return self.points_of_interest

    def get_node(self, node_index):
        if node_index >= len(self.nodes):
            return None
        else:
            return self.nodes[node_index]

    def get_distance(self, start_node_index, end_node_index):
        edges = self.adjacency_list[start_node_index]
        for edge in self.adjacency_list[start_node_index]:
            if edge[0] == end_node_index:
                return edge[1]
        return 0
