class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(n log n + n^2) = O(n^2)
        # Space Complexity: O(1), excluding the output list
        triplet_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            cur_num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if cur_num + nums[left] + nums[right] < 0:
                    left = left + 1
                elif cur_num + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    triplet_sum = [cur_num, nums[left], nums[right]]
                    triplet_list.append(triplet_sum)
                    while left < right and (nums[left] == nums[left + 1]):
                        left = left + 1
                    while left < right and (nums[right] == nums[right - 1]):
                        right = right - 1
                    left = left + 1
                    right = right - 1

        return triplet_list

    def threeSum_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(n log n + n^2) = O(n^2)
        # Space Complexity: O(k), where k is the number of unique triplets
        nums.sort()
        triplet_set = set()
        i = 0
        while i < len(nums) - 2:
            current_num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                triplet_sum = current_num + nums[left] + nums[right]
                if triplet_sum < 0:
                    left += 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    triplet_set.add((current_num, nums[left], nums[right]))
                    left += 1
                    right -= 1
            i += 1
        triplet_list = []
        for i in triplet_set:
            triplet_list.append(list(i))
        return triplet_list


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0, 0, -1, -1, 1, 1]
sol = Solution()
print(sol.threeSum(nums=nums))
