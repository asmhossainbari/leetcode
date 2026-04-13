# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # Time: O(n + m)
    # Space: O(n + m) because it creates a new merged list
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1
        if list1 is None and list2 is None:
            return list1
        merged_list = ListNode(0)
        result = merged_list

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next
            merged_list = merged_list.next
        while list1 is not None:
            merged_list.next = ListNode(list1.val)
            list1 = list1.next
            merged_list = merged_list.next
        while list2 is not None:
            merged_list.next = ListNode(list2.val)
            list2 = list2.next
            merged_list = merged_list.next
        return result.next

    # Time: O(n + m)
    # Space: O(1) extra space because it reuses existing nodes
    def mergeTwoListsOptimized(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node avoids special handling for the first merged node.
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 is not None else list2
        return dummy.next
