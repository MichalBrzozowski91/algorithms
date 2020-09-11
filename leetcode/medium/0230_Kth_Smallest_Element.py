# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def sortedElements(root):
            if not root:
                return []
            left = sortedElements(root.left)
            right = sortedElements(root.right)
            result = left
            if left and root.val != left[-1]:
                result += [root.val]
            elif not left:
                result = [root.val]
            if right and result[-1] != right[0]:
                result += right
            elif right and result[-1] == right[0]:
                result += right[1:]
            #print(root.val,result)
            return result
        result = sortedElements(root)
        return result[k-1]
