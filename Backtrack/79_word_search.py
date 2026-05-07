from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None:
            return False

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or c < 0
                or r >= rows or c >= cols
                or board[r][c] != word[i]
                or (r, c) in visited
            ):
                return False

            # Mark current cell so the same path cannot reuse it.
            visited.add((r, c))
            result = (
                dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
            )
            # Remove it before returning so other starting paths can use it.
            visited.remove((r, c))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                
        return False



sol = Solution()
print(sol.exist(
    board=[
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ],
    word="ABCCED",
))
print(sol.exist(
    board=[
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ],
    word="SEE",
))
print(sol.exist(
    board=[
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ],
    word="ABCB",
))
