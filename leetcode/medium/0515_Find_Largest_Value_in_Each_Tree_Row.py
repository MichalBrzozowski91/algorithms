# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # Deep first search
        if not root:
            return []
        nodes = [root]
        result = []
        while nodes:
            newnodes =[]
            currentmax = float('-inf')
            for node in nodes:
                currentmax = max(currentmax,node.val)
                if node.left:
                    newnodes.append(node.left)
                if node.right:
                    newnodes.append(node.right)
            result.append(currentmax)
            nodes = newnodes
        return result
