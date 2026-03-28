class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
            


sol = Solution()
print(sol.isPerfectSquare(num = 16))  # True
print(sol.isPerfectSquare(num = 14))  # False
print(sol.isPerfectSquare(num = 1))  # True
