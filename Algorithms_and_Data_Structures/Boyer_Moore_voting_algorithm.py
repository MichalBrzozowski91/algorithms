# Boyer-Moore Voting Algorithm
# Finds a majority element in O(N) time and O(1) space
class Solution:
    def majorityElement(self, nums):
        counter = 0
        state = None
        for num in nums:
            if counter == 0:
                state = num
                counter = 1
            elif state == num:
                counter += 1
            else: # counter != 0, state != num
                counter -= 1
        return state
