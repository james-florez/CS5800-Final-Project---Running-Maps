from unittest import TestCase
from src.RoutePlanner import RoutePlanner
from src.Graph import Graph
from src.Node import Node


class TestRoutePlanner(TestCase):
    def setUp(self) -> None:
        self.nodes = []
        self.node0 = Node(0, 0, 0, 2, ["x0", "y0"])
        self.node1 = Node(1, 0, 0, 1, ["x1"])
        self.node2 = Node(2, 0, 0, 0, [])
        self.node3 = Node(3, 0, 0, 3, ["x3", "y3", "z3"])
        self.node4 = Node(4, 0, 0, 2, ["x0", "y0"])
        self.node5 = Node(5, 0, 0, 2, ["x0", "y0"])
        self.node6 = Node(6, 0, 0, 2, ["x0", "y0"])
        self.simpleGraph = Graph()
        self.planner = RoutePlanner(self.simpleGraph)


    def test_plan_dfs(self):
        self.fail()

    def test_plan_bfs(self):
        self.fail()

    def test_merge_sort(self):
        self.fail()

    def test_counting_sort(self):
        self.fail()
