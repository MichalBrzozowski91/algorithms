class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = obstacleGrid # Dp table with obstacles
        k = min(m,n)
        for d in range(k):
            if d == 0:
                dp[0][0] = 1 * (1 - dp[0][0]) # Left upper corner
                for i in range(d + 1,m):
                    dp[i][d] = dp[i - 1][d] * (1 - dp[i][d]) # Multiplication by (1 - dp[i][d]) means that the value dp[i][d] is equal to 0 if there is an obstacle there
                for j in range(d + 1,n):
                    dp[d][j] = dp[d][j - 1] * (1 - dp[d][j])
            else:
                for i in range(d,m):
                    dp[i][d] = (dp[i - 1][d] + dp[i][d - 1]) * (1 - dp[i][d])
                for j in range(d + 1,n):
                    dp[d][j] = (dp[d - 1][j] + dp[d][j - 1]) * (1 - dp[d][j])
        return dp[m - 1][n - 1]
