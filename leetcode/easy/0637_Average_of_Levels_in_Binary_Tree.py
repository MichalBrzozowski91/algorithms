# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def sumNumber(list1,list2):
            l1 = len(list1)
            l2 = len(list2)
            m = max(l1,l2)
            result=[[0,0] for i in range(m)]
            for i in range(l1):
                result[i][0] += list1[i][0] # Sum increment
                result[i][1] += list1[i][1] # Number increment
            for i in range(l2):
                result[i][0] += list2[i][0] # Sum increment
                result[i][1] += list2[i][1] # Number increment
            return result

    
        def sumNumberOfLevels(root):
            if not root:
                return []
            else:
                return [[root.val,1]]+sumNumber(sumNumberOfLevels(root.left),sumNumberOfLevels(root.right))
        
        result = []
        for element in sumNumberOfLevels(root):
            result.append(element[0]/element[1])
        return result
                                                  