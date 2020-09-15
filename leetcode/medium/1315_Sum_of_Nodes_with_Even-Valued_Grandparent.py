# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(root,flag1,flag2):
            '''flag1 even parent
            flag2 even grandparents
            returns sum
            '''
            if not root:
                return 0
            
            result = 0
            if flag2:
                result += root.val
                
            callflag2 = callflag1 = False
            if flag1:
                callflag2 = True # Every child has even grandpa
            if root.val % 2 == 0:
                callflag1 = True # Every child has even parent
                
            left = helper(root.left,callflag1,callflag2)
            right = helper(root.right,callflag1,callflag2)
            
            result += left + right
            #print(root.val,result)
            return result
        return helper(root,False,False)
            