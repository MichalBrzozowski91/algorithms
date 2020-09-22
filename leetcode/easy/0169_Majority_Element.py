# Boyer-Moore Voting Algorithm
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
