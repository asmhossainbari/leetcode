from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums, target):
            left = 0
            right = len(nums) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                    first = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return first

        def searchRight(nums, target):
            left = 0
            right = len(nums) - 1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                    last = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return last

        leftmost = searchLeft(nums, target)
        if leftmost == -1:
            return [-1, -1]
        rightmost = searchRight(nums, target)
        return [leftmost, rightmost]

sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(sol.searchRange(nums = [], target = 0))