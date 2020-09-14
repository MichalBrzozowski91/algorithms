"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        # DFS
        nodes = [root]
        new_nodes = []
        while nodes:
            for i in range(len(nodes)):
                node = nodes[i]
                if i+1 < len(nodes):
                    next_node = nodes[i+1]
                else:
                    next_node = None
                node.next = next_node
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
            new_nodes = []
        return root
