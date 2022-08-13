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
        self.planner.go(10, 5, 1)


