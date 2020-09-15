# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: # Empty tree
            return 0
        elif not root.left and not root.right: # Root does not have children
            return 1
        elif root.left and not root.right: # Root has only a child on the left
            return 1 + self.minDepth(root.left)
        elif not root.left and root.right: # Root has only a child on the right
            return 1 + self.minDepth(root.right)
        else: # Root has two children, we choose a smaller value
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))