from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def nextGreater(nums):
            result = [0] * len(nums)
            stack = []
            for i, val in enumerate(nums):
                while stack and nums[stack[-1]] < nums[i]:
                    stack_index = stack.pop()
                    result[stack_index] = i - stack_index
                stack.append(i)
            return result

        next_greater_list = nextGreater(nums2)
        hashmap = dict()
        for i, val in enumerate(nums2):
            hashmap[val] = i

        ans = []
        for n in nums1:
            num2_index = hashmap[n]
            next_greater_index = next_greater_list[num2_index]
            if next_greater_index == 0:
                ans.append(-1)
            else:
                ans.append(nums2[num2_index + next_greater_index])
        return ans


sol = Solution()
print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(sol.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))