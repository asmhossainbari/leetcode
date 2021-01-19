class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = len(mat)
        col = row
        diagonal_sum = 0
        i = 0
        j = 0
        while i < row and j < col:
            diagonal_sum += mat[i][j]
            i += 1
            j += 1

        m = 0
        n = col - 1
        while m < row and n > -1:
            diagonal_sum += mat[m][n]
            m += 1
            n -= 1

        if row % 2 == 1:
            diagonal_sum -= mat[row // 2][col // 2]
        return diagonal_sum


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]

mat = [[7, 3, 1, 9], [3, 4, 6, 9], [6, 9, 6, 6], [9, 5, 8, 5]]
sol = Solution()
print(sol.diagonalSum(mat=mat))
