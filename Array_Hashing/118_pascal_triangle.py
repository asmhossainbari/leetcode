class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_triangle = []
        pascal_triangle.append([1])
        pascal_triangle.append([1, 1])

        row = 2
        while row <= numRows:
            current_row_items = [1]
            col = 0
            while col < (len(pascal_triangle[row - 1]) - 1):
                current_row_items.append(pascal_triangle[row - 1][col] + pascal_triangle[row - 1][col + 1])
                col += 1
            current_row_items.append(1)
            pascal_triangle.append(current_row_items)
            row += 1

        return pascal_triangle


sol = Solution()
print(sol.generate(numRows=5))