from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
If n is the number of node in a binary tree,
Time complexity: O(n)
Space complexity: O(h), here h is height of the tree
    If tree is balanced, h is log(n) in best case scenario
    If tree is unbalanced, h could be n
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # as diameter variable will be update in recursion, diameter variable is set to global variable by making a class member
        self.diameter = 0

        # we calculate the height of the node
        # in addition to the height, we calculate diameter in between
        def dfs(node):
            if not node:
                return 0

            left_child_height = dfs(node.left)
            right_child_height = dfs(node.right)
            # Update the diameter if the path through the current node is longer
            # except the following line, dfs function determines the height of the node
            self.diameter = max(self.diameter, left_child_height + right_child_height)

            return 1 + max(left_child_height, right_child_height)

        dfs(root)
        return self.diameter

'''
Following is another approach of implementation without using member variable.
'''

class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            left_child_height = dfs(node.left)
            right_child_height = dfs(node.right)

            diameter = max(max(left_child_height[0], right_child_height[0]), (left_child_height[1] + right_child_height[1]))

            return [diameter, 1 + max(left_child_height[1], right_child_height[1])]

        return dfs(root)[0]