import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = []
        self.k = k
        for val in nums:
            heapq.heappush(self.heap, val)

        if len(nums) >= k:
            while len(self.heap) > k:
                heapq.heappop(self.heap)
            self.kth_largest = self.heap[0]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            self.kth_largest = self.heap[0]
            return self.kth_largest

        if val <= self.kth_largest:
            return self.kth_largest
        if val > self.kth_largest:
            heapq.heappushpop(self.heap, val)
            self.kth_largest = self.heap[0]
            return self.kth_largest


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k=3, nums=[4, 5, 8, 2])
param_1 = obj.add(3)
print(param_1)
param_1 = obj.add(5)
print(param_1)
param_1 = obj.add(10)
print(param_1)
param_1 = obj.add(9)
print(param_1)
param_1 = obj.add(4)
print(param_1)
