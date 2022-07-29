from src.Node import Node


class Graph:

    def __init__(self):
        self.adjacencyList = []
        self.numPointsOfInterest = 0
        self.nodes = []

    def add_node(self, node) -> bool:
        self.nodes.append(node)
        index = node.get_index()
        # check if node is already in list and append if not

        if len(self.adjacencyList) >= index:
            return False

        list_node = []
        self.adjacencyList.append(list_node)
        self.numPointsOfInterest = self.numPointsOfInterest + node.get_num_points_of_interest()

        return True

    def add_edge(self, start_index, end_index, distance) -> bool:

        if not len(self.adjacencyList) > start_index or not len(self.adjacencyList) > end_index:
            return False

        list_node = self.adjacencyList[start_index]
        edge_tuple = (end_index, distance)
        list_node.append(edge_tuple)

        return True

    def get_num_points_of_interest(self):
        return self.numPointsOfInterest

    def get_node(self, node_index) -> Node:
        return self.nodes[node_index]
