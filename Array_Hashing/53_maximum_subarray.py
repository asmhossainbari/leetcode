from typing import List


'''
Time complexity: O(n)
Space complexity: O(1)

Intuition:
At each number, either start a new subarray from that number or extend the
previous subarray. Keep the best sum seen so far.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(sol.maxSubArray([1]))  # 1
print(sol.maxSubArray([5, 4, -1, 7, 8]))  # 23
