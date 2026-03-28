from typing import List


# Same binary-search idea as LeetCode 33, but here duplicates are allowed.
# When nums[left] == nums[mid] == nums[right], we cannot tell which half is sorted,
# so shrink both ends and continue.
# other logics are same as leetcode 33
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

            


sol = Solution()
print(sol.search(nums = [2,5,6,0,0,1,2], target = 0))  # True
print(sol.search(nums = [2,5,6,0,0,1,2], target = 3))  # False
print(sol.search(nums = [1,0,1,1,1], target = 0))  # True
