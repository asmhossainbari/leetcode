from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Compare numbers as strings because the best order depends on
        # concatenation, not numeric value. For example, "3" should come
        # before "30" because "330" is larger than "303".
        strs = [str(num) for num in nums]

        def custom_cmp(a: str, b: str) -> int:
            # If a + b creates a larger number than b + a, place a first.
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        strs.sort(key=cmp_to_key(custom_cmp))
        result = ''.join(strs)

        # When every number is 0, the sorted result looks like "000".
        # The required answer should be the single string "0".
        if result.startswith('0'):
            return '0'
        return result


sol = Solution()
print(sol.largestNumber(nums=[10,2]))
print(sol.largestNumber(nums=[3,30,34,5,9]))
print(sol.largestNumber(nums=[1]))
print(sol.largestNumber(nums=[10]))
print(sol.largestNumber(nums=[0, 0, 0]))
