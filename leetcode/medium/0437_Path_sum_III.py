# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Use of a hashmap
    def __init__(self):
        self.global_counter = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def pathSumAncestorList(root,sum,cumulative_total,cumulative_hashmap):
            '''Returns (number of paths with sum, number of paths from root with sum)'''
            if not root:
                return None
            #print(root.val,cumulative_total,cumulative_hashmap)
            
            total_path_sum = root.val + cumulative_total
            residual = total_path_sum - sum
            
            if str(residual) in cumulative_hashmap:
                self.global_counter += cumulative_hashmap[str(residual)]
            result_hashmap = cumulative_hashmap.copy()
            if str(total_path_sum) in result_hashmap:
                result_hashmap[str(total_path_sum)] += 1
            else:
                result_hashmap[str(total_path_sum)] = 1
            
            # Post-order traversal
            pathSumAncestorList(root.left,sum,total_path_sum,result_hashmap)
            pathSumAncestorList(root.right,sum,total_path_sum,result_hashmap)
        pathSumAncestorList(root,sum,0,{'0':1})
        return self.global_counter
            
            
