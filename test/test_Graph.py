from unittest import TestCase
from src.Graph import Graph
from src.Node import Node


class TestGraph(TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.node1 = Node(0, 10, 20, ["Boston Public Garden", "Statue of George Washington"])
        self.node2 = Node(1, 13, 20, ["Boston Commons"])

    def test_add_node(self):
        self.assertEqual(True, self.graph.add_node(self.node1))  # Valid test
        self.assertEqual(False, self.graph.add_node(self.node1))  # Node already exists in graph

    def test_add_edge(self):
        self.assertEqual(True, self.graph.add_node(self.node1))
        self.assertEqual(True, self.graph.add_node(self.node2))
        self.assertEqual(True, self.graph.add_edge(0, 1, 3))  # Valid test
        self.assertEqual(False, self.graph.add_edge(0, 2, 5))  # Invalid node index

    def test_get_num_points_of_interest(self):
        self.assertEqual(0, self.graph.get_num_points_of_interest())  # No points of interest
        self.assertEqual(True, self.graph.add_node(self.node1))
        self.assertEqual(True, self.graph.add_node(self.node2))
        self.assertEqual(3, self.graph.get_num_points_of_interest())  # Valid test

    def test_get_points_of_interest(self):
        self.assertEqual(set(), self.graph.get_points_of_interest())  # No points of interest
        self.assertEqual(True, self.graph.add_node(self.node1))
        self.assertEqual(True, self.graph.add_node(self.node2))
        self.assertEqual({'Boston Public Garden', 'Boston Commons', 'Statue of George Washington'},
                         self.graph.get_points_of_interest())  # Valid test

    def test_get_node(self):
        self.assertEqual(True, self.graph.add_node(self.node1))
        self.assertEqual(self.node1, self.graph.get_node(0))  # Valid test
        self.assertEqual(None, self.graph.get_node(10))  # Invalid node index

    def test_get_distance(self):
        self.assertEqual(True, self.graph.add_node(self.node1))
        self.assertEqual(True, self.graph.add_node(self.node2))
        self.assertEqual(True, self.graph.add_edge(0, 1, 3))
        self.assertEqual(3, self.graph.get_distance(0, 1))  # Valid test
        self.assertEqual(0, self.graph.get_distance(0, 2))  # Invalid node index
