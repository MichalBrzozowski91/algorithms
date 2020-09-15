# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False # If a root is empty, we return False
        elif not root.left and not root.right: # Root does not have children
            return sum == root.val
        elif root.left and not root.right: # Root has only a child on the left
            return self.hasPathSum(root.left,sum - root.val)
        elif not root.left and root.right: # Root has only a child on the right
            return self.hasPathSum(root.right,sum - root.val)
        else: # Root has two children, we must check both paths
            return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)