# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def longestRootUnivaluePath(root):
            if not root:
                return [0,0]
            result = [0,0] # First index is the longest path from root to leaf, second is just the longest path
            left = longestRootUnivaluePath(root.left)
            right = longestRootUnivaluePath(root.right)
            
            if root.left and root.right:
                result[0] = max(1 + left[0],1 + right[0])
                result[1] = max(2 + left[0] + right[0],left[1],right[1])
            elif root.left:
                #print(root.left,longestRootUnivaluePath(root.left))
                result[0] = 1 + left[0]
                result[1] = max(1+left[0],left[1],right[1])
            elif root.right:
                result[0] = 1 + right[0]
                result[1] = max(1 + right[0],left[1],right[1])
            else:
                result[0] = 0
                result[1] = max(left[1],right[1])
            #print(root,result)
            return result
                
        result = longestRootUnivaluePath(root)
        return result[1]