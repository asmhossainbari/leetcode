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

