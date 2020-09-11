"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        nodes = [root]
        while nodes:
            level_nodes =[]
            new_nodes = []
            for node in nodes:
                level_nodes.append(node.val)
                new_nodes += node.children
            result.append(level_nodes)
            nodes = new_nodes
        return result
                
