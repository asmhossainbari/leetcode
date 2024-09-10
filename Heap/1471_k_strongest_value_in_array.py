import heapq
from typing import List
from functools import cmp_to_key
class Node(object):
    def __init__(self, median, value):
        self.median = median
        self.value = value

    def __lt__(self, other):
        first = abs(self.value - self.median)
        second = abs(other.value - other.median)
        if first == second:
            return self.value < other.value
        else:
            return first < second

# class Comparator:
#     def __init__(self, median, value):
#         self.median = median
#         self.value = value
#
#     def compare(a, other):
#         first = abs(a - self.median)
#         second = abs(other.value - other.median)
#         if first == second:
#             return a.value < other.value
#         else:
#             return first < second

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        sorted_arr = sorted(arr)
        n = len(arr)
        median = sorted_arr[((n - 1) // 2)]

        for num in sorted_arr:
            if len(min_heap) < k:
                heapq.heappush(min_heap, Node(median, num))
            elif min_heap[0].value < num:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, Node(median, num))
        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap).value)
        return result

sol = Solution()
print(sol.getStrongest(arr=[6,-3,7,2,11], k=3))