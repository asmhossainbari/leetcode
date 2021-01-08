class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_pointer = 0
        second_pointer = 0
        character_dict = dict()
        max_substr_length = 0

        while second_pointer < len(s):
            if s[second_pointer] not in character_dict:
                character_dict[s[second_pointer]] = 1
                second_pointer += 1
                current_dict_len = len(character_dict)
                if current_dict_len > max_substr_length:
                    max_substr_length = current_dict_len
            else:
                del character_dict[s[first_pointer]]
                first_pointer += 1
        return max_substr_length
    
sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
print(sol.lengthOfLongestSubstring(s=""))
