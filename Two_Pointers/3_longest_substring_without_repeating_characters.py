class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        Time Complexity: O(n)
        Space Complexity: O(min(n, m)), where m is the character set size.
        """
        left = 0
        right = 0
        char_set = set()
        max_substr_len = 0

        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_substr_len = max(max_substr_len, len(char_set))
            else:
                char_set.remove(s[left])
                left += 1
        return max_substr_len
    
sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
print(sol.lengthOfLongestSubstring(s=""))
