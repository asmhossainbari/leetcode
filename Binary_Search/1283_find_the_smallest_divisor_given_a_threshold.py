from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isLessThanThreshold(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
                if total > threshold:
                    return False
            return True

        left = 1
        right = max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if isLessThanThreshold(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
print(sol.smallestDivisor(nums = [1,2,5,9], threshold = 6))  # 5
print(sol.smallestDivisor(nums = [44,22,33,11,1], threshold = 5))  # 44
print(sol.smallestDivisor(nums = [21212,10101,12121], threshold = 1000000))  # 1
