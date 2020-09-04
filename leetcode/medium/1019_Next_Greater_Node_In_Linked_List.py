# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        vals = []
        stack = deque([])
        result = []
        # Create a list
        node = head
        j = 0 # index
        while node:
            vals.append(node.val)
            result.append(0)
            while stack:
                last = stack.pop()
                if node.val > vals[last]:
                    result[last] = node.val
                else:
                    stack.append(last)
                    break
            stack.append(j)
            node = node.next
            j += 1
        return result
            
            
            
