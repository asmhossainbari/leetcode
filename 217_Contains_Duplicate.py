class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dictionary = dict()
        for i in range(len(nums)):
            if nums[i] not in num_dictionary:
                num_dictionary[nums[i]] = i
            else:
                return True
        return False

sol = Solution()
input = [1, 2, 3]
print(sol.containsDuplicate(nums=input))
