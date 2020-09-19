# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x):
        if not head:
            return None
        left_start = None
        left_end = None
        right_start = None
        right_end = None
        node = head
        while node:
            if node.val < x:
                if not left_start:
                    left_start = left_end = node
                else:
                    left_end.next = node
                    left_end = node
            else:
                if not right_start:
                    right_start = right_end = node
                else:
                    right_end.next = node
                    right_end = right_end.next
            node = node.next
        
        # Gluying left and right
        if not left_start:
            return right_start
        elif not right_start:
            return left_start
        else:
            left_end.next = right_start
            right_end.next = None
            return left_start
