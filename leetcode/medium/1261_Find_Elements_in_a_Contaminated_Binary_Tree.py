# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        stack = [root]
        self.hashset = set()
        while stack:
            node = stack.pop()
            self.hashset.add(node.val)
            if node.left:
                node.left.val = 2 * node.val +1
                stack.append(node.left)
            if node.right:
                node.right.val = 2 * node.val +2
                stack.append(node.right)
        self.recovered = root
        #print(self.recovered)
        
    def find(self, target: int) -> bool:
        return target in self.hashset


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)