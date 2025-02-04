from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new_dict = {None: None}
        cur = head
        while cur:
            copy_node = Node(cur.val)
            old_to_new_dict[cur] = copy_node
            cur = cur.next
        cur = head
        while cur:
            copy_node = old_to_new_dict[cur]
            copy_node.next = old_to_new_dict[cur.next]
            copy_node.random = old_to_new_dict[cur.random]
            cur = cur.next

        return old_to_new_dict[head]