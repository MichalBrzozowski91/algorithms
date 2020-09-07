# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # Find a length of a list
        length = 0
        node = root
        while node:
            length += 1
            node = node.next
        # Integer division
        partsize = length // k
        additional = length - partsize * k
        # We need additional parts with the size: partsize + 1
        # and k - additional parts with the size: partsize
        sizes =  [partsize] * (k - additional) + [partsize + 1] * (additional)
        # Create partial linked lists
        result = []
        node = root
        while sizes:
            size = sizes.pop()
            if size == 0:
                result.append(None)
                continue
            counter = 0
            startnode = node
            while counter < size:
                prev = node
                counter += 1
                node = node.next
            prev.next = None
            result.append(startnode)
        return result 
