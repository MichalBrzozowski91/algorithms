# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalancedAndDepth(root):
            '''Return is balanced and depth of a given tree'''
            if not root:
                return [True,0]
            
            # Pre-order traversal
            left_result = isBalancedAndDepth(root.left)
            right_result = isBalancedAndDepth(root.right)
            
            result = [False,0]
            result[0] = left_result[0] and right_result[0] and abs(left_result[1] - right_result[1]) <= 1
            result[1] = 1 + max(left_result[1],right_result[1])
            #print(root.val, result)
            return result
        return isBalancedAndDepth(root)[0]