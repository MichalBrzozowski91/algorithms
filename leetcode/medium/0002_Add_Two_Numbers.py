# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1.val
        b = l2.val
        sum_ = a + b
        digit = sum_ % 10
        result = ListNode(digit)
        pointer = result
        remainder = int((sum_ - digit)/10)
        node1 = l1.next
        node2 = l2.next
        while node1 or node2 or remainder != 0:
            if node1:
                a = node1.val
            else:
                a = 0
            if node2:
                b = node2.val
            else:
                b = 0
            sum_ = a + b + remainder
            digit = sum_ % 10
            pointer.next = ListNode(digit)
            pointer = pointer.next
            remainder = int((sum_ - digit)/10)
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        return result
