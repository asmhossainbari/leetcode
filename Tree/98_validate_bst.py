from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left_boundary, right_boundary):
            if not root:
                return True
            if not (left_boundary < root.val < right_boundary):
                return False

            return dfs(root.left, left_boundary, root.val) and dfs(root.right, root.val, right_boundary)
        return dfs(root, float("-inf"), float("inf"))