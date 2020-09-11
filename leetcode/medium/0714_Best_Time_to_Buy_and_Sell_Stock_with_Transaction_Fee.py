class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        a = prices[-1] - fee # Strategy with an action bought
        b = 0 # Strategy without an action bought
        for p in prices[-2::-1]:
            a = max(p + b - fee,a) # We can sell an action or pass
            b = max( - p + a, b) # We can buy an action or pass
        return b
