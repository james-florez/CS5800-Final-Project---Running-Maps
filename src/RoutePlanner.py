from collections import deque

import geoplotlib

from src.Graph import Graph


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

    def go(self, start_index: int, total_distance: float, mode: int):
        """Plans routes based on starting node index and desired distance.

        Args:
            start_index (int): the index of the starting node
            total_distance (float): the desired route distance in miles
        """

        # Validate input
        if start_index < 0 or start_index >= len(self.my_graph.nodes):
            print("Start index value out of range.")
            return
        if total_distance <= 0:
            print("Total distance must be a positive.")
            return
        if mode <= 0 or mode > 2:
            print("Incorrect mode selection.")
            return

        # Convert the user input from miles to feet.
        total_distance_feet = round(total_distance * 5280)

        # Plan paths using the specified mode (DFS or BFS)
        if mode == 1:
            list_paths = self.plan_dfs(start_index, total_distance_feet)
        else:
            list_paths = self.plan_bfs(start_index, total_distance_feet)

        # Convert the paths to Graphs
        list_graphs = self.convert_paths_to_graphs(list_paths)

        # Sort the Graphs by number of points of interest
        list_graphs.sort(key=lambda x: x.get_num_points_of_interest())

        # Plot the best graph
        self.plot_graph(list_graphs[-1])

        # Print out the points of interest for the best graph
        print(list_graphs[-1].get_points_of_interest())

    def plan_dfs(self, start_index: int, total_distance: int) -> [[int, [int]]]:
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
        path.append(node_index)

        if start_index == node_index and self.check_distance_tolerance(current_distance, total_distance):
            # if not self.is_same_path(list_paths, [current_distance, path]):
            list_paths.append([current_distance, path.copy()])
            del path[-1]  # Backtracking
            return

        for end_node_index, distance in self.my_graph.adjacency_list[node_index].items():
            new_distance = current_distance + distance
            if (not visited[end_node_index] and new_distance < total_distance) or (
                    end_node_index == start_index and self.check_distance_tolerance(new_distance, total_distance)):
                self.dfs_util(start_index, end_node_index, visited, new_distance, total_distance, path, list_paths)

        del path[-1]  # Backtracking
        visited[node_index] = False  # Backtracking
        return

    def is_same_path(self, list_of_paths: [[int, [int]]], current_path: [int, [int]]) -> bool:
        """Checks if a given path is already in the list of paths and returns a bool.

        Args:
            list_of_paths ([[int, [int]]]): The paths that have already been created
            current_path ([int, [int]]): The new path that is being compared
        Returns:
            bool: True if the current_path already exists in list_of_paths and False if it does not
        """

        if len(list_of_paths) == 0:
            return False

        reversed_current_path = current_path.copy()
        reversed_current_path[1].reverse()
        for path in list_of_paths:
            if path[0] == current_path[0] and len(path[1]) == len(current_path[1]):
                for index, value in enumerate(path[1]):
                    if not path[1][index] == current_path[1][index]:
                        return False
                return True
        return False

    def plan_bfs(self, start_index: int, total_distance: int) -> [[int, [int]]]:
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
            if current_node_index == start_index and self.check_distance_tolerance(current_distance, total_distance):
                # if not self.is_same_path(list_paths, current_path):
                list_paths.append(current_path.copy())

            # Add children paths to the queue
            for new_node_index, edge_distance in self.my_graph.adjacency_list[current_node_index].items():
                new_distance = current_distance + edge_distance
                new_node_path = current_node_path.copy()
                new_node_path.append(new_node_index)
                if (new_distance < total_distance and new_node_index not in current_node_path) or (
                        self.check_distance_tolerance(new_distance, total_distance) and new_node_index == start_index):
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
            path = distance_node_list[1]
            for i in range(len(path)):
                node_index = path[i]
                graph.add_node(self.my_graph.get_node(node_index))
                if i != 0:
                    prev_node_index = path[i - 1]
                    distance = self.my_graph.get_distance(prev_node_index, node_index)
                    if distance != 0:
                        graph.add_edge(prev_node_index, node_index, distance)
            list_graphs.append(graph)
        return list_graphs

    def plot_graph(self, graph: Graph):
        """Plots a Graph using geoplotlib.

        Args:
            graph (Graph): The Graph to be plotted
        """
        dict = {'src_lat': [],
                'src_lon': [],
                'dest_lat': [],
                'dest_lon': [],
                }

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
                         color='binary',
                         linewidth=20)

        geoplotlib.show()

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
