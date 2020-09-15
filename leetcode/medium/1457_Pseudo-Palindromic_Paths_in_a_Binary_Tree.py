# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isPalindrome(self,boolean_list):
        #print('Checking boolean_list',boolean_list)
        return sum(boolean_list) <= 1
    
    def helper(self,root,boolean_list):
        if not root:
            return 0
        result_list = boolean_list.copy()
        result_list[root.val] = 1 - result_list[root.val]
        #print('Visiting',root.val,'current list is',result_list)
        if not root.left and not root.right: # This is a leaf
            return self.isPalindrome(result_list)
        else:
            left = self.helper(root.left,result_list)
            right = self.helper(root.right,result_list)
            return left + right
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return int(self.helper(root,[0]*10))