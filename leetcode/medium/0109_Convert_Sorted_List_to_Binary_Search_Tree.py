# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            return TreeNode(head.val,None,TreeNode(head.next.val))
        # Find a half of a linked list
        a = head
        b = head.next
        aprev = None
        while b and b.next:
            aprev = a
            a = a.next
            b = b.next.next
        middle = a
        if aprev:
            aprev.next = None
        return TreeNode(middle.val,self.sortedListToBST(head),self.sortedListToBST(middle.next))
