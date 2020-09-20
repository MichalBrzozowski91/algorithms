class Solution:
    def uniquePaths(self, m, n):
        dp = [[None for _ in range(n)] for _ in range(m)] # Empty dp table
        k = min(m,n)
        for d in range(k):
            # Vertical line
            if d == 0:
                for i in range(d,m):
                    dp[i][d] = 1
                for j in range(d,n):
                    dp[d][j] = 1
            else:
                for i in range(d,m):
                    dp[i][d] = dp[i - 1][d] + dp[i][d - 1]
                for j in range(d,n):
                    dp[d][j] = dp[d - 1][j] + dp[d][j - 1]
            #print(dp)
        return dp[m - 1][n - 1]
