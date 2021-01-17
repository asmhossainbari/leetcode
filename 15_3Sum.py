class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplet_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            cur_num = nums[i]
            first_ptr = i + 1
            last_ptr = len(nums) - 1
            while first_ptr < last_ptr:
                if cur_num + nums[first_ptr] + nums[last_ptr] < 0:
                    first_ptr = first_ptr + 1
                elif cur_num + nums[first_ptr] + nums[last_ptr] > 0:
                    last_ptr = last_ptr - 1
                else:
                    lst = [cur_num, nums[first_ptr], nums[last_ptr]]
                    triplet_list.append(lst)
                    while first_ptr < last_ptr and (nums[first_ptr] == nums[first_ptr + 1]):
                        first_ptr = first_ptr + 1
                    while first_ptr < last_ptr and (nums[last_ptr] == nums[last_ptr - 1]):
                        last_ptr = last_ptr - 1
                    first_ptr = first_ptr + 1
                    last_ptr = last_ptr - 1

        return triplet_list

    def threeSum_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) == 0:
            return []
        nums.sort()
        triplet_set = set()
        i = 0
        while i < len(nums) - 2:
            current_num = nums[i]
            first_ptr = i + 1
            last_ptr = len(nums) - 1
            while first_ptr < last_ptr:
                triplet_sum = current_num + nums[first_ptr] + nums[last_ptr]
                if triplet_sum < 0:
                    first_ptr += 1
                elif triplet_sum > 0:
                    last_ptr -= 1
                else:
                    triplet_set.add((current_num, nums[first_ptr], nums[last_ptr]))
                    first_ptr += 1
                    last_ptr -= 1
            i += 1
        triplet_list = []
        for i in triplet_set:
            triplet_list.append(list(i))
        return triplet_list


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0, 0, -1, -1, 1, 1]
sol = Solution()
print(sol.threeSum(nums=nums))
