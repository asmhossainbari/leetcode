class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        left = 0
        i = 0
        right = len(nums) - 1
        while i <= right:
            # Move 0s to the beginning.
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            # 1s are already in the middle section.
            elif nums[i] == 1:
                i += 1
            else:
                # Move 2s to the end.
                nums[i], nums[right] = nums[right], nums[i]
                # When you swap with right, do not move i immediately,
                # because the new value brought from the right side is still unknown and must be checked.
                right -= 1
        


nums = [2, 0, 2, 1, 1, 0]
sol = Solution()
sol.sortColors(nums)
print(nums)
