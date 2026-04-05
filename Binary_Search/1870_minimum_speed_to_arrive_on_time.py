from typing import List
from math import ceil

# Speed must positive integer
# Tests are generated such that the answer will not exceed 10^7. So, this is max speed
# 
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1

        def can_make(speed):
            total_time = 0.0
            for i, d in enumerate(dist):
                if i == len(dist) - 1:
                    time = d / speed
                else:
                    time = ceil(d / speed)
                total_time += time
                if total_time > hour:
                    return False
            return True

        left = 1
        right = 10**7
        min_speed = 0
        while left <= right:
            mid = left + (right - left) // 2
            if can_make(mid):
                min_speed = mid
                right = mid - 1
                
            else:
                left = mid + 1
        if min_speed == 0:
            return -1
        else:
            return min_speed
 

sol = Solution()
print(sol.minSpeedOnTime(dist = [1,3,2], hour = 6))  # 1
print(sol.minSpeedOnTime(dist = [1,3,2], hour = 2.7))  # 3
print(sol.minSpeedOnTime(dist = [1,3,2], hour = 1.9))  # -1
