class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_root = self.root
        for ch in word:
            if ch not in cur_root.children:
                cur_root.children[ch] = TrieNode()
            cur_root = cur_root.children[ch]
        cur_root.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur_root = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in cur_root.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    ch = word[i]
                    if ch not in cur_root.children:
                        return False
                    cur_root = cur_root.children[ch]
            return cur_root.end_of_word 
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
