class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            elif len(stack) > 0 and (item == ')' or item == '}' or item == ']'):
                top_item = stack[-1]
                if item == ')' and top_item == '(':
                    stack.pop()
                elif item == '}' and top_item == '{':
                    stack.pop()
                elif item == ']' and top_item == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return len(stack) == 0



sol = Solution()
s = "(]"
s = "()"
s = "()[]{}"
s = "[]["
print(sol.isValid(s))