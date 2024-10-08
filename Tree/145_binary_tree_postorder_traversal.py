from typing import List, Optional
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        left_child = self.postorderTraversal(root.left)
        right_child = self.postorderTraversal(root.right)
        val = root.val
        return left_child + right_child + [val]

    def postorderTraversalRecursiveFunction(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorder(root):
            if not root:
                return root
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
        postorder(root)
        return result