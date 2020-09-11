# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # O(n) space O(1) time solution
        # Checking edge cases
        if not head or not head.next:
            return
        #if not head.next.next:
        #    return
        
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
        
        # Changing a linked list in-place
        Node1 = head
        Node2 = center.next
        prev1 = None
        prev2 = None

        while Node1 != center: 
            prev1 = Node1
            prev2 = Node2
            Node1 = Node1.next
            prev1.next = Node2
            Node2 = Node2.next
            prev2.next = Node1

        if Node2 != center: # We are at the center
            Node1.next = Node2
            return
        else:
            Node1.next = None
            return
                

        
