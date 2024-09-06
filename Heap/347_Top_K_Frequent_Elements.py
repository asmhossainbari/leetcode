import collections
import heapq

class Node(object):
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

class Solution(object):
    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     heap = []
    #     dict = {}
    #     for n in nums:
    #         if n not in dict:
    #             dict[n] = 1
    #         else:
    #             dict[n] += 1
    #
    #     for key, value in dict.items():
    #         heapq.heappush(heap, Node(key, value))
    #     result = []
    #     for i in range(k):
    #         result.append(heapq.heappop(heap).val)
    #     return result

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        hash_map = collections.defaultdict(int)
        for n in nums:
            hash_map[n] += 1

        for key, value in hash_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, Node(key, value))
            elif min_heap[0].freq < value:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, Node(key, value))
        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap).val)
        return result
sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
nums = [1]
k = 1
print(sol.topKFrequent(nums=nums, k=k))