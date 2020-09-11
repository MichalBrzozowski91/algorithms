# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.global_list = []
    def pathSumList(self,root,sum,ancestors,total_path_sum):
        if not root:
            return None
        new_total = total_path_sum + root.val
        new_ancestors = ancestors + [root.val]
        #print(root.val,new_ancestors,new_total)
        if root.left:
            self.pathSumList(root.left,sum,new_ancestors,new_total)
        if root.right:
            self.pathSumList(root.right,sum,new_ancestors,new_total)
        if not root.left and not root.right and new_total == sum:
            self.global_list.append(new_ancestors)
            
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.pathSumList(root,sum,[],0)
        return self.global_list
