from typing import List

# Smallest possible valid capacity: max(weights)
# Largest necessary capacity: sum(weights)
# The days constraint is 1 <= days <= weights.length <= 5 * 10^4. So, day could be 1. That means all the packages must be delivered in one day.
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipAll(k):
            i = 0
            total_weight = 0
            total_days = 1
            while i < len(weights):
                weight = weights[i]
                if total_weight + weight > k:
                    total_days += 1
                    total_weight = 0
                else:
                    i += 1
                    total_weight = total_weight + weight
            if total_days <= days:
                return True
            else:
                return False


                
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if canShipAll(mid):
                right = mid
            else:
                left = mid + 1
        return left



sol = Solution()
print(sol.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))  # 15
print(sol.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))  # 6
print(sol.shipWithinDays(weights = [1,2,3,1,1], days = 4))  # 3
