import heapq
class Node(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
       return self.val > other.val

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in nums:
            heapq.heappush(heap, Node(i))
        k_th_largest_element = 0
        for i in range(k):
            k_th_largest_element = heapq.heappop(heap).val
        return k_th_largest_element

sol = Solution()
print(sol.findKthLargest(nums=[3,2,1,5,6,4],k = 2))
