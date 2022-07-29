from src.Node import Node


class Graph:

    def __init__(self):
        # TODO possibly make the adjacencyList use dictionaries
        self.adjacency_list = []
        self.points_of_interest = set()
        self.nodes = []

    def add_node(self, node) -> bool:
        self.nodes.append(node)
        index = node.get_index()
        # check if node is already in list and append if not

        if len(self.adjacency_list) >= index:
            return False

        list_node = []
        self.adjacency_list.append(list_node)

        # Add points of interest to the hash set
        for point_of_interest in node.get_points_of_interest():
            self.points_of_interest.add(point_of_interest)

        return True

    def add_edge(self, start_index, end_index, distance) -> bool:

        # TODO might need to modify this condition
        if not len(self.adjacency_list) > start_index or not len(self.adjacency_list) > end_index:
            return False

        list_node1 = self.adjacency_list[start_index]
        edge_tuple1 = (end_index, distance)
        list_node1.append(edge_tuple1)

        list_node2 = self.adjacency_list[end_index]
        edge_tuple2 = (start_index, distance)
        list_node2.append(edge_tuple2)

        return True

    def get_num_points_of_interest(self):
        return len(self.points_of_interest)

    def get_points_of_interest(self):
        return self.points_of_interest

    def get_node(self, node_index) -> Node:
        return self.nodes[node_index]
