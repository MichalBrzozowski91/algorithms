# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self,head,blocked):
        if not head: # No duplicates in an empty list
            return head
        if head.val == blocked:
            return self.helper(head.next,blocked)
        if not head.next: # No duplicates in a 1-element only list
            return head 
        if head.val == head.next.val:
            return self.helper(head.next,head.val)
        else: # head.val is a new value
            return ListNode(head.val,self.helper(head.next,None))
            
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return self.helper(head,None)
