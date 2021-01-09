# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        sorted_list = ListNode()
        head = sorted_list
        while l1 and l2:
            if l1.val <= l2.val:
                sorted_list.next = l1
                l1 = l1.next
            else:
                sorted_list.next = l2
                l2 = l2.next
            sorted_list = sorted_list.next

        while l1:
            sorted_list.next = l1
            sorted_list = sorted_list.next
            l1 = l1.next

        while l2:
            sorted_list.next = l2
            sorted_list = sorted_list.next
            l2 = l2.next
        return head.next



