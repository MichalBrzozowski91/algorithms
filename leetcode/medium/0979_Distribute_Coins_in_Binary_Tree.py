# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoinsAndCount(self,root):
        if not root:
            return [0,0]
        left = self.distributeCoinsAndCount(root.left)
        right = self.distributeCoinsAndCount(root.right)
        result = root.val + left[0] + right[0] - 1
        return [result,abs(result) + left[1] + right[1]]
    def distributeCoins(self, root: TreeNode) -> int:
        return self.distributeCoinsAndCount(root)[1]