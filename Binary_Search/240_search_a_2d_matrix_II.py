from typing import List

'''
Rows are sorted left to right
Columns are sorted top to bottom
So if we start at the top-right corner:
    moving left gives smaller values
    moving down gives larger values

Moving left means decreasing the column
Moving down means increasing the row
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # Start from the top-right corner
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False



sol = Solution()
print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))  # True
print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))  # False
print(sol.searchMatrix(matrix = [[-5]], target = -5))  # True
