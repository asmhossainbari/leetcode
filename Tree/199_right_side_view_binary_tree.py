from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
BFS solution: level order traversal
Children array stores the nodes of each level. Right side view of the level is the last node in the children array
As children array is used, it adds space complexity and run time would be slightly slower as we need to access children array. Moreover, children array is destroyed and created each level. It introduces added runtime.
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            children = []
            for i in range(len(queue)):
                node = queue.popleft()
                children.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(children[-1])
        return result

'''
BFS solution: level order traversal
There is no children array. Queue stores the nodes of each level. When we reach queue length, this is the right side view of the tree.
It reduces runtime and there is no extra space except queue
'''

class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                node = queue.popleft()
                if i == q_len - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result