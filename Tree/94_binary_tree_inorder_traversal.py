# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        left_child = self.inorderTraversal(root.left)
        val = root.val
        right_child = self.inorderTraversal(root.right)
        return left_child + [val] + right_child
