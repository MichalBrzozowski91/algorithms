class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_max = nums[0] # Current maximum
        dp_max_right = nums[0] # Current maximum which can be enlarged
        dp_min_right = nums[0] # Current minimum (negative number) which can be enlarged
        for i in range(1,len(nums)):
            val = nums[i]
            if val <= 0:
                dp_max_right, dp_min_right = max(dp_min_right*val,val), min(dp_max_right*val,val)                
            else:
                dp_max_right, dp_min_right = max(dp_max_right*val,val), min(dp_min_right*val,val)
            dp_max = max(dp_max,dp_max_right)
        return dp_max
        
