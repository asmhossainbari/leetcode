from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
Time complexity: O(N)
Space complexity: O(1)
N is the number of nodes in the linked list
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        cur = head
        while cur:
            cur = cur.next
            list_length += 1

        remove_index = list_length - n
        if remove_index == 0:
            return head.next

        start_index = 0
        cur = head
        while start_index < list_length:
            if start_index + 1 == remove_index:
                cur.next = cur.next.next
                break
            cur = cur.next
            start_index += 1

        return head

