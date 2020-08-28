class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices == [] or k==0:
            return 0
        # Greedy strategy
        profit = 0
        action_flag = False
        transaction_count = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1] and not action_flag:
                profit -= prices[i] #We buy an action
                action_flag = True
                transaction_count += 1
            elif prices[i]>=prices[i+1] and action_flag:
                profit += prices[i] #We sell an action
                action_flag = False
        if action_flag:
            profit += prices[-1] #We sell an action
            action_flag = False
        print(transaction_count,profit)
        if transaction_count <= k:
            return profit
        
        a = [prices[-1]]*k # Index j is profit with action bought and this is (j+1)-th transaction - we sell an action 
        b = [0]*(k+1) # Index j is profit without action bought and after j transactions - we do nothing
        for p in prices[-2::-1]:
            a_copy = a
            b_copy = b
            for j in range(k):
                a[j] = max(a[j],p + b[j+1]) # We do nothing or sell an action
                b[j] = max(b[j],-p + a_copy[j]) # We do nothing or buy an action
        return b[0]
        
