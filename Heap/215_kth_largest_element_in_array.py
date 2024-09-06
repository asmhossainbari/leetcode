import heapq
class Node(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
       return self.val > other.val

class Solution(object):
    # time complexity: O(NlogN)
    #
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

    # time complexity: O(NlogK)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            elif nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]


sol = Solution()
print(sol.findKthLargest(nums=[3,2,1,5,6,4],k = 2))
