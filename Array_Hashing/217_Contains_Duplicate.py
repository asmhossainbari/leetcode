class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                return True
        return False

sol = Solution()
nums = [1,2,3,1]
print(sol.containsDuplicate(nums=nums))