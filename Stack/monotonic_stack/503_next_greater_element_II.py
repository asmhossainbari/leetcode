from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def nextGreater(num_list):
            result = [0] * len(num_list)
            stack = []
            for i, val in enumerate(num_list):
                while stack and num_list[stack[-1]] < val:
                    stack_index = stack.pop()
                    result[stack_index] = i - stack_index
                stack.append(i)
            return result

        '''
        circular array is address by replicating same array twice
        since length of the array is increased by 2, we need to apply modulo operation to get original indices
        we need to use monotonic stack (increasing)
        '''
        n = len(nums)
        nums = nums * 2
        next_greater_indices = nextGreater(num_list=nums)
        ans = []
        for index in range(n):
            if next_greater_indices[index] == 0:
                ans.append(-1)
            else:
                delta = next_greater_indices[index]
                next_greater_index = (index + delta) % n
                ans.append(nums[next_greater_index])
        return ans


sol = Solution()
print(sol.nextGreaterElements(nums=[1,2,1]))
print(sol.nextGreaterElements(nums = [1,2,3,4,3]))