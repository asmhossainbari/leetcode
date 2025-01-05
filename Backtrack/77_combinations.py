from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        cur = []
        def backtrack(cur, start):
            if len(cur) == k:
                result.append(cur.copy())
                return

            for i in range(start, n + 1):
                cur.append(i)
                backtrack(cur, i + 1)
                cur.pop()

        backtrack(cur, 1)
        return result


sol = Solution()
print(sol.combine(n = 4, k = 2))
print(sol.combine(n = 1, k = 1))


