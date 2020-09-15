# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # O(1) memory solution
        if not head or not head.next:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while slow_pointer != fast_pointer:
            if slow_pointer and fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            else:
                return False
        return True
        