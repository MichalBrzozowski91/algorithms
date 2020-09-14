# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        '''This function returns [max gain with no conditions, max gain if parent node was robbed]'''
        if not root:
            return 0, 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        return max(left[0] + right[0], root.val + left[1] + right[1]), left[0] + right[0]
        
    def rob(self, root: TreeNode) -> int:
        return self.helper(root)[0]
