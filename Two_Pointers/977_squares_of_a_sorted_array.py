class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        index = right
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                result[index] = nums[right] ** 2
                right -= 1
            else:
                result[index] = nums[left] ** 2
                left += 1
            index -= 1
        return result


sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10]))
print(sol.sortedSquares([-7, -3, 2, 3, 11]))
print(sol.sortedSquares([-5]))
print(sol.sortedSquares([0]))
print(sol.sortedSquares([1, 2, 3]))
print(sol.sortedSquares([-3, -2, -1]))
print(sol.sortedSquares([-2, -1, 3]))
