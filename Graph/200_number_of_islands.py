from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            grid[r][c] = '0'
            if 0 <= r - 1 and grid[r - 1][c] == '1':
                dfs(r - 1, c)
            if r + 1 <= row - 1 and grid[r + 1][c] == '1':
                dfs(r + 1, c)
            if 0 <= c - 1 and grid[r][c- 1] == '1':
                dfs(r, c - 1)
            if c + 1 <= col - 1 and grid[r][c + 1] == '1':
                dfs(r, c + 1)

        num_island = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    num_island += 1
                    dfs(i, j)
        return num_island