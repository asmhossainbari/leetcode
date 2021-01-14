class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2_next_greater_dict = dict()
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[i]:
                popped_index = stack.pop()
                nums2_next_greater_dict[nums2[popped_index]] = nums2[i]
            stack.append(i)
        next_greater_list = []
        for i in nums1:
            if i in nums2_next_greater_dict:
                next_greater_list.append(nums2_next_greater_dict[i])
            else:
                next_greater_list.append(-1)
        return next_greater_list
    

sol = Solution()
print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(sol.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))