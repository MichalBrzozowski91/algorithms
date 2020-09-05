# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        '''
        Return in-order traversal of a binary tree
        For a BST this has an ascending order
        '''
        if not root:
            return []
        left = self.inOrder(root.left)
        right = self.inOrder(root.right)
        return left + [root.val] + right
    def minSequence(self, list1, list2):
        result = []
        i = 0
        j = 0
        while i < len(list1) or j < len(list2):
            if j >= len(list2) or (i < len(list1) and list1[i] <= list2[j]):
                result.append(list1[i])
                i += 1
            elif i >= len(list1) or (j < len(list2) and list2[j] <= list1[i]):
                result.append(list2[j])
                j += 1
        return result
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.inOrder(root1)
        print(list1)
        list2 = self.inOrder(root2)
        print(list2)
        return self.minSequence(list1,list2)
