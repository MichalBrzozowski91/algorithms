# O(N^3) time O(N^2) space complexity solution
def indexController(A,a,b,d,n):
    if a in range(0,n-1-d) and b in range(0,n-1-d):
        if a > b:
            return A[b][a]
        else:
            return A[a][b]
    else:
        return float('-inf')

def indexControllerUpper(A,a,b,d,n):
    if a in range(0,d+2) and b in range(0,d+2):
        if a > b:
            return A[b][a]
        else:
            return A[a][b]
    else:
        return float('-inf')

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid) # Length of a given grid
        M_previous = [[0]*n for i in range(n)] # Matrix of previous diagonal
        M_current = [[0]*n for i in range(n)] # Matrix of current diagonal
        # Lower triangle
        for d in range(n-1,-1,-1): # Diagonal index
            # Right-down corner
            if d == n-1:
                M_current[0][0] = grid[n-1][d]
                continue
            # Diagonal substitution - make a list copy
            for i in range(0,n):
                for j in range(0,n):
                    M_previous[i][j] = M_current[i][j]
            for k_1 in range(0,n-1-d+1): # Movement 1st index
                for k_2 in range(k_1,n-1-d+1): # Movement second index
                    # k_1 equals k_2
                    # Both move right
                    # Index is (n-1-k_1,d+k_1) and (n-1-k_2,d+k_2)
                    if grid[n-1-k_1][d+k_1] == -1 or grid[n-1-k_2][d+k_2] == -1:
                        M_current[k_1][k_2] = float('-inf')
                        continue
                    right_right = indexController(M_previous,k_1,k_2,d,n)
                    right_down = indexController(M_previous,k_1,k_2-1,d,n)
                    down_right = indexController(M_previous,k_1-1,k_2,d,n)
                    down_down = indexController(M_previous,k_1-1,k_2-1,d,n)
                    if k_1 == k_2:
                        M_current[k_1][k_1] = grid[n-1-k_1][d+k_1] + max(right_right,right_down,down_down)
                        continue
                    else:
                        M_current[k_1][k_2] = grid[n-1-k_1][d+k_1] + grid[n-1-k_2][d+k_2] + max(right_right,right_down,down_right,down_down)

        #Upper Triangle
        for d in range(n-2,-1,-1): # Diagonal index
            # Diagonal substitution - make a list copy
            for i in range(0,n):
                for j in range(0,n):
                    M_previous[i][j] = M_current[i][j]
            for k_1 in range(0,d+1): # Movement 1st index
                for k_2 in range(k_1,d+1): # Movement second index
                    # k_1 equals k_2
                    # Both move right
                    # Index is (d-k_1,k_1) and (d-k_2,k_2)
                    if grid[d-k_1][k_1] == -1 or grid[d-k_2][k_2] == -1:
                        M_current[k_1][k_2] = float('-inf')
                        continue
                    right_right = indexControllerUpper(M_previous,k_1+1,k_2+1,d,n)
                    right_down = indexControllerUpper(M_previous,k_1+1,k_2,d,n)
                    down_right = indexControllerUpper(M_previous,k_1,k_2+1,d,n)
                    down_down = indexControllerUpper(M_previous,k_1,k_2,d,n)
                    if k_1 == k_2:
                        M_current[k_1][k_1] = grid[d-k_1][k_1] + max(right_right,right_down,down_down)
                        continue
                    else:
                        M_current[k_1][k_2] = grid[d-k_1][k_1] + grid[d-k_2][k_2] + max(right_right,right_down,down_right,down_down)
        if M_current[0][0] == float('-inf'):
            return 0
        else:
            return M_current[0][0]
