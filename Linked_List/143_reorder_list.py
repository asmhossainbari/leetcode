from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # step 1: Find the middle of the list. After the loop, slow is the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Disconnect first and second half of the list
        cur = slow.next
        slow.next = None

        # Step 2: Reverse the second half of the list. After the loop, prev is the head of the reversed second half of the list
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Step 3: Merge first and second half of the list. Second half is the closest to the end of the list. Thus, we iterate over the second half of the list
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

