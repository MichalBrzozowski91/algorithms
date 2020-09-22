# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        res = []
        state1 = None
        state2 = None
        counter1 = 0
        counter2 = 0
        for num in nums:
            if num == state1:
                counter1 += 1
            elif num == state2:
                counter2 += 1
            elif counter1 == 0:
                state1 = num
                counter1 = 1
            elif counter2 == 0:
                state2 = num
                counter2 = 1
            else: # We have three different observations: state1, state2 and num, we forget about them
                counter1 -= 1
                counter2 -= 1
                if counter1 == 0:
                    state1 = None
                if counter2 == 0:
                    state2 = None
        # We have 2 candidates: state1 and state2
        count = sum(1 for num in nums if num == state1)
        if count > len(nums) // 3:
            res.append(state1)
        count = sum(1 for num in nums if num == state2)
        if count > len(nums) // 3:
            res.append(state2)
        return res
