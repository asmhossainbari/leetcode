class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = dict()
        dictionary['I'] = 1
        dictionary['V'] = 5
        dictionary['X'] = 10
        dictionary['L'] = 50
        dictionary['C'] = 100
        dictionary['D'] = 500
        dictionary['M'] = 1000

        str_len = len(s)
        i = 0
        result = 0
        while i < str_len:
            cur_char = s[i]
            cur_value = dictionary[cur_char]
            if (i + 1 < str_len) and dictionary[s[i]] < dictionary[s[i+1]]:
                result = result - cur_value
            else:
                result = result + cur_value
            i = i + 1
        return result


sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
