# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and not t2:
            return t1
        elif not t1 and t2:
            return t2
        elif not t1 and not t2:
            return None
        else:
            resultTree = TreeNode(t1.val+t2.val,self.mergeTrees(t1.left,t2.left),self.mergeTrees(t1.right,t2.right))
            return resultTree
