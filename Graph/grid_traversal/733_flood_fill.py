from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if image[r][c] != original_color:
                return
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image

        