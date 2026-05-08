from collections import deque
from typing import List

'''
DFS solution
Time complexity: O (V + E)
Space complexity: O (V + E)
where V is the number of courses and E is the number of prerequisites
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  dictionary for each course to its prerequisites
        prerequisite_map = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisite_map[course].append(prerequisite)

        # need a set to store the visited status of the course
        visited = set()

        def dfs(crs):
            # if course is in visited, cycle is found
            if crs in visited:
                return False

            # if prerequisite is empty, we can finish the course
            if not prerequisite_map[crs]:
                return True

            visited.add(crs)
            for pre in prerequisite_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prerequisite_map[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

'''
BFS solution
Kahn's algorithm
Time complexity: O (V + E)
Space complexity: O (V + E)
'''
class Solution2:
    def buildAdjacencyList(self, n, edgeList):
        adjacency_list = {i: [] for i in range(n)}
        for v1, v2 in edgeList:
            adjacency_list[v2].append(v1)
        return adjacency_list

    def topoBFS(self, numCourses, prerequisites):
        adjacency_list = self.buildAdjacencyList(numCourses, prerequisites)
        in_degree = [0] * numCourses
        for v1, _ in prerequisites:
            in_degree[v1] += 1
        queue = deque()
        for v in range(numCourses):
            if in_degree[v] == 0:
                queue.append(v)

        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for des in adjacency_list[node]:
                in_degree[des] -= 1
                if in_degree[des] == 0:
                    queue.append(des)

        if count != numCourses:
            return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.topoBFS(numCourses, prerequisites)
