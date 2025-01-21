from typing import List

'''
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = dict()
        for n in nums:
            if n not in hashmap.keys():
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        max_freq = -1
        majority_item = nums[0]
        for key, freq in hashmap.items():
            if freq > max_freq:
                max_freq = freq
                majority_item = key
        return majority_item

'''
Time complexity: O(n)
Space complexity: O(1)
Boyer-Moore Voting Algorithm
'''
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 0
        for num in nums:
            if num == candidate:
                counter += 1
            elif counter == 0:
                candidate = num
            else:
                counter -= 1
        return candidate


sol = Solution2()
print(sol.majorityElement(nums = [3,2,3]))
print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))