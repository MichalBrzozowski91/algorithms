# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,leftflag):
        if not root:
            return 0
        result = 0
        if not root.left and not root.right: # This is a leaf
            if leftflag:
                return root.val
            else:
                return 0
        if root.right:
            result += self.helper(root.right,False)
        if root.left:
            result += self.helper(root.left,True)
        return result
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.helper(root,False)