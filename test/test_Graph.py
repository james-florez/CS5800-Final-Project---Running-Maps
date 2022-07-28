from unittest import TestCase
from src.Graph import Graph
from src.Node import Node


class TestGraph(TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.node1 = Node(0, 10, 20, 2, ["Boston Public Garden", "Statue of George Washington"])
        self.node2 = Node(1, 13, 20, 1, ["Boston Commons"])

    def test_add_node(self):
        self.assertEqual(True, self.graph.add_node(self.node1))

    def test_add_edge(self):
        self.assertEqual(True, self.graph.add_edge(0, 1, 3))
