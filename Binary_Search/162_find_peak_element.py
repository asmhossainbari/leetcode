from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
print(sol.findPeakElement([1, 2, 3, 1]))  # 2
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 1 or 5
print(sol.findPeakElement([1]))  # 0
print(sol.findPeakElement([2, 1]))  # 0
print(sol.findPeakElement([1, 2]))  # 1
print(sol.findPeakElement([1, 3, 2]))  # 1
print(sol.findPeakElement([3, 2, 1]))  # 0
