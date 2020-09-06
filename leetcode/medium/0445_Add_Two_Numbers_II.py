# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNumber(self,l1):
        if not l1:
            return ''
        return str(l1.val) + self.getNumber(l1.next)
    def createList(self,number):
        digit = str(number)[0]
        result = ListNode(digit)
        node = result
        for digit in str(number)[1:]:
            node.next = ListNode(int(digit))
            node = node.next
        return result
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.createList(int(self.getNumber(l1))+int(self.getNumber(l2)))
