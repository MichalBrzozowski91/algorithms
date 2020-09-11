# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # Calculate length
        N = 0
        node = head
        while node:
            last = node
            N += 1
            node = node.next
        k = k % N # Rotation integer should be in range(N)
        if k == 0: # Rotation is an identity
            return head
        # Create two pointers separated by k
        a = head
        b = head
        for _ in range(k):
            b = b.next
        # Move the pointers to the end
        while b:
            prev = a
            a,b = a.next,b.next
        # Node a is our new start
        start = a
        prev.next = None
        last.next = head
        return start
