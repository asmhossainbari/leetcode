# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case
        if head is None or head.next is None:
            return head

        # odd even list
        odd_list = head
        even_list = head.next

        cur_odd = odd_list
        cur_even = even_list

        while cur_odd.next is not None and cur_even.next is not None:
            cur_odd.next = cur_even.next
            cur_odd = cur_odd.next

            cur_even.next = cur_odd.next
            cur_even = cur_even.next

        cur_odd.next = even_list
        return odd_list