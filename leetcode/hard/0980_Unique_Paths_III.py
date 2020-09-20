class Solution:
    def uniquePathsIII(self, grid):
        res = 0
        m = len(grid)
        n = len(grid[0])
        obstacles = 0
        start = None
        end = None
        # Find start and end
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == -1:
                    obstacles += 1
        # We will use depth first search and bracktracking
        paths = [[{start},start]] # We store indices of vicited squares and a last position
        new_paths = []
        while paths:
            for path in paths:
               backtracking = path[0]
               last = path[1]
               movements = ((-1,0),(1,0),(0,-1),(0,1))
               for movement in movements:
                   candidate = (last[0] + movement[0],last[1] + movement[1])
                   if candidate == end and len(backtracking) + obstacles + 1 == m*n:
                       res += 1
                   elif candidate == end:
                       pass
                   elif candidate[0] in range(m) and candidate[1] in range(n) and grid[candidate[0]][candidate[1]] != -1 and candidate not in backtracking:
                       new_paths.append([backtracking | {candidate}, candidate])
            paths = new_paths
            new_paths = []
        return res
