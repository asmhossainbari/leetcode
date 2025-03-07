from typing import List

'''
TIme complexity: O(logn)
Space complexity: O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        print(left == right)
        return nums[left]


sol = Solution2()
print(sol.findMin(nums = [3,4,5,1,2]))
print(sol.findMin(nums = [4,5,6,7,0,1,2]))
print(sol.findMin(nums = [11,13,15,17]))