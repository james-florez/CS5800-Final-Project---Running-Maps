from unittest import TestCase
from BostonGraph import BostonGraph
from RoutePlanner import RoutePlanner


class TestBostonGraph(TestCase):
    def setUp(self) -> None:
        self.boston = BostonGraph()
        self.planner = RoutePlanner(self.boston.get_boston_map())

    def test_get_boston_map(self):
        self.assertTrue(self.boston.get_boston_map())  # Returning the graph counts as True

    def test_boston_map_route_planner(self):
        self.planner.go(39, 0.5, 1)  # This test works

    def test_plot_all_boston(self):
        self.planner.plot_graph(self.boston.get_boston_map())

