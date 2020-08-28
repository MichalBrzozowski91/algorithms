"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        if root.children == []: # Root has no children, we visit it
            return [root.val]
        temporary_list = []
        for child in root.children:
            temporary_list += self.postorder(child)
        return temporary_list + [root.val]
