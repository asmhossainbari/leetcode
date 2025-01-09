# Google Interview Question
# time complexity: sort(nlogn) + n ==> nlogn
# space complexity: O(1) => ignoring required space for sorting

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         nums = list(set(nums))
#         nums.sort()
#         left = 0
#         right = 1
#         max_len = 1
#         while right < len(nums):
#             if nums[right] == nums[right - 1] + 1:
#                 max_len = max(max_len, right - left + 1)
#                 right += 1
#             else:
#                 left = right
#                 right += 1
#         return max_len

# time complexity: O(n)
# space complexity: O(n) -> for set
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        for n in nums:
            if (n - 1) not in num_set:
                seq_len = 1
                while (n + seq_len) in num_set:
                    seq_len += 1
                max_len = max(max_len, seq_len)
        return max_len

nums = []
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,2,0,1]
nums = [0]
nums = [0,-1]
nums = []

sol = Solution()
print(sol.longestConsecutive(nums))


