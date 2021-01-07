# class Solution(object):
#     def myAtoi(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         result = 0
#         number_start = False
#         negative = False
#         s = s.strip()
#         if len(s) >= 1 and s[0] != '-' and s[0] != '+' and (s[0] < '0' or s[0] > '9'):
#             return 0
#         for i in range(len(s)):
#             if s[i] == '-' and number_start == False:
#                 negative = True
#                 continue
#             if s[i] == '+' and number_start == False:
#                 negative = False
#                 continue
#             if number_start == True and (s[i] < '0' or s[i] > '9'):
#                 break
#             if (negative == True or negative == False) and (s[i] < '0' or s[i] > '9'):
#                 return 0
#             if '0' <= s[i] <= '9':
#                 result = 10 * result + int(s[i])
#                 number_start = True
#
#         if negative == True:
#             result = -1 * result
#         if result < -2**31 or result > 2**31 - 1:
#             result = -2**31
#
#         return result
#
#
# result = Solution()
# print(result.myAtoi("+-12"))
# print(result.myAtoi("3.14159"))
# print(result.myAtoi("   -42"))
# print(result.myAtoi("words and 987"))
# print(result.myAtoi("4193 with words"))
# print(result.myAtoi("-91283472332"))
# print(result.myAtoi(""))
#
#
#
#

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        is_negative = False
        start_index = 0
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[start_index] == '-':
            is_negative = True
        if s[start_index] == '+' or s[start_index] == '-':
            start_index += 1

        result = 0
        for index in range(start_index, len(s)):
            if s[index] < '0' or s[index] > '9':
                break
            result = result * 10 + int(s[index])
        if is_negative:
            result = -result
        if result < -2**31:
            result = -2**31
        if result > 2**31 -1:
            result = 2**31 - 1
        return result

result = Solution()
# print(result.myAtoi("+-12"))
# print(result.myAtoi("3.14159"))
# print(result.myAtoi("   -42"))
# print(result.myAtoi("words and 987"))
# print(result.myAtoi("4193 with words"))
# print(result.myAtoi("-91283472332"))
# print(result.myAtoi(""))
print(result.myAtoi(" "))
print(result.myAtoi("     +0 123"))

