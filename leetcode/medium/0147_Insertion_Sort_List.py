class Solution:
    def insertionSortList(self, head):
        if not head:
            return None
        dummy = ListNode(float('-inf'))
        start_sorted = dummy
        end_sorted = dummy
        node = head
        while node:
            next_node = node.next
            pointer = start_sorted
            stop = False
            prev = dummy
            while pointer:
                if pointer.val < node.val:
                    prev = pointer
                    pointer = pointer.next
                    continue
                else:
                    stop = True
                    prev.next = node
                    node.next = pointer
                    break
            if not stop:
                end_sorted.next = node
                end_sorted = node
                node.next = None
            node = next_node
        return dummy.next
