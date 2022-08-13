from unittest import TestCase
from BostonGraph import BostonGraph
from RoutePlanner import RoutePlanner


class TestBostonGraph(TestCase):
    def setUp(self) -> None:
        self.boston = BostonGraph()
        self.planner = RoutePlanner(self.boston.get_boston_map())

    def test_get_boston_map(self):
        self.assertTrue(self.boston.get_boston_map())  # Returning the graph counts as True

    def test_boston_map_route_planner_dfs(self):
        # Note that only 1 of these tests can be uncommented at a time

        # Tests with Node 39 as the starting point
        # self.planner.go(39, 0.5, 1)  # This test works
        # self.planner.go(39, 1.0, 1)  # This test works
        # self.planner.go(39, 1.5, 1)  # This test works
        # self.planner.go(39, 2, 1)  # This test works
        self.planner.go(39, 2.5, 1)  # This test works
        # self.planner.go(39, 3, 1)  # TODO this isn't showing part of the route on Tremont
        # self.planner.go(39, 3.5, 1)  # This test works (Takes 3 minutes on James' Macbook)
        # self.planner.go(39, 4, 1)  # TODO Untested (I gave up after running it for 20 minutes)
        # self.planner.go(39, 4.5, 1)  # TODO Untested

        # Tests with Node 27 as the starting point
        self.planner.go(27, 2.5, 1)  # TODO this isn't showing part of the route on Shawmut

        # Tests with Node 82 as the starting point
        self.planner.go(82, 2.5, 1)  # This test works

        # Tests with Node 0 as the starting point
        self.planner.go(0, 2.5, 1)  # This test works

    def test_boston_map_route_planner_bfs(self):
        # Note that only 1 of these tests can be uncommented at a time

        # self.planner.go(39, 0.5, 2)  # This test works
        # self.planner.go(39, 1.0, 2)  # This test works
        # self.planner.go(39, 1.5, 2)  # This test works
        self.planner.go(39, 2, 2)  # This test works

    def test_plot_all_boston(self):
        self.planner.plot_graph(self.boston.get_boston_map())

