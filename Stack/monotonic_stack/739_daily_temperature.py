from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # stack will contain a pair (temperature, index)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_temperature,  stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((temperature, i))
        return result


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73]))
print(sol.dailyTemperatures(temperatures=[30,40,50,60]))
print(sol.dailyTemperatures(temperatures=[30,60,90]))
