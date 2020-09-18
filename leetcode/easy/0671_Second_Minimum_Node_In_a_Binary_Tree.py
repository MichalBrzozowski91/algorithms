# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        if not root.left and not root.right:
            return -1
        if root.left.val == root.val:
            left = self.findSecondMinimumValue(root.left)
        else:
            left = root.left.val
        if root.right.val == root.val:
            right = self.findSecondMinimumValue(root.right)
        else:
            right = root.right.val
        if left == -1:
            return right
        elif right == -1:
            return left
        else:
            return min(left,right)