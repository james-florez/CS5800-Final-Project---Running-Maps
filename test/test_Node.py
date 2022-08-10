from unittest import TestCase
from src.Node import Node


class TestNode(TestCase):
    def setUp(self):
        self.node = Node(0, 10, 20, ["Boston Public Garden", "Statue of George Washington"])

    def test_get_index(self):
        self.assertEqual(0, self.node.get_index())  # Valid test
        self.assertNotEqual(10, self.node.get_index())

    def test_get_latitude(self):
        self.assertEqual(10, self.node.get_latitude())  # Valid test
        self.assertNotEqual(1, self.node.get_latitude())

    def test_get_longitude(self):
        self.assertEqual(20, self.node.get_longitude())  # Valid test
        self.assertNotEqual(10, self.node.get_longitude())

    def test_get_num_points_of_interest(self):
        self.assertEqual(2, self.node.get_num_points_of_interest())  # Valid test
        self.assertNotEqual(3, self.node.get_num_points_of_interest())

    def test_get_points_of_interest(self):
        # Valid test
        self.assertEqual(["Boston Public Garden", "Statue of George Washington"], self.node.get_points_of_interest())
        self.assertNotEqual([], self.node.get_points_of_interest())
