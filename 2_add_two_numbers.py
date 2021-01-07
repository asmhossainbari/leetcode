# Definition for singly-linked list.
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
        if l1 is None and l2 is None:
            return None
        sum_linked_list = ListNode()
        head = sum_linked_list
        carry = 0
        while (l1 is not None) and l2 is not None:
            sum_result = carry + l1.val + l2.val
            if sum_result > 9:
                new_node = ListNode()
                new_node.val = sum_result - 10
                sum_linked_list.next = new_node
                sum_linked_list = sum_linked_list.next
                carry = 1
            else:
                new_node = ListNode()
                new_node.val = sum_result
                sum_linked_list.next = new_node
                sum_linked_list = sum_linked_list.next
                carry = 0

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum_result = carry + l1.val
            if sum_result > 9:
                new_node = ListNode()
                new_node.val = sum_result - 10
                sum_linked_list.next = new_node
                sum_linked_list = sum_linked_list.next
                carry = 1
            else:
                new_node = ListNode()
                new_node.val = sum_result
                sum_linked_list.next = new_node
                sum_linked_list = sum_linked_list.next
                carry = 0
            l1 = l1.next

        while l2 is not None:
            sum_result = carry + l2.val
            if sum_result > 9:
                new_node = ListNode()
                new_node.val = sum_result - 10
                sum_linked_list.next = new_node
                sum_linked_list = sum_linked_list.next
                carry = 1
            else:
                new_node = ListNode()
                new_node.val = sum_result
                sum_linked_list.next = new_node
                sum_linked_list = sum_linked_list.next
                carry = 0
            l2 = l2.next

        if carry == 1:
            new_node = ListNode()
            new_node.val = carry
            sum_linked_list.next = new_node
            sum_linked_list = sum_linked_list.next

        return head.next