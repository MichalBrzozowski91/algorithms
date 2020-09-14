"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(1) space complexity solution
class Solution:
    def connect(self, root):
        if not root:
            return root
        start_above = root
        pointer_above = start_above
        # Start of a new level
        while start_above.left:
            pointer_above = start_above
            prev_right = None
            while pointer_above:
                node_left = pointer_above.left
                node_right = pointer_above.right
                if prev_right:
                    prev_right.next = node_left
                node_left.next = node_right
                prev_right = node_right
                pointer_above = pointer_above.next
            start_above = start_above.left
        return root
