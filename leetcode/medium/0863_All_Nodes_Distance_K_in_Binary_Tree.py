# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def helper(self,root,L):
        '''Return all values of nodes at the depth L (in other words with distance L from the root)'''
        if not root:
            return []
        if L == 0:
            return [root.val]
        left = self.helper(root.left,L - 1)
        right = self.helper(root.right, L - 1)
        return left + right
    
    def finder(self,root,target):
        '''Finds a given node and returns a path to it'''
        if not root:
            return []
        if root.val == target.val:
            return [[root,None]]
        left = self.finder(root.left,target)
        right = self.finder(root.right,target)
        if left != []:
            return [[root,'left']] + left
        if right != []:
            return [[root,'right']] + right
        return []
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []
        # We search a tree iteratively with an in-order traversal
        finder = self.finder(root,target) 
        finder.reverse()
        result = []
        for i in range(len(finder)):
            if K - i < 0:
                return result
            node = finder[i][0]
            # Eliminate a child
            if finder[i][1] == 'left':
                node.left = None
            if finder[i][1] == 'right':
                node.right = None
            result += self.helper(node, K - i)
        return result
