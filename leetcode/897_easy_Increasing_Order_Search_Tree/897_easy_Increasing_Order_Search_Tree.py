# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrderList(root):
            if root == None:
                return []
            return inOrderList(root.left) + [root.val] + inOrderList(root.right)
        def treeFromList(deq):
            if deq == deque([]):
                return None
            a = deq.popleft()
            return TreeNode(a,None,treeFromList(deq))
        deq = deque(inOrderList(root))
        return treeFromList(deq)
