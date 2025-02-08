from typing import List

class Solution:
    def buildAdjacencyList(self, numCourses, prerequisites):
        adjacency_list = {i: [] for i in range(numCourses)}
        for v1, v2 in prerequisites:
            adjacency_list[v2].append(v1)
        return adjacency_list

    def topoBFS(self, numCourses, prerequisites):
        adjacency_list = self.buildAdjacencyList(numCourses, prerequisites)
        in_degree = [0] * numCourses
        for v1, v2 in prerequisites:
            in_degree[v1] += 1
        queue = []
        for v in range(numCourses):
            if in_degree[v] == 0:
                queue.append(v)
        count = 0
        topo_order = []
        while queue:
            node = queue.pop(0)
            topo_order.append(node)
            count += 1
            for neighbor in adjacency_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if count == numCourses:
            return topo_order
        else:
            return []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.topoBFS(numCourses, prerequisites)