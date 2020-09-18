# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p,q):
        # Special cases
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Pre-order traversal
        if not t: # t is None
            return True
        if not s: # s is empty
            return False
        
        # We visit s and check if s and t are the same
        #print('Visiting',s.val)
        if s.val == t.val and self.isSameTree(s,t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
            