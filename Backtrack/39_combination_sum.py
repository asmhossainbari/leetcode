from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []
        def backtrack(cur, index, cur_target):
            if cur_target < 0:
                return
            if cur_target == 0:
                result.append(cur.copy())
                return

            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                backtrack(cur, i, cur_target - candidates[i])
                cur.pop()

        backtrack(cur, 0, target)
        return result





sol = Solution()
print(sol.combinationSum(candidates = [2,3,6,7], target = 7))
print(sol.combinationSum(candidates = [2,3,5], target = 8))
print(sol.combinationSum(candidates = [2], target = 1))