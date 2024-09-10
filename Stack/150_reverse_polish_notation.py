from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack[0]


sol = Solution()
print(sol.evalRPN(tokens=["2","1","+","3","*"]))
print(sol.evalRPN(tokens=["4","13","5","/","+"]))
print(sol.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))