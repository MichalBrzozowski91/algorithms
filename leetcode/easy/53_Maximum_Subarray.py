class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0 # Current running sum
        max_sum = nums[0]
        for j in range(len(nums)):
            s += nums[j]
            if s > max_sum:
                max_sum = s # Changing the current maximum
            if s < 0:
                s = 0 # Dropping a negative tail
        return max_sum
