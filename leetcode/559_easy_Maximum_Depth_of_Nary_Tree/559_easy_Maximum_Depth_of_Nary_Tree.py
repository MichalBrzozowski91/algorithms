"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: # Root is an empty tree
            return 0
        elif not root.children:
            return 1
        listOfDepths = []
        for child in root.children:
            listOfDepths.append(self.maxDepth(child))
        return 1 + max(listOfDepths)
