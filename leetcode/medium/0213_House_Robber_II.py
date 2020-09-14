class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = 0
        # Maximal gain if we skip the first house
        dp = 0 # Maximal money under the condition that we did not rob the last house
        dp_last = 0 # Maximal money under the condition that we did rob the last house
        for i in range(1,len(nums)):
            dp, dp_last = max(dp,dp_last), dp + nums[i]
        result = max(dp,dp_last)
        # Maximal gain if we skip the last house
        dp = 0 # Maximal money under the condition that we did not rob the last house
        dp_last = 0 # Maximal money under the condition that we did rob the last house
        for i in range(len(nums) - 1):
            dp, dp_last = max(dp,dp_last), dp + nums[i]
        result = max(result,max(dp,dp_last))
        return result
