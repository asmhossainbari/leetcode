from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(left_ptr, right_ptr):
            first = -1
            while left_ptr <= right_ptr:
                mid_ptr = (left_ptr + right_ptr) // 2
                if nums[mid_ptr] == target:
                    first = mid_ptr
                    right_ptr = mid_ptr - 1
                elif target < nums[mid_ptr]:
                    right_ptr = mid_ptr - 1
                else:
                    left_ptr = mid_ptr + 1
            return first

        def binarySearchRight(left_ptr, right_ptr):
            last = -1
            while left_ptr <= right_ptr:
                mid_ptr = (left_ptr + right_ptr) // 2
                if nums[mid_ptr] == target:
                    last = mid_ptr
                    left_ptr = mid_ptr + 1
                elif target < nums[mid_ptr]:
                    right_ptr = mid_ptr - 1
                else:
                    left_ptr = mid_ptr + 1
            return last

        nums_len = len(nums)
        left_most = binarySearchLeft(0, nums_len - 1)
        right_most = binarySearchRight(0, nums_len - 1)


        return [left_most, right_most]


sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(sol.searchRange(nums = [], target = 0))