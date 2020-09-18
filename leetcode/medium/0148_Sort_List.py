# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Merge sort
    def merge(self, head1, head2):
        '''
        Merges two sorted linked lists \n
        Return head and tail of a merged list \n
        Works in-place \n
        '''
        #print('merging',printLinked(head1),'with',printLinked(head2))
        if not head1:
            return head2
        if not head2:
            return head1
        node1 = head1
        node2 = head2
        if head1.val < head2.val:
            merged_head = head1
            node1 = node1.next
        else:
            merged_head = head2
            node2 = node2.next
        node = merged_head
        while node1 or node2:
            if not node1:
                node.next = node2
                node2 = node2.next
            elif not node2:
                node.next = node1
                node1 = node1.next
            elif node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        #print('Merged list:',printLinked(merged_head))
        return merged_head
                
        
    def sortList(self,head):
        '''The function returns a head of a sorted list'''
        if not head:
            return None
        if not head.next:
            return head
        # Find a half of a linked list
        a = head
        b = head.next
        while b and b.next:
            a = a.next
            b = b.next.next
        half = a
        # We divide the linked list in two parts
        right_half = half.next
        half.next = None
        left_half = head
        # We sort the halves
        left = self.sortList(left_half)
        right = self.sortList(right_half)
        # Merge left and right
        return self.merge(left, right)
        
