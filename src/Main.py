# CS5800 Final Project
# Running Maps
# by James Florez, Subhankar Shah, and Aashi Shrimal

from Graph import Graph
from RoutePlanner import RoutePlanner


def main():
    # Load a Graph of Boston

    # Create a RoutePlanner object
    dummy_graph = Graph()
    planner = RoutePlanner(dummy_graph)

    # Prompt the user for input
    start_node_index = input("Enter the index of the starting position:\n")
    total_distance = input("Enter the desired loop distance in miles:\n")

    # Use the RoutePlanner to plan acceptable routes
    planner.go()


main()
