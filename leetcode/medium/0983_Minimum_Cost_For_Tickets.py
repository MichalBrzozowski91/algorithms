class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l = len(days)
        dp = [0 for i in range(l+1)]
        dp[l] = 0
        for i in reversed(range(l)):
            # 1-day pass; over at the day days[i] 
            candidate = dp[i+1] + costs[0]
            # 7-day pass; over at the day days[i] + 6
            for j in range(i+1,l+1):
                if j == l or days[j] > days[i] + 6:
                    candidate = min(candidate,dp[j]+costs[1])
                    break
            # 30-day pass; over at the days[i] + 29
            for j in range(i+1,l+1):
                if j == l or days[j] > days[i] + 29:
                    candidate = min(candidate,dp[j] + costs[2])
                    break
            dp[i] = candidate
        return dp[0]