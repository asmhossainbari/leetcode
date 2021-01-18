# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if k == 0:
            return head
        temp = head
        list_len = 0
        while temp is not None:
            temp = temp.next
            list_len += 1

        k = k % list_len
        if k <= 0:
            return head

        tail_list_head = head
        for step in range(list_len - k - 1):
            tail_list_head = tail_list_head.next

        front_list_head = tail_list_head.next
        result_head = front_list_head
        tail_list_head.next = None

        while front_list_head.next is not None:
            front_list_head = front_list_head.next
        front_list_head.next = head
        return result_head