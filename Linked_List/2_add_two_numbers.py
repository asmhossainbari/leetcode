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
        result = ListNode(0)
        head = result
        carry = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            result.next = ListNode(sum % 10)
            result = result.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            sum = l1.val + carry
            carry = sum // 10
            result.next = ListNode(sum % 10)
            result = result.next
            l1 = l1.next

        while l2 is not None:
            sum = l2.val + carry
            carry = sum // 10
            result.next = ListNode(sum % 10)
            result = result.next
            l2 = l2.next

        if carry > 0:
            result.next = ListNode(carry)

        return head.next


sol = Solution()
print(sol.addTwoNumbers(ListNode(0), ListNode(2)))