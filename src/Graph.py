from collections import defaultdict
from src.Node import Node


class Graph:
    """A class used to represent a Graph (city map/route).

    Attributes:
        adjacency_list ({{int}}): adjacency list representation of the Graph with distance values
        points_of_interest (set): names of points of interest in the Graph
        nodes (list): Nodes in the Graph
    """

    def __init__(self):
        """Initializes a Graph object."""

        self.adjacency_list = {}
        self.points_of_interest = set()
        self.nodes = {}

    def add_node(self, node: Node) -> bool:
        """Adds a Node to the Graph representing a street intersection.

        Args:
            node (Node): the Node to be added
        Returns:
            bool: True if the Node was added and False if a Node with the same index already exists in the Graph
        """

        # Validate parameters
        if self.nodes.__contains__(node.get_index()):
            return False  # Node already exists

        # Add node
        self.nodes[node.get_index()] = node
        self.adjacency_list[node.get_index()] = defaultdict(int)

        # Add points of interest
        for point_of_interest in node.get_points_of_interest():
            self.points_of_interest.add(point_of_interest)

        return True

    def add_edge(self, start_index: int, end_index: int, distance: int) -> bool:
        """Adds an edge to the Graph representing a street.

        Args:
            start_index (int): the index of the Node on the 1st side of the edge
            end_index (int): the index of the Node on the 2nd side of the edge
            distance (int): the length of the edge in feet
        Returns:
             bool: True if the edge was added and False if either Node index does not exist in the Graph
        """

        # Validate parameters
        if start_index not in self.adjacency_list or end_index not in self.adjacency_list:
            return False  # Node does not exist

        # Add (end_index, distance) to the start node adjacency list
        self.adjacency_list[start_index][end_index] = distance

        # Add (start_index, distance) to the end node adjacency list
        self.adjacency_list[end_index][start_index] = distance

        return True

    def get_num_points_of_interest(self) -> int:
        """Gets the number of the points of interest in the Graph.

        Returns:
            int: number of points of interest
        """
        return len(self.points_of_interest)

    def get_points_of_interest(self) -> set:
        """Gets the names of the points of interest in the Graph.

        Returns:
            set: names of points of interest
        """
        return self.points_of_interest

    def get_node(self, node_index: int) -> Node or None:
        """Gets the Node with the given node index.

        Returns:
            Node or None: The Node if the node index is valid or None if it is invalid
        """
        if not self.nodes.__contains__(node_index):
            return None
        else:
            return self.nodes[node_index]

    def get_distance(self, start_node_index: int, end_node_index: int) -> int:
        """Gets the distance (feet) of the edge between the Nodes given by the indices.

        Returns:
            int: the distance in feet between the Nodes or 0 if the Nodes are not connected
        """
        return self.adjacency_list[start_node_index][end_node_index]
