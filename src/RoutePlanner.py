from typing import Optional

from src.Graph import Graph


class RoutePlanner:
    def __init__(self, graph):
        # Should the graph be an argument in the constructor?
        self.myGraph = graph

    def plan_dfs(self, start_index, distance) -> [Graph]:
        # Total number of vertices

        n = len(self.myGraph.adjacency_list)
        # Initialise the visited boolean
        visited = [False] * n

        list_paths = []

        self.dfs_util(start_index, start_index, visited, self.myGraph.adjacency_list[start_index][1], [], distance, list_paths)

        list_graph = []
        for distance_node_list in list_paths:
            graph = Graph()
            for node_index in distance_node_list[1]:
                graph.add_node(self.myGraph.get_node(node_index))
                # Need to figure how to add edge.
            list_graph.append(graph)

        return list_graph

    def dfs_util(self, start_index, node_index, visited, distance, path: [], total_distance, list_paths) :

        visited[node_index] = True
        print(node_index)

        path.append(node_index)

        if start_index == node_index and distance != 0:
            list_paths.append([distance, path])
            return

        for list_edges in self.myGraph.adjacency_list[node_index]:
            if not visited[list_edges[0]] and (distance + list_edges[1]) <= total_distance:
                self.dfs_util(start_index, list_edges[0], visited, distance + list_edges[1], path, total_distance, list_paths)

        del path[-1]
        return

    def plan_bfs(self, start_index, distance):
        pass

    def merge_sort(self, routes):
        pass

    def counting_sort(self, routes):
        pass
