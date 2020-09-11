# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def pointwiseList(list1,list2):
            result = []
            if len(list1) >= len(list2):
                result = list1
                for i in range(0,len(list2)):
                    result[i] = result[i] + list2[i]
            else:
                result = list2
                for i in range(0,len(list1)):
                    result[i] = list1[i] + result[i]
            return result
        if not root:
            return []
        a = \
            [[root.val]] + pointwiseList(self.levelOrder(root.left),self.levelOrder(root.right))
        #print(a)
        return a
