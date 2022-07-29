from typing import Optional

from src.Graph import Graph


class RoutePlanner:
    def __init__(self, graph):
        # Should the graph be an argument in the constructor?
        self.myGraph = graph

    def plan_dfs(self, start_index, distance) -> [Graph]:
        # Total number of vertices

        n = len(self.myGraph.adjacencyList)
        # Initialise the visited boolean
        visited = [False] * n

        list_paths = []

        for list_edges in self.myGraph[start_index]:
            if not visited[list_edges[0]]:
                list_paths.append(self.dfs_util(start_index, list_edges[0], visited, list_edges[1], [], distance))

        list_graph = []
        for distance_node_list in list_paths[1]:
            graph = Graph()
            for node_index in distance_node_list:
                graph.add_node(self.myGraph.get_node(node_index))
                # Need to figure how to add edge.
            list_graph.append(graph)

        return list_graph

    def dfs_util(self, start_index, node_index, visited, distance, path : [], total_distance) -> ():

        visited[node_index] = True
        print(node_index)

        path.append(node_index)

        if start_index == node_index:
            result_tuple = (distance, path)
            return result_tuple

        for list_edges in self.myGraph[node_index]:
            if not visited[list_edges[0]] and (distance + list_edges[1]) <= total_distance:
                self.dfs_util(start_index, list_edges[0], visited, distance + list_edges[1], path, total_distance)

        return None

    def plan_bfs(self, start_index, distance):
        pass

    def merge_sort(self, routes):
        pass

    def counting_sort(self, routes):
        pass
