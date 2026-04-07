from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_place(distance):
            total_balls = 1
            last_position = position[0]
            for current_position in position[1:]:
                if current_position - last_position >= distance:
                    total_balls += 1
                    last_position = current_position
                    if total_balls == m:
                        return True
            return False


        position = sorted(position)
        left = 1
        right = position[-1] - position[0]
        while left <= right:
            mid = left + (right - left) // 2
            if can_place(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right

sol = Solution()
print(sol.maxDistance(position=[1, 2, 3, 4, 7], m=3))  # 3
print(sol.maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))  # 999999999
print(sol.maxDistance(position=[1, 3, 5, 7, 9], m=3))  # 4
