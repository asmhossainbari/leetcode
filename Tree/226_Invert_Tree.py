# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left if root.left else None)
        self.invertTree(root.right if root.right else None)
        return root
