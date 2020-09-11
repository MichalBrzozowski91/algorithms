# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        current_tree = root
        while current_tree:
            #print(current_tree)
            if val < current_tree.val:
                if not current_tree.left:
                    current_tree.left = TreeNode(val)
                    break
                else:
                    current_tree = current_tree.left
                    continue
            elif val > current_tree.val:
                if not current_tree.right:
                    current_tree.right = TreeNode(val)
                    break
                else:
                    current_tree = current_tree.right
                    continue
        return root
