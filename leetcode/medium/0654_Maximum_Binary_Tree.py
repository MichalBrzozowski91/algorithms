# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: # Empty list
            return None
        
        m = max(nums)
        index = nums.index(m)
        left = self.constructMaximumBinaryTree(nums[:index])
        right = self.constructMaximumBinaryTree(nums[index+1:])
        return TreeNode(m,left,right)
