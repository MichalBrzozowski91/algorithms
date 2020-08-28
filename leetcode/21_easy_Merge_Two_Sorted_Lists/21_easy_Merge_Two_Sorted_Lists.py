# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        last = None
        while l1 or l2:
            if not l1:
                new_element = l2.val
                l2 = l2.next
            elif not l2 or l1.val <= l2.val:
                new_element = l1.val
                l1 = l1.next
            elif not l1 or l2.val <= l1.val:
                new_element = l2.val
                l2 = l2.next
            if not result:
                result = ListNode(new_element)
                last = result
            else:
                last.next = ListNode(new_element)
                last = last.next
        return result
