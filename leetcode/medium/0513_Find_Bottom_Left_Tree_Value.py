# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        nodes = [root]
        result = None
        while nodes:
            newnodes = []
            result = nodes[0].val
            for node in nodes:
                if node.left:
                    newnodes.append(node.left)
                if node.right:
                    newnodes.append(node.right)
            nodes = newnodes
        return result
            
