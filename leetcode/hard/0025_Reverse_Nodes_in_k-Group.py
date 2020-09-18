class Solution:
    def reverseKGroup(self, head, k):
        # Edge cases
        if not head or not head.next:
            return head
        if k == 1:
            return head
        # Consider the first point
        first_group = True
        counter = 1
        prev = None
        start = end = head
        # Create a pointer which is k - 1 nodes ahead of a first pointer
        pointer = head
        for _ in range(k - 1):
            pointer = pointer.next
        new = head.next
        pointer = pointer.next
        # Loop over next nodes
        while new:
            next_new = new.next # We remember that before changing new_next
            if counter < k: # The group has less than k elements
                if not first_group:
                    prev.next = new
                new.next, end.next = start, new.next
                start = new
                counter += 1
            else: # counter = k
                if not pointer: # We cannot start another group, we do not have enough nodes ahead
                    return head
                else: # We start another group
                    first_group = False
                    prev = end
                    start = new
                    end = new
                    counter = 1
            if first_group:
                head = start
            new = next_new
            if pointer:
                pointer = pointer.next
        return head