class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            x_div_mid = x // mid
            if mid == x_div_mid:
                return mid
            elif mid < x_div_mid:
                left = mid + 1
            else:
                right = mid - 1

        return right

sol = Solution()
print(sol.mySqrt(x=4))
print(sol.mySqrt(x=8))
print(sol.mySqrt(x=9))