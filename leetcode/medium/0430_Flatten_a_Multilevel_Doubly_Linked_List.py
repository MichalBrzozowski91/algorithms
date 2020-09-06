"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        #seen = set()
        stack = []
        node = head
        while node:
            prev = node
            if node.child:
                if node.next:
                    stack.append(node.next)
                node.next = node.child
                node.child.prev = node
                node.child = None
            node = node.next
            if not node:
                if not stack:
                    return head
                else:
                    node = stack.pop()
                    prev.next = node
                    node.prev = prev
