class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit_cooldown = 0
        #profit_noaction_bought = 0
        #profit_action_bought = 0
        if prices == []: # No prices
            return 0
        # Last day of transactions:
        profit_cooldown = 0 # We cannot make any transaction
        profit_noaction_bought = 0 # We cannot buy any action in the last day
        profit_action_bought = prices[-1] # We sell an action we have
        for p in prices[-2::-1]:
                #profit_cooldown = profit_noaction_bought # Cooldown stops
                #profit_noaction_bought = max(profit_noaction_bought, - prices[i] + profit_action_bought) # We do nothing or we buy an action
                #profit_action_bought = max(profit_action_bought, prices[i] + profit_cooldown) # We do nothing or we sell an action and have to cooldown
                profit_cooldown, profit_noaction_bought, profit_action_bought = \
                profit_noaction_bought, \
                max(profit_noaction_bought, - p + profit_action_bought), \
                max(profit_action_bought, p + profit_cooldown)
        return profit_noaction_bought
