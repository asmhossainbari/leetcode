class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        left = 0
        right = len(numbers) - 1
        while left <= right:
            sum = numbers[left] + numbers[right] 
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))
