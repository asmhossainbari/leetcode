from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []
        candidates.sort()

        def backtrack(cur, index, cur_target):
            if cur_target < 0:
                return
            if cur_target == 0:
                result.append(cur.copy())
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, cur_target - candidates[i])
                cur.pop()

        backtrack(cur, 0, target)
        return result




sol = Solution()
print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(sol.combinationSum2(candidates = [2,5,2,1,2], target = 5))