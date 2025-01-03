from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        
        def backtrack(cur, index):
            if index == len(nums):
                result.append(cur.copy())
                return

            cur.append(nums[index])
            backtrack(cur, index + 1)
            cur.pop()
            backtrack(cur, index + 1)

        backtrack(cur, 0)
        return result


sol = Solution()
print(sol.subsets(nums = [1,2,3]))
print(sol.subsets(nums = [0]))
