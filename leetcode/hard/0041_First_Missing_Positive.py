class Solution:
    def firstMissingPositive(self, nums):
        # Changing signs solution O(N) space, O(1) time
        # Eliminate nonpositive numbers
        l = len(nums)
        i = 0
        while i in range(l):
            if nums[i] <= 0:
                nums[i] = l + 2
            else:
                i += 1
        # Changing signs
        for num in nums:
            if abs(num) in range(1,l + 1):
                nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        # Looking for the answer
        for i in range(l):
            if nums[i] > 0:
                return i + 1
        return l + 1
