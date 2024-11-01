from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        min_array = [0] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])

        stack = []
        for i in range(n - 1, -1, -1):
            num_k = nums[i]
            while stack and stack[-1] <= min_array[i]:
                stack.pop()
            if stack and num_k > stack[-1]:
                return True

            stack.append(num_k)
        return False



sol = Solution()
print(sol.find132pattern(nums = [1,2,3,4]))
print(sol.find132pattern(nums = [3,1,4,2]))
print(sol.find132pattern(nums = [-1,3,2,0]))
print(sol.find132pattern(nums = [ 9, 11, 8, 9, 10, 7, 9 ]))