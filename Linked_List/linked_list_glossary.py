from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        slow pointer points to head, moves one step at a time
        fast pointer points to head, moves two steps at a time
        since fast pointer moves two steps, fast pointer will point to None before slow pointer
        if slow meets fast pointer, linked list has a cycle
        """

        if head is None:
            return False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def searchKey(self, head: Optional[ListNode], key: int) -> bool:
        if head is None:
            return False
        cur = head
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    def findLength(self,  head: Optional[ListNode]) -> int:
        count = 0
        if head is None:
            return count
        cur = head
        while cur:
            cur = cur.next
            count += 1
        return count