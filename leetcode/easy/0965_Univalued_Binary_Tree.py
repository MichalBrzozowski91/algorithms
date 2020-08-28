# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        elif root.left and not root.right:
            return root.val == root.left.val and self.isUnivalTree(root.left)
        elif not root.left and root.right:
            return root.val == root.right.val and self.isUnivalTree(root.right)
        else:
            return root.val == root.left.val and self.isUnivalTree(root.left) and root.val == root.right.val and self.isUnivalTree(root.right)
