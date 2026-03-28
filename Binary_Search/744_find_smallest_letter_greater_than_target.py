from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        if letters[left] <= target:
            return letters[0]
        else:
            return letters[left]


sol = Solution()
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))