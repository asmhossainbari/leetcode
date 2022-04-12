class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        for key in s_dict.keys():
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
        return True

s = "rat"
t = "cat"
sol = Solution()
print(sol.isAnagram(s, t))