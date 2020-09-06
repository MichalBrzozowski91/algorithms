# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pointer1 = head
        pointer2 = head
        for _ in range(n):
            pointer2 = pointer2.next
        if not pointer2: # We remove the first node
            return head.next
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        pointer1.next = pointer1.next.next # We remove a node
        return head
