# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # We get the lenght of lists A and B:
        lengthA = 0
        node = headA
        while node:
            lengthA += 1
            node = node.next
        
        lengthB = 0
        node = headB
        while node:
            lengthB += 1
            node = node.next
        
        # We go to the start of both linked lists
        nodeA = headA
        nodeB = headB
        k = lengthA - lengthB
        if k >= 0: # List A is longer
            for i in range(k):
                if nodeA:
                    nodeA = nodeA.next
                else:
                    return None
        else: # List B is longer
            for i in range(-k):
                if nodeB:
                    nodeB = nodeB.next
                else:
                    return None
                
        # We do a final chect (last with the last and so on)
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
        return None
            