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
        character_set = set()
        max_substr_length = 0

        while right < len(s):
            if s[right] not in character_set:
                character_set.add(s[right])
                right += 1
                current_set_len = len(character_set)
                if current_set_len > max_substr_length:
                    max_substr_length = current_set_len
            else:
                character_set.remove(s[left])
                left += 1
        return max_substr_length
    
sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
print(sol.lengthOfLongestSubstring(s=""))
