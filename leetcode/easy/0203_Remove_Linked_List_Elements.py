# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Without recursion - in-place solution 
        if not head:
            return None
        if not head.next:
            if head.val == val:
                return None
            else:
                return head
        node = head
        prev = None
        while node.next:
            if node.val == val: # We remove a node in-place - we change a linked-list structure
                node.val = node.next.val
                node.next = node.next.next
            else:
                prev = node # We remember posiion of the last not forbidden value in the list
                node = node.next # We just move a pointer
        
        # We check the last node separately
        if not prev and not head.next:
            if head.val == val:
                return None
            else:
                return head
        if node.val == val:
            prev.next = None
        return head
