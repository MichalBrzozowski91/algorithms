# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # Global variables
        self.minimum = float('inf') 
        self.previous = None
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return None
        if root.left:
            self.getMinimumDifference(root.left)
            
        if self.previous == None:
            self.previous = root.val
        else:
            self.minimum = min(self.minimum,root.val - self.previous)
            self.previous = root.val
        #print(self.previous,root.val)
            
        if root.right:
            self.getMinimumDifference(root.right)
        return self.minimum
    def minDiffInBST(self, root: TreeNode) -> int:
        return self.getMinimumDifference(root)