# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive solution
    def helper(self, root): # Returns treenode and depth
        if not root:
            return None,0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left[1] > right[1]:
            return left[0], left[1] + 1
        if left[1] < right[1]:
            return right[0], right[1] + 1
        if left[1] == right[1]:
            return root, left[1] + 1
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[0]
