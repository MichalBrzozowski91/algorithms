# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lCEandPQflags(root,p,q):
            '''The function returns P Q flags and LCE'''
            result = [False,False,None]
            # Post-order traversal
            # Go left
            if root.left:
                
                search_result = lCEandPQflags(root.left,p,q)
                if search_result[2]:
                    return search_result
                elif search_result[0]:
                    result[0] = True
                elif search_result[1]:
                    result[1] = True

            # Go right
            if root.right:
                search_result = lCEandPQflags(root.right,p,q)

                if search_result[2]:
                    return search_result
                elif search_result[0]:
                    result[0] = True
                elif search_result[1]:
                    result[1] = True

            

            if root.val == p.val:
                result[0] = True
            elif root.val == q.val:
                result[1] = True
                
            if result[0] and result[1]:
                result[2] = TreeNode(root.val)

            #print('Visiting a node',root.val,'Flags are',result)
                
            return result
        #print(lCEandPQflags(root,p,q))
        return lCEandPQflags(root,p,q)[2]
