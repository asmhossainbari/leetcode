class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            mid_squre = mid * mid
            if mid_squre == x:
                return mid
            elif mid_squre < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

sol = Solution()
print(sol.mySqrt(x=4))
print(sol.mySqrt(x=8))
print(sol.mySqrt(x=9))
print(sol.mySqrt(x=0))