# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTBound(self,root,minimum,maximum):
        if not root:
            return True
        #print(root.val,minimum,maximum)
        if root.val <= minimum or root.val >= maximum:
            return False
        if not self.isValidBSTBound(root.left,minimum, min(root.val,maximum)):
            return False
        if not self.isValidBSTBound(root.right,max(minimum,root.val),maximum):
            return False
        return True
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTBound(root,float('-inf'),float(inf))
