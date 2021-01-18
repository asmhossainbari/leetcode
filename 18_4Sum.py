class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) < 4:
            return []
        if len(nums) == 4 and (nums[0] + nums[1] + nums[2] + nums[3]) == target:
            return [ [nums[0], nums[1], nums[2], nums[3]] ]
        result_list = []
        nums.sort()
        i = 0
        while i < len(nums) - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            quad_list = self.threeSum(nums=nums, val_a=nums[i], a_index=i + 1, target=target)
            if len(quad_list) > 0:
                for item in quad_list:
                    result_list.append(item)
            i += 1

        return result_list

    def threeSum(self, nums, val_a, a_index, target):
        quad_list = []
        i = a_index
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1] and i - 1 != a_index - 1:
                i += 1
                continue
            first_ptr = i + 1
            last_ptr = len(nums) - 1
            while first_ptr < last_ptr:
                current_num = nums[i]
                quadruplet_sum = current_num + val_a + nums[first_ptr] + nums[last_ptr]
                if quadruplet_sum < target:
                    first_ptr += 1
                elif quadruplet_sum > target:
                    last_ptr -= 1
                else:
                    quad_list.append([current_num, val_a, nums[first_ptr], nums[last_ptr]])
                    while first_ptr < last_ptr and nums[first_ptr] == nums[first_ptr + 1]:
                        first_ptr += 1
                    while first_ptr < last_ptr and nums[last_ptr] == nums[last_ptr - 1]:
                        last_ptr -= 1
                    first_ptr += 1
                    last_ptr -= 1
            i += 1

        return quad_list


sol = Solution()
print(sol.fourSum(nums=[1,0,-1,0,-2,2], target = 0))
print(sol.fourSum(nums=[0,0,0,0], target = 0))
print(sol.fourSum(nums=[1, 1, 1, 1], target = 4))
print(sol.fourSum(nums=[-2,-1,-1,1,1,2,2], target=0))
