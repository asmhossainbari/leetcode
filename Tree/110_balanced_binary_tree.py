from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
n is the number of node in a tree
Time complexity: O(n^2)
Space complexity: O(n)
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def maxHeight(node):
            if not node:
                return 0
            return 1 + max(maxHeight(node.left), maxHeight(node.right))

        if not root:
            return True
        left_subtree_height = maxHeight(root.left)
        right_subtree_height = maxHeight(root.right)
        if abs(left_subtree_height - right_subtree_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

'''
n is the number of node in a tree
Time complexity: O(n)
Space complexity: O(h), here h is height of the tree
    If tree is balanced, h is log(n) in best case scenario
    if tree is unbalanced, h could be n
'''
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)
            balanced = left_subtree[0] and right_subtree[0] and (abs(left_subtree[1] - right_subtree[1]) <= 1)
            return [balanced, 1 + max(left_subtree[1], right_subtree[1])]
        return dfs(root)[0]


