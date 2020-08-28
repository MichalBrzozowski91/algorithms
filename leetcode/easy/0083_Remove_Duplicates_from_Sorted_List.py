# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head # Node is a variable which denotes currently considered  node
        if not node:
            return None
        while node.next: # This is not the last node
            #print(node.val)
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
                
