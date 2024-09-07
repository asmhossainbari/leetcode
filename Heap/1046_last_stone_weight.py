import collections
import heapq
from typing import List

class Stone(object):
    def __init__(self, weight):
        self.weight = weight

    def __lt__(self, other):
        return self.weight > other.weight


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, Stone(stone))
        while len(max_heap) > 1:
            first = heapq.heappop(max_heap).weight
            second = heapq.heappop(max_heap).weight
            if first == second:
                continue
            else:
                new_weight = abs(first - second)
                heapq.heappush(max_heap, Stone(new_weight))
        if len(max_heap) == 0:
            return 0
        return max_heap[0].weight

sol = Solution()
print(sol.lastStoneWeight(stones = [2, 7, 4, 1, 8, 1]))
print(sol.lastStoneWeight(stones = [1]))