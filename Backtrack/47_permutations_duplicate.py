class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        templist = []
        used = [False for i in range(len(nums))]
        nums.sort()
        def backtrack(result, templist, nums, used):
            if len(templist) == len(nums):
                result.append(templist[:])
            else:
                for i in range(len(nums)):
                    if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                        continue
                    used[i] = True
                    templist.append(nums[i])
                    backtrack(result, templist, nums, used)
                    used[i] = False
                    templist.pop()

        backtrack(result, templist, nums, used)
        return result


sol = Solution()
nums = [1,1,3]
# nums = [1]
print(sol.permuteUnique(nums=nums))