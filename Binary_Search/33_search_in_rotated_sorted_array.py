from typing import List


# In each step, one half is sorted.
# Check whether the target is in the sorted half, then discard the other half.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # left to mid sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left =  mid + 1
            # mid to right sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1



sol = Solution()
print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))  # 4
print(sol.search(nums = [4,5,6,7,0,1,2], target = 3))  # -1
print(sol.search(nums = [1], target = 0))  # -1
