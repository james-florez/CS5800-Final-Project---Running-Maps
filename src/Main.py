# CS5800 Final Project
# Running Maps
# by James Florez, Subhankar Shah, and Aashi Shrimal

from Graph import Graph
from RoutePlanner import RoutePlanner
from BostonGraph import BostonGraph

def main():
    # Load a Graph of Boston

    # Create a RoutePlanner object
    boston_graph = BostonGraph()
    planner = RoutePlanner(boston_graph.get_boston_map())

    # Prompt the user for input
    start_node_index = int(input("Enter the index of the starting position:\n"))
    total_distance = float(input("Enter the desired loop distance in miles:\n"))
    mode = int(input("Enter 1 for DFS or 2 for BFS:\n"))

    # Use the RoutePlanner to plan acceptable routes
    planner.go(start_node_index, total_distance, mode)


main()
