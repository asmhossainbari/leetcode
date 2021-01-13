# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        val = root.val
        left_child = self.preorderTraversal(root.left)
        right_child = self.preorderTraversal(root.right)
        return [val] + left_child + right_child