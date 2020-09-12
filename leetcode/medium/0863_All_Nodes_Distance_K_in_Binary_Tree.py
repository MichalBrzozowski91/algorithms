# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        #print('Call of the function with pre:',pre,'post:',post)
        if not pre:
             return None # Empty tree
        if pre == post:
            return TreeNode(pre[0]) # One node tree
        
        result = TreeNode(pre[0]) # or post[-1]
        if pre[1] == post[-2]:
            result.left = self.constructFromPrePost(pre[1:],post[:-1])
            return result
        else:
            preindex = pre.index(post[-2])
            left_pre = pre[1:preindex] # Preorder traversal of the left subtree
            right_pre = pre[preindex:] # Preorder traversal of the right subtree
            postindex = post.index(pre[1])
            left_post = post[:postindex+1] # Postorder traversal of the left subtree
            right_post = post[postindex+1:-1] # Postorder traversal of the right subtree
            
            result.left = self.constructFromPrePost(left_pre,left_post)
            result.right = self.constructFromPrePost(right_pre,right_post)
            return result
