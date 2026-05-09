from typing import List


'''
Time complexity: O(n)
Space complexity: O(1), ignoring the output array

Intuition:
For each index, answer = product of all numbers on the left * product of all numbers on the right.
First pass stores prefix products in result.
Second pass multiplies each position by the running suffix product.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1

        for i, num in enumerate(nums):
            result[i] = prefix
            prefix *= num

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))      # [24, 12, 8, 6]
print(sol.productExceptSelf([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
