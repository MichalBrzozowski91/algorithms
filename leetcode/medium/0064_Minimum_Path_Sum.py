class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # Number of rows
        n = len(grid[0]) # Number of columns
        if m == 0 or n == 0:
            return 0
        # Last row
        for j in range(n - 2, -1,-1):
            grid[m-1][j] += grid[m-1][j+1]
        for i in range(m - 2, -1,-1):
            # Last column
            grid[i][n-1] += grid[i+1][n-1]
            for j in range(n-2, -1,-1):
                grid[i][j] += min(grid[i+1][j],grid[i][j+1])
        return grid[0][0]
