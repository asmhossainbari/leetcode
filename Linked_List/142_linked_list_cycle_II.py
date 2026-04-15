# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        # Step 1: Use slow and fast pointers to detect whether a cycle exists.
        slow = head
        fast = head
        # In Python, the else block after while runs only if the loop ends without hitting break.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # Step 2: Reset one pointer to head and move both one step to find the cycle entry.
        entry_ptr = head
        meet_ptr = slow
        while entry_ptr != meet_ptr:
            entry_ptr = entry_ptr.next
            meet_ptr = meet_ptr.next

        return entry_ptr
