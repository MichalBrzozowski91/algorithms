# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def combineTreeList(self,list1,list2):
        result = []
        if not list1 or not list2:
            return []
        for tree1 in list1:
            for tree2 in list2:
                result.append(TreeNode(0,tree1,tree2))
        return result
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        list_of_trees = [[],[TreeNode(0)],[]] + [[]]*(N-2)
        for i in range(3,N+1):
            list_of_trees[i] = []
            if i % 2 == 0:
                continue
            for k in range(1,i-1):
                list_of_trees[i]+= self.combineTreeList(list_of_trees[k],list_of_trees[i-k-1])
                #print(i,list_of_trees[i])
        #print('aaaa',self.combineTreeList([TreeNode(0)],[TreeNode(0)]))
        return list_of_trees[N]