from src.Node import Node


class Graph:

    def __init__(self):
        self.adjacencyList = []
        self.numPointsOfInterest = 0

    def add_node(self, node) -> bool:
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

        list_node1 = self.adjacencyList[start_index]
        edge_tuple1 = (end_index, distance)
        list_node1.append(edge_tuple1)

        list_node2 = self.adjacencyList[end_index]
        edge_tuple2 = (start_index, distance)
        list_node2.append(edge_tuple2)

        return True

    def get_num_points_of_interest(self):
        return self.numPointsOfInterest
