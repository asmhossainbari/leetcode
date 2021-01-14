# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head is None:
            return []
        if head.next is None:
            return [0]

        arr_list = []
        current_node = head
        while current_node is not None:
            arr_list.append(current_node.val)
            current_node = current_node.next
        return self.nextGreaterElement(arr=arr_list)

    def nextGreaterElement(self, arr):
        """
        :type arr: List[int]
        :rtype List[int]
        """
        next_greater_list = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while len(stack) > 0 and arr[stack[-1]] < arr[i]:
                next_greater_list[stack.pop()] = arr[i]
            stack.append(i)
        return next_greater_list


sol = Solution()
print(sol.nextGreaterElement(arr=[2,1,5]))
print(sol.nextGreaterElement(arr=[2,7,4,3,5]))
print(sol.nextGreaterElement(arr=[1,7,5,1,9,2,5,1]))