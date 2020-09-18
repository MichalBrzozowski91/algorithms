# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def levelAndParentOfx(root,parent,x): # The outcome of this functions is a list (level of x, parent of x)
            result = [None, None]
            if not root:
                return result
            if root.val == x: # We found x
                result[0] = 1
                result[1] = parent
            else:
                result_left = levelAndParentOfx(root.left,root.val,x)
                result_right = levelAndParentOfx(root.right,root.val,x)
                if result_left[0]: # x was found on the left branch
                    result[0] = 1 + result_left[0]
                    result[1] = result_left[1]
                if result_right[0]: # x was found on the right branch
                    #print(not result_right[0])
                    result[0] = 1 + result_right[0]
                    result[1] = result_right[1]
            print('Visited',root.val,'with a parent',parent,'searching for',x)
            print('Result is',result)
            return result
            print(levelAndParentOfx(root,None,x))
        x_search_result = levelAndParentOfx(root,None,x)
        y_search_result = levelAndParentOfx(root,None,y)
        return x_search_result[0] == y_search_result[0] and not x_search_result[1] == y_search_result[1]