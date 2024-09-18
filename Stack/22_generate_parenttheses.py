from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        we have two variable open_count and close_count to track the count of the parentheses
        Conditions:
        1. if open_count and close_count equal to n, we have added required parentheses. this is one correct order
        2. we can only add open parentheses if open_count is less than n. If we add open parentheses, we increment the count of open parentheses
        3. we can only add closed parentheses, if close_count is less than open_count
        """
        stack = []
        result = []
        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result

sol = Solution()
print(sol.generateParenthesis(n=3))
print(sol.generateParenthesis(n=1))
print(sol.generateParenthesis(n=8))