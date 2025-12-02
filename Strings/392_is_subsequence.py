class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_len = len(t)
        s_indx = 0
        s_len = len(s)

        for i in range(t_len):
            if s_indx < s_len and t[i] == s[s_indx]:
                s_indx += 1
        return s_indx == s_len

sol = Solution()
print(sol.isSubsequence(s = "abc", t = "ahbgdc"))
print(sol.isSubsequence(s = "axc", t = "ahbgdc"))
print(sol.isSubsequence(s="", t="ahbgdc"))
print(sol.isSubsequence(s="b", t="abc"))