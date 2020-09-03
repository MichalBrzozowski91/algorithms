# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self,root):
        # Iterative solution
        if not root:
            return []
        result = []
        nodes = [[root,1]]
        while nodes:
            node = nodes[-1]
            tree = node[0]
            flag = node[1]
            if flag == 0:
                result.append(tree.val)
                nodes.pop()
            else:
                nodes[-1][1] = 0 # Node was open
                if tree.right:
                    nodes.append([tree.right,1])
                if tree.left:
                    nodes.append([tree.left,1])
        return result
