class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea: let's use two pointers
        i = 0
        current_max = 0
        for j in range(len(prices)):
            if prices[j] - prices[i] > current_max:
                current_max = prices[j] - prices[i] # We calculate how much we earn buy buying at i and selling at j
            if prices[j] < prices[i]:
                i = j # We move a second pointer if stock price is lower
        return current_max