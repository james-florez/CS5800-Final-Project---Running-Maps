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

        # Create Nodes
        self.node0_new = Node(0, 42.35093, -71.06304, ["x0", "y0"])
        self.node1_new = Node(1, 42.35063, -71.06154, ["x1"])
        self.node2_new = Node(2, 42.35016,  -71.05974, [])
        self.node3_new = Node(3, 42.3524, 71.06455, ["x3", "y3", "z3"])
        self.node4_new = Node(4, 42.35238, -71.06261, [])

        self.nodes_new = [self.node0, self.node1, self.node2, self.node3, self.node4]

        # Create Graph
        self.simpleGraph_new = Graph()

        # Load Nodes
        for node in self.nodes_new:
            self.simpleGraph_new.add_node(node)

        # Load Edges
        self.simpleGraph_new.add_edge(0, 1, 5)
        self.simpleGraph_new.add_edge(1, 2, 5)
        self.simpleGraph_new.add_edge(2, 3, 5)
        self.simpleGraph_new.add_edge(3, 0, 5)
        self.simpleGraph_new.add_edge(3, 4, 5)
        self.simpleGraph_new.add_edge(4, 0, 5)

        # Create RoutePlanner
        self.planner_new = RoutePlanner(self.simpleGraph_new)

    def test_plan_dfs_list_paths(self):
        self.assertEqual([[15, [0, 3, 4, 0]], [15, [0, 4, 3, 0]]], self.planner_new.plan_dfs_list_paths(0, 15))
        #self.assertEqual([[15, [1, 0, 2, 1]], [15, [1, 2, 0, 1]]], self.planner_new.plan_dfs_list_paths(1, 15))
        self.assertEqual([[25, [0, 1, 2, 3, 4, 0]], [25, [0, 4, 3, 2, 1, 0]]],
                         self.planner_new.plan_dfs_list_paths(0, 25))
        self.assertEqual([[2191, [0, 1, 2, 3, 0]], [2191, [0, 3, 2, 1, 0]]], self.planner.plan_dfs_list_paths(0, 2191))

    def test_plan_bfs_list_paths(self):
        self.assertEqual([[15, [0, 3, 4, 0]], [15, [0, 4, 3, 0]]], self.planner_new.plan_bfs_list_paths(0, 15))
        #self.assertEqual([[15, [1, 0, 2, 1]], [15, [1, 2, 0, 1]]], self.planner_new.plan_bfs_list_paths(1, 15))
        self.assertEqual([[25, [0, 1, 2, 3, 4, 0]], [25, [0, 4, 3, 2, 1, 0]]],
                         self.planner_new.plan_bfs_list_paths(0, 25))
        self.assertEqual([[2191, [0, 1, 2, 3, 0]], [2191, [0, 3, 2, 1, 0]]], self.planner.plan_bfs_list_paths(0, 2191))

    def test_check_distance_tolerance(self):
        self.assertTrue(self.planner.check_distance_tolerance(10000, 10000))  # Identical
        self.assertFalse(self.planner.check_distance_tolerance(0, 10000))  # Zero

        # Check 10% tolerance
        self.assertTrue(self.planner.check_distance_tolerance(11000, 10000))
        self.assertFalse(self.planner.check_distance_tolerance(11001, 10000))
        self.assertTrue(self.planner.check_distance_tolerance(9000, 10000))
        self.assertFalse(self.planner.check_distance_tolerance(8999, 10000))

        # Check 0.5 mile tolerance
        self.assertTrue(self.planner.check_distance_tolerance(102640, 100000))
        self.assertFalse(self.planner.check_distance_tolerance(102641, 100000))
        self.assertTrue(self.planner.check_distance_tolerance(97360, 100000))
        self.assertFalse(self.planner.check_distance_tolerance(97359, 100000))

    def test_merge_sort(self):
        self.assertEqual([], self.planner.merge_sort(self.planner.plan_dfs_list_paths(0, 5)))

    def test_counting_sort(self):
        self.assertEqual("", self.planner.counting_sort(self.planner.plan_dfs_list_paths(0, 5)))
