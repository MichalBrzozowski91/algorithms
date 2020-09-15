# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodesBound(self,root,upperbound):
        if not root:
            return 0
        #print('Visiting',root.val,'with the upperbound',upperbound)
        # Pre order traversal
        # Visit the root first
        if root.val < upperbound:
            left = self.goodNodesBound(root.left,upperbound)
            right = self.goodNodesBound(root.right,upperbound)
            return left + right
        else:
            left = self.goodNodesBound(root.left,root.val)
            right = self.goodNodesBound(root.right,root.val)
            return 1 + left + right
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesBound(root,float(-inf))