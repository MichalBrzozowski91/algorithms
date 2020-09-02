# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative solution
        if not root:
            return []
        result = []
        deq = deque([root])
        while deq:
            print(deq)
            element = deq.pop()
            result.append(element.val)
            if element.right:
                deq.append(element.right)
            if element.left:
                deq.append(element.left)
        return result
        
