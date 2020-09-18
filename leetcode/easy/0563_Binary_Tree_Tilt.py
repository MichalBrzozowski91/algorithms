# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def findTiltAndSum(root):
            '''Function returns a pair [tilt,sum of all nodes,sum of tilts]'''
            if not root:
                return [0,0,0]
            left_path = findTiltAndSum(root.left)
            right_path = findTiltAndSum(root.right)
            new_tilt = abs(left_path[1]-right_path[1])
            return [new_tilt,root.val + left_path[1] + right_path[1],new_tilt + left_path[2]+right_path[2]]
        return findTiltAndSum(root)[2]