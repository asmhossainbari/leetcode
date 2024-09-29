from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(k):
            time = 0
            for i, pile in enumerate(piles):
                t1 = pile // k
                if pile % k:
                    t1 += 1
                time += t1
            if time <= h:
                return True
            else:
                return False

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if canEatAll(mid):
                high = mid
            else:
                low = mid + 1
        return low


sol = Solution()
print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
