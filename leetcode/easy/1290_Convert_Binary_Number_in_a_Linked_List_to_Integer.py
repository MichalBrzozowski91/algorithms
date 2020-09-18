# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self,head):
        if not head:
            return 0,0
        result_next = self.helper(head.next)
        return result_next[0] + head.val*2**result_next[1], result_next[1] + 1 
    def getDecimalValue(self, head: ListNode) -> int:
        return self.helper(head)[0]
        