class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if self.isVowel(s[i]):
                while not self.isVowel(s[j]) and j > i:
                    j -= 1
                s[i], s[j] = s[j], s[i]
                j -= 1
            i += 1

        return "".join(s)                   
            
    def isVowel(self, char):
        if char == 'a' or char == 'A' or char == 'e' or char == 'E' or \
                char == 'o' or char == 'O' or char == 'i' or char == 'I' \
                or char == 'u' or char == 'U':
            return True
        else:
            return False

sol = Solution()
print(sol.reverseVowels(s="hello"))
print(sol.reverseVowels(s="leetcode"))
print(sol.reverseVowels(s="lmottefff"))
