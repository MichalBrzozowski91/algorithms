# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val >= root.val:
            return TreeNode(val,root)
        else:
            return TreeNode(root.val,root.left,self.insertIntoMaxTree(root.right,val))