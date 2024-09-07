import collections
import heapq
from typing import List

class Node(object):
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        max_heap = []

        for num in nums:
            if num % 2 == 0:
                hashmap[num] += 1
        if len(hashmap) == 0:
            return -1
        for num, freq in hashmap.items():
            heapq.heappush(max_heap, Node(num, freq))

        parent_node = heapq.heappop(max_heap)
        smallest_value = parent_node.num
        maximum_freq = parent_node.freq


        while len(max_heap) > 0:
            node = heapq.heappop(max_heap)
            if node.freq == maximum_freq and node.num < smallest_value:
                smallest_value = node.num
        return smallest_value

sol = Solution()
print(sol.mostFrequentEven(nums= [0,1,4,4,2,2,1]))
print(sol.mostFrequentEven(nums = [4,4,4,9,2,4]))
print(sol.mostFrequentEven(nums = [29,47,21,41,13,37,25,7]))