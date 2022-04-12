class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        character_set = set()
        max_len = 0
        while right < len(s):
            if s[right] not in character_set:
                character_set.add(s[right])
                right += 1
                max_len = max(max_len, len(character_set))
            else:
                character_set.remove(s[left])
                left += 1

        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
print(sol.lengthOfLongestSubstring(s=""))