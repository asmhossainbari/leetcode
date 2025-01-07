from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        cur = []
        end = 10
        def backtrack(cur, index, target):
            if target < 0:
                return
            if target == 0 and len(cur) == k:
                result.append(cur.copy())
                return

            for i in range(index, end):
                cur.append(i)
                backtrack(cur, i + 1, target - i)
                cur.pop()

        backtrack(cur, 1, n)
        return result


sol = Solution()
print(sol.combinationSum3(k = 3, n = 7))
print(sol.combinationSum3(k = 3, n = 9))
print(sol.combinationSum3(k = 4, n = 1))
print(sol.combinationSum3(k = 2, n = 18))
