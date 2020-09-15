# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # We use the fact that the tree has distinct value
    def helper(self,root, del_set): #Returns a forrest and a boolean which means there is a last tree in a forrest
        if not root:
            return [[],False]
        #print('Visiting',root.val,'del set',del_set)
        if not del_set:
            return [[root],True] # There is nothing to delete
        if root.val in del_set:
            del_set.remove(root.val)
            left = self.helper(root.left,del_set)
            right = self.helper(root.right,del_set)
            return [left[0] + right[0],False]
        
        left = self.helper(root.left,del_set)
        right = self.helper(root.right,del_set)
        #print('Root:',root.val,'left and right checked','LEFT:',left,'RIGHT',right)
        
        
        if not left[1] and not right[1]:
            result = left[0] + right[0] +[TreeNode(root.val)]
            return [result,True]
        if not right[1] and left[1]: # Right forrest is empty
            result = right[0] + left[0][:-1] + [TreeNode(root.val,left[0][-1])]
            return [result, True]
        if not left[1] and right[1]: # Left forrest is empty
            result = left[0] + right[0][:-1] + [TreeNode(root.val,None,right[0][-1])]
            return [result, True]
        if left[1] and right[1]: # We glue last trees in two forrests
            result = left[0][:-1] + right[0][:-1] + [TreeNode(root.val,left[0][-1],right[0][-1])]
            return [result,True]
        
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        return self.helper(root, set(to_delete))[0]