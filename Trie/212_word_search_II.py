from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.full_word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()

        for word in words:
            cur_root = self.root
            for ch in word:
                if ch not in cur_root.children:
                    cur_root.children[ch] = TrieNode()
                cur_root = cur_root.children[ch]
            cur_root.word = True

        rows = len(board)
        cols = len(board[0])
        result = set()
        visited = set()
        def dfs(r, c, node, word):
            if ( r < 0 or c < 0
                or r >= rows or c >= cols
                or (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                result.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root, "")
        
        return list(result)

    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.full_word = word

        rows = len(board)
        cols = len(board[0])
        result = []
        visited = set()

        def dfs(r, c, parent):
            if (
                r < 0 or c < 0
                or r >= rows or c >= cols
                or (r, c) in visited
                or board[r][c] not in parent.children
            ):
                return

            ch = board[r][c]
            node = parent.children[ch]

            if node.full_word:
                result.append(node.full_word)
                node.full_word = None

            visited.add((r, c))
            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)
            visited.remove((r, c))

            if not node.children and not node.full_word:
                del parent.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result

sol = Solution()
print(sol.findWords(
    board=[
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],
    words=["oath", "pea", "eat", "rain"],
))
print(sol.findWords(
    board=[
        ["a", "b"],
        ["c", "d"],
    ],
    words=["abcb"],
))
print(sol.findWords2(
    board=[
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],
    words=["oath", "pea", "eat", "rain"],
))
print(sol.findWords2(
    board=[
        ["a", "b"],
        ["c", "d"],
    ],
    words=["abcb"],
))
