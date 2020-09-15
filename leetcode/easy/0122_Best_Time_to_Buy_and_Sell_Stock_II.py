class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0        
        for i in range(1,len(prices)):
            r = prices[i]-prices[i-1]
            if r > 0:
                s += r
        return s