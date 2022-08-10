from typing import Optional

from src.Graph import Graph
import numpy
import pyglet
import geoplotlib
from geoplotlib.utils import read_csv
import matplotlib


class RoutePlanner:
    """A class used to plan routes through a Graph (city map)

    Attributes:
        my_graph (Graph): the Graph used for planning routes through
    """

    def __init__(self, graph: Graph):
        """Initializes a RoutePlanner object.

        Args:
            graph (Graph): the Graph to be used for planning routes through
        """

        self.my_graph = graph

    # TODO: GO function will be used to initiate the sequence of function calls which will create the list of graphs and sort.
    def go(self):
        # TODO convert the user input which will be in miles to feet.
        pass

    def plan_dfs(self, start_index: int, total_distance: float) -> [Graph]:
        """Plans routes of a given distance using DFS.

        Args:
            start_index (int): the index of the node to start the routes from
            total_distance (int): the desired total distance of the route in feet
        Returns:
            [Graph]: List of Graphs representing loop routes of acceptable distance
        """

        graphs = self.convert_paths_to_graphs(self.plan_dfs_list_paths(start_index, total_distance))
        self.plot_graph(graphs[0])
        return graphs

    def plan_dfs_list_paths(self, start_index: int, total_distance: float) -> [[int, [int]]]:
        """Plans routes of a given distance using DFS.

        Args:
            start_index (int): the index of the node to start the routes from
            total_distance (int): the desired total distance of the route in feet
        Returns:
            [[int, [int]]]: List of paths with the format [distance, [node1, node2, ..., nodeN]]
        """

        # Total number of vertices
        n = len(self.my_graph.adjacency_list)
        # Initialise the visited boolean
        visited = [False] * n

        list_paths = []  # List of paths with the format [distance, [node1, node2, ..., nodeN]]

        # Fill list_paths with all paths that meet loop and distance requirements
        self.dfs_util(start_index, start_index, visited, 0, total_distance, [], list_paths)

        return list_paths

    def dfs_util(self, start_index: int, node_index: int, visited: [bool], current_distance: int,
                 total_distance: int, path: [int], list_paths: [[int, [int]]]):
        """Utility method to recursively plan routes with DFS.

        Args:
            start_index (int): the index of the starting point of the routes
            node_index (int): the index of the current location
            visited ([bool]): list of bools representing if nodes with corresponding indices have been visited
            current_distance (int): the current path distance
            total_distance (int): the desired total distance
            path ([int]): path with the format [node1, node2, ..., nodeN]
            list_paths ([[int, [int]]]): List of paths with the format [distance, [node1, node2, ..., nodeN]]
        """

        visited[node_index] = True
        print(node_index)

        path.append(node_index)

        # TODO should we check that current_distance is close to total_distance before adding to list_paths?
        if start_index == node_index and current_distance != 0:
            # TODO is current_distance needed in this tuple? What do we use it for?
            list_paths.append([current_distance, path.copy()])
            del path[-1]  # Backtracking
            return

        for end_node_index, distance in self.my_graph.adjacency_list[node_index].items():
            if (not visited[end_node_index] and (current_distance + distance) <= total_distance) or (
                    end_node_index == start_index and (current_distance + distance) == total_distance):
                self.dfs_util(start_index, end_node_index, visited, current_distance + distance, total_distance,
                              path, list_paths)

        del path[-1]  # Backtracking
        visited[node_index] = False  # Backtracking
        return

    # TODO Reverse the node list and check if the two lists are equivalent to each other or not
    def isSamePath(self) -> bool:
        return False

    def plan_bfs(self, start_index: int, total_distance: int) -> [Graph]:
        """Plans routes of a given distance using BFS.

        Args:
            start_index (int): the index of the node to start the routes from
            total_distance (int): the desired total distance of the route in feet
        Returns:
            [Graph]: List of Graphs representing loop routes of acceptable distance
        """
        return self.convert_paths_to_graphs(self.plan_bfs_list_paths(start_index, total_distance))

    def plan_bfs_list_paths(self, start_index: int, total_distance: int) -> [[int, [int]]]:
        """Plans routes of a given distance using BFS.

        Args:
            start_index (int): the index of the node to start the routes from
            total_distance (int): the desired total distance of the route in feet
        Returns:
            [[int, [int]]]: List of paths with the format [distance, [node1, node2, ..., nodeN]]
        """

        list_paths = []  # List of paths with the format [distance, [node1, node2, ..., nodeN]]
        q = deque()  # Create a queue for BFS
        q.append([0, [start_index]])  # Append the starting node with a distance of 0
        while q:
            # Get the current path information
            current_path = q.popleft()  # Path with the format [distance, [node1, node2, ..., nodeN]]
            current_distance = current_path[0]
            current_node_path = current_path[1]
            current_node_index = current_node_path[-1]  # Current node is the last one in the list

            # If a loop of acceptable distance is formed add it to list_paths
            # TODO update with distance tolerance function
            if current_node_index == start_index and current_distance == total_distance:
                list_paths.append(current_path.copy())

            # Add children paths to the queue
            connected_nodes = self.my_graph.adjacency_list[current_node_index]
            for connected_node in connected_nodes:
                new_distance = current_distance + connected_node[1]
                new_node_index = connected_node[0]
                new_node_path = current_node_path.copy()
                new_node_path.append(new_node_index)
                # TODO update with distance tolerance function
                if (new_distance <= total_distance and new_node_index not in current_node_path)\
                        or (new_distance == total_distance and new_node_index == start_index):
                    q.append([new_distance, new_node_path])

        return list_paths

    def convert_paths_to_graphs(self, list_paths: [[int, [int]]]) -> [Graph]:
        """Converts a list of paths to a list of Graphs.

        Args:
            list_paths ([[int, [int]]]): List of paths with the format [distance, [node1, node2, ..., nodeN]]
        Returns:
            [Graph]: List of Graphs converted from the list of paths
        """

        list_graphs = []  # List of Graphs representing the paths
        for distance_node_list in list_paths:
            graph = Graph()
            for i in range(len(distance_node_list[1])):
                node_index = distance_node_list[1][i]
                graph.add_node(self.my_graph.get_node(node_index))
                if i != 0:
                    prev_node_index = distance_node_list[1][i - 1]
                    distance = self.my_graph.get_distance(prev_node_index, node_index)
                    if distance != 0:
                        graph.add_edge(prev_node_index, node_index, distance)
            # TODO check if this graph is equivalent to one that was already created
            list_graphs.append(graph)
        return list_graphs

    # TODO : Plot the graph using geoplotlib.
    def plot_graph(self, graph: Graph) -> {}:
        dict = {'src_lat': [],
                'src_lon': [],
                'dest_lat': [],
                'dest_lon': [],
                }

        # TODO: There are repeats while adding the values in the dictionary, we need to figure that out.
        for node in graph.nodes.values():
            node_index = node.get_index()
            for end_node_index in graph.adjacency_list[node.get_index()].keys():
                dict['src_lat'] += [node.get_latitude()]
                dict['src_lon'] += [node.get_longitude()]
                dict['dest_lat'] += [graph.get_node(end_node_index).get_latitude()]
                dict['dest_lon'] += [graph.get_node(end_node_index).get_longitude()]


        data = dict
        geoplotlib.graph(data,
                         src_lat='src_lat',
                         src_lon='src_lon',
                         dest_lat='dest_lat',
                         dest_lon='dest_lon',
                         color='hot_r',
                         alpha=100,
                         linewidth=20)

        geoplotlib.show()

        return dict

    def check_distance_tolerance(self, current_distance: int, total_distance: int) -> bool:
        """Checks if the current distance is within an acceptable tolerance of the total distance.

        Uses either 0.5 miles or 10% of the total distance, whichever is smaller.

        Returns:
            bool: True if the current distance with within tolerance and False if not
        """
        half_mile = 2640  # 2640 ft == 0.5 miles
        ten_percent_tolerance = total_distance * 0.1
        # Use whatever tolerance is smaller (0.5 miles or 10% of total_distance)
        if half_mile <= ten_percent_tolerance:
            upper_bound = total_distance + half_mile
            lower_bound = total_distance - half_mile
        else:
            upper_bound = total_distance + ten_percent_tolerance
            lower_bound = total_distance - ten_percent_tolerance
        return lower_bound <= current_distance <= upper_bound

    def merge_sort(self, routes):
        pass

    def counting_sort(self, routes):
        pass
