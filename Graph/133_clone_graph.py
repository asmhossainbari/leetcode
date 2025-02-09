
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque

'''
DFS solution
Time complexity O(V + E)
Space complexity O(V)
where V is the number of vertice and E is the number edges
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new_map = {}
        def dfs(node):
            if node in old_to_new_map:
                return old_to_new_map[node]
            copy = Node(node.val)
            old_to_new_map[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        if node:
            return dfs(node)
        else:
            return None


'''
BFS solution
Time complexity O(V + E)
Space complexity O(V)
where V is the number of vertice and E is the number edges
'''

class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new_map = {}
        copy = Node(node.val)
        old_to_new_map[node] = copy
        queue = deque()
        queue.append(node)
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in old_to_new_map:
                    old_to_new_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new_map[cur_node].neighbors.append(old_to_new_map[neighbor])

        return old_to_new_map[node]

