# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def frequencyDictionary(root):
            # Returns a list [frequency dictionary, sum]
            if not root:
                return [{},0]
            # pre-order traversal
            dictionary = {}
            left_path = frequencyDictionary(root.left)
            right_path = frequencyDictionary(root.right)
            
            # Adding two dictionaries
            
            for k in left_path[0]:
                dictionary[k] = left_path[0][k]
            for k in right_path[0]:
                if k in dictionary:
                    dictionary[k] += right_path[0][k]
                else:
                    dictionary[k] = right_path[0][k]
                    
            new_sum = root.val + left_path[1] + right_path[1]
            if str(new_sum) in dictionary:
                dictionary[str(new_sum)] += 1
            else:
                dictionary[str(new_sum)] = 1
            
            #print('Visiting',root.val,'Dictionary:',dictionary,'Sum:',new_sum)
            return [dictionary,new_sum]
            
        result = frequencyDictionary(root)[0]
        if not result:
            return []
        m = max(result.values())
        frequent_list = [key for key, value in result.items() if value == m]
        return frequent_list
        
            
