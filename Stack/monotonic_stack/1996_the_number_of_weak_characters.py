from typing import List

class Solution:

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        '''
        Sort the properties based on ascending order of attack and descending order of defence
        Since defence is sorted locally with descending order when attack is equal, stack will be monotonically decreasing
        In lambda function of sort function, we provide property of sorting within bracket. If there is more than one property, sorting is done based on the order of property
        '''
        properties.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        stack = []

        for attack, defence in properties:
            while stack and stack[-1] < defence:
                result += 1
                stack.pop()
            stack.append(defence)
        return result



properties = [[5,5],[6,3],[3,6]]
sol = Solution()
print(sol.numberOfWeakCharacters(properties=[[5,5],[6,3],[3,6]]))
print(sol.numberOfWeakCharacters(properties=[[2,2],[3,3]]))
print(sol.numberOfWeakCharacters(properties=[[1,5],[10,4],[4,3]]))
