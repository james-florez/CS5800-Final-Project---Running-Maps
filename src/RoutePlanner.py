from typing import Optional

from src.Graph import Graph


class RoutePlanner:
    def __init__(self, graph):
        self.myGraph = graph

    def plan_dfs(self, start_index: int, total_distance: float) -> [Graph]:
        return self.convert_paths_to_graphs(self.plan_dfs_list_paths(start_index, total_distance))

    def plan_dfs_list_paths(self, start_index: int, total_distance: float) -> [int, [int]]:
        # Total number of vertices
        n = len(self.myGraph.adjacency_list)
        # Initialise the visited boolean
        visited = [False] * n

        list_paths = []  # List of paths with the format [distance, [node1, node2, ..., nodeN]]

        # Fill list_paths with all paths that meet loop and distance requirements
        self.dfs_util(start_index, start_index, visited, 0, total_distance, [], list_paths)

        return list_paths

    def dfs_util(self, start_index: int, node_index: int, visited: [bool], current_distance: float, total_distance: float, path: [int], list_paths: [[int]]):

        visited[node_index] = True
        print(node_index)

        path.append(node_index)

        # TODO should we check that current_distance is close to total_distance before adding to list_paths?
        if start_index == node_index and current_distance != 0:
            # TODO is current_distance needed in this tuple? What do we use it for?
            list_paths.append([current_distance, path.copy()])
            del path[-1]  # Backtracking
            return

        for list_edges in self.myGraph.adjacency_list[node_index]:
            if (not visited[list_edges[0]] and (current_distance + list_edges[1]) <= total_distance) or (list_edges[0] == start_index and (current_distance + list_edges[1]) == total_distance):
                self.dfs_util(start_index, list_edges[0], visited, current_distance + list_edges[1], total_distance,
                              path, list_paths)

        del path[-1]  # Backtracking
        visited[node_index] = False  # Backtracking
        return

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
                    # TODO Need to figure how to add edge. Need to record distance between nodes somewhere
            # TODO check if this graph is equivalent to one that was already created
            list_graphs.append(graph)
        return list_graphs

    def merge_sort(self, routes):
        pass

    def counting_sort(self, routes):
        pass
