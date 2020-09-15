# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
from itertools import groupby

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def listOfNodes(root):
            if not root:
                return []
            left = listOfNodes(root.left)
            right = listOfNodes(root.right)
            return [root.val] + left + right
        if not root:
            return []
        list_final = listOfNodes(root)
        # group most_common output by frequency
        freqs = groupby(Counter(list_final).most_common(), lambda x:x[1])
        # pick off the first group (highest frequency)
        return ([val for val,count in next(freqs)[1]])
        