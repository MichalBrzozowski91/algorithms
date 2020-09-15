class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        l = len(arr)
        # Create a dp and dp_max grids:
        dp = [[[0] for i in range(l)] for i in range(l)]
        dp_max = [[[0] for i in range(l)] for i in range(l)]
        # We calculate dp for diagonal elements
        for i in range(l):
            dp[i][i] = 0
            dp_max[i][i] = arr[i]
        
        # We calculate dp for other elements
        for k in range(1,l): # Lenght of a subarray
            for i in range(l-k):
                #print('calculating dp[',i,'][',i+k,']')
            #We calculate dp[i][i+k]
                values = [dp[i][j]+dp[j+1][i+k] + dp_max[i][j]*dp_max[j+1][i+k] for j in range(i,i+k)]
                print(dp[i][i],dp[i+1][i+k],dp_max[i][i],dp_max[i+1][i+k])
                dp[i][i+k] = min(values)
                dp_max[i][i+k] = max(arr[i+k],dp_max[i][i+k-1])
                print('values',values,'result:',dp[i][i+k])
        # We returm a value of dp[0][l-1]
        return dp[0][l-1]
            