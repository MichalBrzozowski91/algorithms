# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxVal(self,root):
        '''Returns a node with the largest value in a given BST'''
        if not root:
            return None
        if not root.right:
            return root
        return self.maxVal(root.right)
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: # key is not in a tree
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right # A found node with a given key does not have left children, so we just change it t root.right3
            if not root.right:
                return root.left 
            maxNode = self.maxVal(root.left)
            maxNode.right = root.right
            return root.left
        if key > root.val:
            toDelete = self.deleteNode(root.right, key)
            root.right = toDelete
            return root
        if key < root.val:
            toDelete = self.deleteNode(root.left, key)
            root.left = toDelete
            return root
