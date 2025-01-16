from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Time complexity: O(h
'''
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # left_tree_size = self.countNodes(root.left)
        # right_tree_size = self.countNodes(root.right)
        # return left_tree_size + right_tree_size + 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
