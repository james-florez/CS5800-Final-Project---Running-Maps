from src.Node import Node


class Graph:
    def __init__(self):
        self.adjacencyList = []
        self.numPointsOfInterest = 0

    def add_node(self, node):
        index = node.get_index()
        # check if node is already in list and append if not

    def add_edge(self, start_index, end_index, distance):
        pass

    def get_num_points_of_interest(self):
        return self.numPointsOfInterest
