# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        elif root.val in range(L,R + 1):
            return TreeNode(root.val,self.trimBST(root.left,L,R),self.trimBST(root.right,L,R))
        elif root.val < L: # We trim the whole left branch
            return self.trimBST(root.right,L,R)
        elif root.val > R: # We trim the whole right branch
            return self.trimBST(root.left,L,R)