# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)->ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 is not None and l2 is not None:
            total = l1.val + l2.val + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            total = l1.val + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next

        while l2 is not None:
            total = l2.val + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

    # Optimized version: handles both lists and the final carry in a single loop.
    # This keeps the same logic but avoids separate loops for the remaining nodes.
    def addTwoNumbersOptimized(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next


sol = Solution()
print(sol.addTwoNumbers(ListNode(0), ListNode(2)))
