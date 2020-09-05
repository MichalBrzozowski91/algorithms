# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        node = head
        odd = node
        node = node.next
        second_node = node
        even = node
        node = node.next
        odd_flag = True
        while node:
            if odd_flag:
                odd.next = node
                odd = node
                odd_flag = False
            else:
                even.next = node
                even = node
                odd_flag = True
            node = node.next
        even.next = None
        odd.next = second_node
        return head
            
