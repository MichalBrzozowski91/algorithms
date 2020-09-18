# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        resultlist = []
        while True:
            if not head:
                l = len(resultlist)
                half = l // 2
                return resultlist[half]
            else:
                resultlist.append(head)
                head = head.next
            