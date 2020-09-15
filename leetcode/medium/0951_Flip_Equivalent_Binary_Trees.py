# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: #There are both empty
            return True
        if not root1 or not root2: #One is empty
            return False
        if root1.val != root2.val: # Different root value
            return False
        if root1.left and root2.left and root1.left.val == root2.left.val and root1.right and root2.right and root1.right.val == root2.right.val:
            if self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right):
                return True 
        if root1.left and root2.left and root1.left.val == root2.left.val and root1.right and root2.right and root1.right.val == root2.right.val:
        compareLeftRight = self.flipEquiv(root1.left,root2.right)
        compareRightLeft = self.flipEquiv(root1.right,root2.left)
        return (compareLeftLeft and compareRightRight) or (compareLeftRight and compareRightLeft)
            