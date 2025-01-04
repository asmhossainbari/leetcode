class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur = []
        result = []
        visited = [False for i in range(len(nums))]

        def backtrack(cur, visited):
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                cur.append(nums[i])
                visited[i] = True
                backtrack(cur, visited)
                cur.pop()
                visited[i] = False

        backtrack(cur, visited)
        return result

sol = Solution()
nums = [1,2,3]
# nums = [1]
print(sol.permute(nums=nums))