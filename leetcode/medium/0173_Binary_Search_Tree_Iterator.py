# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        if not root:
            self.list = []
            return None
        self.list = [root] # List of ancestors
        while self.list[-1].left:
            self.list.append(self.list[-1].left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        #print(self.list)
        nextnode = self.list.pop() # Last element of a list
        if nextnode.right:
            self.list += [nextnode.right]
            while self.list[-1].left:
                self.list.append(self.list[-1].left)
        return nextnode.val
    

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.list


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
