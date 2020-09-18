# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def convertSequence(root):
            if not root:
                return []
            return convertSequence(root.left) + [root.val] + convertSequence(root.right)
        def twoSum(numbers, target):
            # Two pointer solution
            nums = numbers
            i, j = 0, len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                if s == target: # s is equal to a target:
                    return True
                elif s > target: # s is too big
                    j -= 1
                elif s < target: # s is too small
                    i += 1
            return None
        return twoSum(convertSequence(root),k)