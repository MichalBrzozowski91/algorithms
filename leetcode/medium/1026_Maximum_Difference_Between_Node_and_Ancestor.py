# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root): # Returns best value, min and max
        #print('visiting',root.val)
        result_val = 0
        result_max = root.val
        result_min = root.val
        
        if root.left:
            left = self.helper(root.left)
            result_val = max(result_val,left[0],abs(root.val-left[1]),abs(root.val-left[2]))
            result_min = min(result_min,left[1])
            result_max = max(result_max,left[2])
        if root.right:
            right = self.helper(root.right)
            result_val = max(result_val,right[0],abs(root.val-right[1]),abs(root.val-right[2]))
            result_min = min(result_min,right[1])
            result_max = max(result_max,right[2])
        #print('visited',root.val,'result:',result_val,result_max,result_min)
        return result_val,result_min,result_max
            
            
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.helper(root)[0]