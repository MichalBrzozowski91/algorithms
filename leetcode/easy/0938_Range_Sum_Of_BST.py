# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        elif root.val in range(L,R+1):
            return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
        elif root.val < L : # We look only on the right branch
            return self.rangeSumBST(root.right,L,R)
        else:
            return self.rangeSumBST(root.left,L,R)