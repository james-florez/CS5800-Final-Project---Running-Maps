from typing import Optional

from src.Graph import Graph
import numpy
import pyglet
import geoplotlib
from geoplotlib.utils import read_csv
import matplotlib


class RoutePlanner:
    def __init__(self, graph):
        self.myGraph = graph

    # TODO: GO function will be used to initiate the sequence of function calls which will create the list of graphs and sort.
    def go(self):
        # TODO convert the user input which will be in miles to feet.
        pass

    def plan_dfs(self, start_index: int, total_distance: float) -> [Graph]:
        graphs = self.convert_paths_to_graphs(self.plan_dfs_list_paths(start_index, total_distance))
        self.plot_graph(graphs[0])
        return graphs

    def plan_dfs_list_paths(self, start_index: int, total_distance: float) -> [int, [int]]:
        # Total number of vertices
        n = len(self.myGraph.adjacency_list)
        # Initialise the visited boolean
        visited = [False] * n

        list_paths = []  # List of paths with the format [distance, [node1, node2, ..., nodeN]]

        # Fill list_paths with all paths that meet loop and distance requirements
        self.dfs_util(start_index, start_index, visited, 0, total_distance, [], list_paths)

        return list_paths

    def dfs_util(self, start_index: int, node_index: int, visited: [bool], current_distance: float,
                 total_distance: float, path: [int], list_paths: [[int]]):

        visited[node_index] = True
        print(node_index)

        path.append(node_index)

        # TODO should we check that current_distance is close to total_distance before adding to list_paths?
        if start_index == node_index and current_distance != 0:
            # TODO is current_distance needed in this tuple? What do we use it for?
            list_paths.append([current_distance, path.copy()])
            del path[-1]  # Backtracking
            return

        for end_node_index, distance in self.myGraph.adjacency_list[node_index].items():
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

    def plan_bfs(self, start_index: int, total_distance: float) -> [Graph]:
        return self.convert_paths_to_graphs(self.plan_bfs_list_paths(start_index, total_distance))

    def plan_bfs_list_paths(self, start_index: int, total_distance: float) -> [int, [int]]:
        pass

    def convert_paths_to_graphs(self, list_paths: [int, [int]]) -> [Graph]:
        list_graphs = []  # List of Graphs representing the paths
        for distance_node_list in list_paths:
            graph = Graph()
            for i in range(len(distance_node_list[1])):
                node_index = distance_node_list[1][i]
                graph.add_node(self.myGraph.get_node(node_index))
                if i != 0:
                    prev_node_index = distance_node_list[1][i - 1]
                    distance = self.myGraph.get_distance(prev_node_index, node_index)
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

    def merge_sort(self, routes):
        pass

    def counting_sort(self, routes):
        pass
