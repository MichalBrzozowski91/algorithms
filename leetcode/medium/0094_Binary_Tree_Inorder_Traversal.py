# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative solution with a stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [('tree',root)]
        while stack:
            a = stack.pop()
            if a[0] == 'write it':
                result.append(a[1])
            elif a[0] == 'tree':
                if a[1].right:
                    stack.append(('tree',a[1].right))
                stack.append(('write it',a[1].val))
                if a[1].left:
                    stack.append(('tree',a[1].left))
            #print(stack)
        return result
