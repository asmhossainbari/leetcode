from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def can_make_bouquets(days):
            flower = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flower += 1
                    if flower == k:
                        bouquets += 1
                        flower = 0
                        if bouquets == m:
                            return True

                else:
                    flower = 0
            return bouquets >= m
        
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if can_make_bouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
print(sol.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))  # 3
print(sol.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))  # -1
print(sol.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))  # 12
