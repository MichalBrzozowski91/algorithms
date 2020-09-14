class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = 0 # Maximal money under the condition that we did not rob the last house
        dp_last = 0 # Maximal money under the condition that we did rob the last house
        for house in nums:
            dp, dp_last = max(dp,dp_last), dp + house
        return max(dp,dp_last)
