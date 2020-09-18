# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def listOfBinaryNumbers(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            resultList =[]
            for p in listOfBinaryNumbers(root.left):
                resultList.append(str(root.val) + p)
            for p in listOfBinaryNumbers(root.right):
                resultList.append(str(root.val) + p)
            return resultList
        currentSum = 0
        for element in listOfBinaryNumbers(root):
            currentSum += int(element,2)
        return currentSum