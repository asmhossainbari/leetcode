class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        result = []
        templist = []
        def backtrack(result, templist, nums):
            if len(templist) == len(nums):
                result.append(templist[:])
                return
            else:
                for i in range(len(nums)):
                    if nums[i] in templist:
                        continue
                    templist.append(nums[i])
                    backtrack(result, templist, nums)
                    templist.pop()

        backtrack(result, templist, nums)
        return result

sol = Solution()
nums = [1,2,3]
# nums = [1]
print(sol.permute(nums=nums))