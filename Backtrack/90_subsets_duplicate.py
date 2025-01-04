from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sorting makes the repeated value adjacent to each other
        nums.sort()
        result = []
        cur = []

        def backtrack(cur, index):
            if index == len(nums):
                result.append(cur.copy())
                return

            cur.append(nums[index])
            backtrack(cur, index + 1)
            cur.pop()
            # need to skip the duplicate values
            # need to check next value with the prev so index + 1 could be greater than length of the array
            while (index + 1 < len(nums)) and (nums[index + 1] == nums[index]):
                index += 1
            backtrack(cur, index + 1)

        backtrack(cur, 0)
        return result


sol = Solution()
print(sol.subsetsWithDup(nums = [1,2,2]))
print(sol.subsetsWithDup(nums = [0]))