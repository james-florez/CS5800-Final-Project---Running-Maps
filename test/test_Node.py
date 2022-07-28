from unittest import TestCase
from src.Node import Node


class TestNode(TestCase):
    def setUp(self):
        self.node = Node(0, 10, 20, 2, ["Boston Public Garden", "Statue of George Washington"])

    def test_get_index(self):
        self.assertEqual(self.node.get_index(), 0)

    def test_get_x(self):
        self.assertEqual(self.node.get_x(), 10)

    def test_get_y(self):
        self.assertEqual(self.node.get_y(), 20)

    def test_get_num_points_of_interest(self):
        self.assertEqual(self.node.get_num_points_of_interest(), 2)

    def test_get_descriptions(self):
        self.assertEqual(self.node.get_descriptions(), ["Boston Public Garden", "Statue of George Washington"])
