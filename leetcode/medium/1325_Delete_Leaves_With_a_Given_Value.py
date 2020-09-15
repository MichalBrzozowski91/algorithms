# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        # Post order traversal
        left = self.removeLeafNodes(root.left,target)
        right = self.removeLeafNodes(root.right,target)
        if root.val == target and not left and not right: # We cut down the entire tree
            return None
        else:
            return TreeNode(root.val,left,right) # Reconstruction of a tree
            