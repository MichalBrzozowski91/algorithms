# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
        # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        if not root:
            return True
        p = root.left
        q = root.right
        deq = deque([p,q])
        while deq:
            p = deq.popleft()
            q = deq.pop()
            if not check(p, q):
                return False
            
            if p and q:
                deq.appendleft(p.right)
                deq.appendleft(p.left)
                deq.append(q.left)
                deq.append(q.right)
        return True
        
        