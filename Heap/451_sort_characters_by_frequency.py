import collections
import heapq

class Node(object):
    def __init__(self, chars, freq):
        self.chars = chars
        self.freq = freq

    def __lt__(self, other):
       return self.freq > other.freq

class Solution:
    def frequencySort(self, s: str) -> str:
        max_heap = []
        hash_map = collections.defaultdict(int)
        for char in s:
            hash_map[char] += 1

        for char, freq in hash_map.items():
            heapq.heappush(max_heap, Node(char * freq, freq))

        result = ''
        heap_len = len(max_heap)
        for i in range(heap_len):
            result += heapq.heappop(max_heap)
        return result


