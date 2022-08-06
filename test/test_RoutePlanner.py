from unittest import TestCase
from src.RoutePlanner import RoutePlanner
from src.Graph import Graph
from src.Node import Node


class TestRoutePlanner(TestCase):
    def setUp(self) -> None:
        # Create Nodes
        self.node0 = Node(0, 0, 0, ["x0", "y0"])
        self.node1 = Node(1, 0, 0, ["x1"])
        self.node2 = Node(2, 0, 0, [])
        self.node3 = Node(3, 0, 0, ["x3", "y3", "z3"])
        self.node4 = Node(4, 0, 0, [])
        self.node5 = Node(5, 0, 0, [])
        self.node6 = Node(6, 0, 0, ["x6", "y6"])
        self.node7 = Node(7, 0, 0, ["x7"])
        self.node8 = Node(8, 0, 0, ["x8"])
        self.node9 = Node(9, 0, 0, ["x9"])
        self.node10 = Node(10, 0, 0, ["x10", "y10"])
        self.node11 = Node(11, 0, 0, [])
        self.node12 = Node(12, 0, 0, ["x12", "y12", "z12"])
        self.nodes = [self.node0, self.node1, self.node2, self.node3, self.node4, self.node5, self.node6, self.node7,
                      self.node8, self.node9, self.node10, self.node11, self.node12]

        # Create Graph
        self.simpleGraph = Graph()

        # Load Nodes
        for node in self.nodes:
            self.simpleGraph.add_node(node)

        # Load Edges
        self.simpleGraph.add_edge(0, 1, 225)
        self.simpleGraph.add_edge(1, 5, 1326)
        self.simpleGraph.add_edge(5, 6, 468)
        self.simpleGraph.add_edge(0, 2, 1275)
        self.simpleGraph.add_edge(2, 7, 2265)
        self.simpleGraph.add_edge(1, 2, 345)
        self.simpleGraph.add_edge(5, 7, 1168)
        self.simpleGraph.add_edge(6, 7, 3456)
        self.simpleGraph.add_edge(0, 3, 465)
        self.simpleGraph.add_edge(3, 2, 1156)
        self.simpleGraph.add_edge(3, 4, 4561)
        self.simpleGraph.add_edge(4, 7, 4563)
        self.simpleGraph.add_edge(3, 9, 788)
        self.simpleGraph.add_edge(9, 10, 3265)
        self.simpleGraph.add_edge(4, 10, 980)
        self.simpleGraph.add_edge(10, 11, 7890)
        self.simpleGraph.add_edge(7, 11, 1102)
        self.simpleGraph.add_edge(11, 12, 458)
        self.simpleGraph.add_edge(6, 8, 1783)
        self.simpleGraph.add_edge(8, 12, 1987)

        # Create RoutePlanner
        self.planner = RoutePlanner(self.simpleGraph)


    def test_plan_dfs(self):
        self.assertEqual([], self.planner.plan_dfs(0, 20000))

    def test_plan_bfs(self):
        self.assertEqual([], self.planner.plan_bfs(0, 5))

    def test_merge_sort(self):
        self.assertEqual([], self.planner.merge_sort(self.planner.plan_dfs(0, 5)))

    def test_counting_sort(self):
        self.assertEqual("", self.planner.counting_sort(self.planner.plan_dfs(0, 5)))
