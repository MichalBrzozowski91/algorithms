# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # Create a hashset from G
        hashset = set()
        counter = 0
        for g in G:
            hashset.add(g)
            counter += 1
        
        node = head
        while node and node.next:
            if node.val in hashset and node.next.val in hashset:
                counter -= 1
            node = node.next
        return counter
