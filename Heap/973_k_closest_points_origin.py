from typing import List
import math
import heapq

class PointDist(object):
    def __init__(self, pt, dist):
        self.point = pt
        self.dist = dist

    def __lt__(self, other):
        return self.dist > other.dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, PointDist(point, dist))
            elif max_heap[0].dist > dist:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, PointDist(point, dist))

        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap).point)
        return result

sol = Solution()
print(sol.kClosest(points = [[1,3],[-2,2]], k = 1))
print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
print(sol.kClosest(points = [[2,2],[2,2],[3,3],[2,-2],[1,1]], k = 4))


