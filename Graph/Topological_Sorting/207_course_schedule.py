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

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

'''
Kahn's algorithm
Time complexity: O (V + E)
Space complexity: O (V + E)
where V is the number of courses and E is the number of prerequisites
'''
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adjacency_list = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            in_degree[dst] += 1
            adjacency_list[src].append(dst)

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        finish_course = 0
        while queue:
            node = queue.popleft()
            finish_course += 1
            for neighbour in adjacency_list[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if finish_course == numCourses:
            return True
        else:
            return False


'''
Solution 3 implementation is much better than solution 2 though the time and space complexity is same.
deque is not used here.
'''
class Solution3:
    def buildAdjacencyList(self, n, edgeList):
        adjacency_list = {i: [] for i in range(n)}
        for v1, v2 in edgeList:
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
        while queue:
            node = queue.pop(0)
            count += 1
            for des in adjacency_list[node]:
                in_degree[des] -= 1
                if in_degree[des] == 0:
                    queue.append(des)

        if count != numCourses:
            return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if self.topoBFS(numCourses, prerequisites):
            return True
        else:
            return False