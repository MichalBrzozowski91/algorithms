# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def pointwiseList(list1,list2):
            result = []
            if len(list1) >= len(list2):
                result = list1
                for i in range(1,len(list2)+1):
                    result[-i] = result[-i] + list2[-i]
            else:
                result = list2
                for i in range(1,len(list1)+1):
                    result[-i] = list1[-i] + result[-i]
            return result
        if not root:
            return []
        a = \
            pointwiseList(self.levelOrderBottom(root.left),self.levelOrderBottom(root.right))+[[root.val]]
        #print(a)
        return a
