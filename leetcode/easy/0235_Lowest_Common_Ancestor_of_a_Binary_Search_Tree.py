# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #print(p,q)
        #print(p.val)
        #print(q.val)
        a = min(p.val,q.val)
        b = max(p.val,q.val)
        if root.val in range(a,b+1): # Then p is in the left subtree, q in the right, therefore LCE is equal to root.val
            return TreeNode(root.val)
        elif root.val < a: # Then p and q are in the right subtree
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > b: # Then p and q are in the left subtree
            return self.lowestCommonAncestor(root.left,p,q)