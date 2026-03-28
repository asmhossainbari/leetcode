from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] > n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left

sol = Solution()
print(sol.hIndex([0, 1, 3, 5, 6]))   # 3
print(sol.hIndex([0, 0, 0, 0]))      # 0
print(sol.hIndex([1]))               # 1
print(sol.hIndex([0, 1, 4, 4, 5, 6]))  # 4
