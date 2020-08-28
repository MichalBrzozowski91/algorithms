class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        a = prices[-1] #Profit with action bought and this is 1st transaction - we sell an action
        b = prices[-1] #Profit with action bought and this is 2nd transaction - we sell an action
        c = 0 #Profit without action bought and this before transactions - we do nothing
        d = 0 #Profit without action bought and this is after 1st transaction - we do nothing
        #e = 0 #Profit without action bought and this is after 2nd transaction - we do nothing
        for p in prices[-2::-1]:
            #a = max(a,p + d) # We can do nothing or sell an action (1st transaction)
            #b = max(b,p + 0) # We can do nothing or sell an action (2nd transaction)
            #c = max(c,-p + a) # We can do nothing or buy an action (1st transaction)
            #d = max(d, -p + b) # We can do nothing or buy an action (2nd transaction)
            a,b,c,d = max(a,p + d), max(b,p + 0), max(c,-p + a), max(d, -p + b)
        return c
