from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

sol = Solution()
print(sol.removeElement(nums = [3,2,2,3], val = 3))
print(sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))