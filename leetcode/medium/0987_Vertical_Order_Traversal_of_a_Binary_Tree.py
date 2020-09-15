# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # Depth-first traversal
        if not root:
            return []
        result = {}
        temp_result = {}
        current_list = [(root,0)]
        temp_list = []
        current_min = 0
        while current_list:
            for node,vert in current_list:
                #print(node.val,vert)
                if node.left:
                    temp_list.append((node.left,vert-1))
                    current_min = min(current_min,vert-1)
                if node.right:
                    temp_list.append((node.right,vert+1))
                if str(vert) not in temp_result:
                    temp_result[str(vert)] = [node.val]
                else:
                    temp_result[str(vert)].append(node.val)
            current_list, temp_list = temp_list, []
            for key in temp_result:
                #print(key,result,temp_result)
                temp_result[key].sort()
                if key not in result:
                    result[key] = temp_result[key]
                else:
                    result[key] += temp_result[key]
            temp_result ={}
            
            
        result_list = [0]*len(result)
        minimum = current_min#min(int(key) for key in result.keys())
        #print(result)
        #print(result.keys())
        for key in list(result):
            result_list[-minimum + int(key)] = result[key]
        
        return result_list