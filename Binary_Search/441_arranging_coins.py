# Binary search the maximum number of complete rows whose total coins
# mid * (mid + 1) / 2 does not exceed n.
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            mid_square = (mid * (mid + 1)) // 2
            if mid_square == n:
                return mid
            elif mid_square < n:
                left = mid + 1
            else:
                right = mid - 1
        return right


sol = Solution()
print(sol.arrangeCoins(n = 5))  # 2
print(sol.arrangeCoins(n = 8))  # 3
print(sol.arrangeCoins(n = 1))  # 1
