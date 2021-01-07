class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = dict()
        for i in range(len(nums)):
            if (target - nums[i]) not in dictionary:
                dictionary[nums[i]] = i
            else:
                return [dictionary[target - nums[i]], i]



sol = Solution()
nums = [3, 3]
target = 6
lst = sol.twoSum(nums=nums, target=target)
print(lst)