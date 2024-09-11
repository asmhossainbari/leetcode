class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        reversed_l1 = self.reverseList(head=l1)
        reversed_l2 = self.reverseList(head=l2)
        head = ListNode(0)
        temp = head
        carry = 0
        while reversed_l1 is not None and reversed_l2 is not None:
            sum = reversed_l1.val + reversed_l2.val + carry
            div = sum // 10
            mod = sum % 10
            head.next = ListNode(mod)
            head = head.next
            carry = div
            reversed_l1 = reversed_l1.next
            reversed_l2 = reversed_l2.next

        while reversed_l1 is not None:
            sum = reversed_l1.val + carry
            div = sum // 10
            mod = sum % 10
            head.next = ListNode(mod)
            head = head.next
            carry = div
            reversed_l1 = reversed_l1.next

        while reversed_l2 is not None:
            sum = reversed_l2.val + carry
            div = sum // 10
            mod = sum % 10
            head.next = ListNode(mod)
            head = head.next
            carry = div
            reversed_l2 = reversed_l2.next

        if carry > 0:
            head.next = ListNode(carry)
            head = head.next

        return self.reverseList(temp.next)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        prev = None
        current = head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
