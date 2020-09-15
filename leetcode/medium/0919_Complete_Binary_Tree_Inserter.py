# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, v: int) -> int:
        # Depth first search
        node_list = [self.root]
        new_list = []
        while True:
            for node in node_list:
                #print(node.val,node_list)
                if not node.left:
                    node.left = TreeNode(v)
                    return node.val
                if not node.right:
                    node.right = TreeNode(v)
                    return node.val
                new_list += [node.left,node.right]
            node_list = new_list
            new_list = []

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()