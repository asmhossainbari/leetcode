from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        first_str_len = len(strs[0])

        for i in range(first_str_len):
            flag = False
            for s in strs:
                if not s.startswith(first_str):
                    flag = True
                    break
            if flag:
                first_str = first_str[:-1]
            else:
                return first_str
        return ""

sol = Solution()
print(sol.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix(strs = ["dog","racecar","car"]))
