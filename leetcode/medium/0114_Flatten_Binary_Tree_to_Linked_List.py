# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = []
        node = root
        while node:
            prev = node
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                node.right = node.left
                node.left = None
            node = node.right
            if not node:
                if not stack:
                    return None
                else:
                    node = stack.pop()
                    prev.right = node
