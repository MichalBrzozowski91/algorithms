# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) space O(1) time solution
        # Checking edge cases
        if not head or not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False
        
        # Finding a half of a linked list by slow and fast pointer
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        center = slow
        #print(center)
        
        # Reverse second half of a linked list in-place
        slow = slow.next
        prev = None
        while slow:
            temp = slow # This variable refers to the same object as slow
            slow = slow.next # Now the variable slow refers to the next object
            temp.next = prev # We change the link in the previous slow
            prev = temp
        center.next = prev
        
        #print(head)
        # Checking if this is a palindrom by comparing left and right half of the linked list
        Node1 = head
        Node2 = center.next
        while Node1 and Node2:
            if Node1.val != Node2.val:
                return None
            else:
                Node1 = Node1.next
                Node2 = Node2.next
        return True
        
        