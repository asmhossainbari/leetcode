class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) == 1:
            return False

        parentheses_dict = dict()
        parentheses_dict['('] = ')'
        parentheses_dict['{'] = '}'
        parentheses_dict['['] = ']'
        parentheses_list = [s[0]]
        i = 1
        while i < len(s):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                parentheses_list.append(s[i])
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(parentheses_list) > 0:
                    closed_parentheses = parentheses_list.pop()
                    if closed_parentheses == ')' or closed_parentheses == '}' or closed_parentheses == ']':
                        return False
                    if s[i] != parentheses_dict[closed_parentheses]:
                        return False
                else:
                    return False
            i += 1
        if len(parentheses_list) > 0:
            return False
        else:
            return True


sol = Solution()
s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
s = "(){}}{"
s = "[])"
s = "))"
print(sol.isValid(s=s))
