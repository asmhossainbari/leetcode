from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(sol.maxArea(height = [1,1]))

