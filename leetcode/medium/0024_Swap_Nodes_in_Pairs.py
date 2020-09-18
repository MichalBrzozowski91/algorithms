# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        prev = None
        node = head
        head = head.next # Change the starting point
        while node and node.next:
            print(node.val)
            # Do a swap
            node2 = node.next
            node.next, node2.next = node2.next, node
            if prev:
                prev.next = node2
            prev = node
            # Move a pointer by two places
            node = node.next
        return head
            